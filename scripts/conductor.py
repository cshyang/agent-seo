from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

import yaml

PACKAGE_DIR = Path(__file__).resolve().parent  # scripts/ directory within agent-seo repo
REPO_ROOT = PACKAGE_DIR.parent                  # agent-seo repo root
CLIENTS_DIR = REPO_ROOT / ".seo-ops" / "clients"
DEFAULT_RUNS_DIR = REPO_ROOT / ".seo-ops" / "clients" / "_conductor_runs"
REQUIRED_BRIEF_FIELDS = [
    "brief_id",
    "client",
    "target_keyword",
    "target_service_page",
    "intent",
    "audience",
    "required_internal_links",
    "cta",
    "status",
    "brief_doc",
]
STAGES = [
    "research",
    "outline",
    "draft",
    "seo-review",
    "brand-commercial-review",
    "factual-review",
    "comparison",
]


def load_yaml(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise ValueError(f"Expected YAML mapping in {path}")
    return data


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "untitled"


def utc_now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def validate_brief(brief: Dict[str, Any]) -> List[str]:
    errors: List[str] = []
    for field in REQUIRED_BRIEF_FIELDS:
        if field not in brief or brief[field] in (None, "", []):
            errors.append(f"Missing required field: {field}")
    if brief.get("status") not in {"approved_for_research", "draft_brief", "approved_for_draft"}:
        errors.append("status must be draft_brief, approved_for_research, or approved_for_draft")
    links = brief.get("required_internal_links") or []
    if not isinstance(links, list):
        errors.append("required_internal_links must be a list")
    target = brief.get("target_service_page")
    if target and isinstance(links, list) and target not in links:
        errors.append("target_service_page should also be present in required_internal_links")
    return errors


@dataclass
class RunPaths:
    run_dir: Path
    brief: Path
    status: Path
    log: Path


class ContentConductor:
    def __init__(self, package_dir: Path = PACKAGE_DIR, runs_dir: Path = DEFAULT_RUNS_DIR):
        self.package_dir = package_dir
        self.runs_dir = runs_dir
        self.registry_path = package_dir / "model_registry.yaml"
        self.prompts_dir = package_dir / "conductor-prompts"

    def validate_config(self) -> Dict[str, Any]:
        registry = load_yaml(self.registry_path)
        missing = []
        for rel in [
            "conductor-prompts/research.md",
            "conductor-prompts/outline.md",
            "conductor-prompts/writer.md",
            "conductor-prompts/seo-review.md",
            "conductor-prompts/brand-commercial-review.md",
            "conductor-prompts/factual-review.md",
            "conductor-prompts/comparison.md",
        ]:
            if not (self.package_dir / rel).exists():
                missing.append(rel)
        # Also check client data
        for client_rel in [".seo-ops/clients/sua/style-guide.md", ".seo-ops/clients/sua/lead-quality-guardrails.yaml"]:
            if not (REPO_ROOT / client_rel).exists():
                missing.append(client_rel)
        return {"ok": not missing, "missing": missing, "registry_version": registry.get("version")}

    def init_run(self, brief_path: Path, overwrite: bool = False) -> RunPaths:
        brief = load_yaml(brief_path)
        errors = validate_brief(brief)
        if errors:
            raise ValueError("Brief validation failed: " + "; ".join(errors))
        client = slugify(str(brief["client"]))
        brief_id = slugify(str(brief["brief_id"]))
        run_dir = self.runs_dir / client / brief_id
        if run_dir.exists() and not overwrite:
            raise FileExistsError(f"Run already exists: {run_dir}")
        brief_doc = (brief_path.parent / str(brief["brief_doc"])).resolve()
        if not brief_doc.exists():
            raise FileNotFoundError(f"brief_doc not found: {brief_doc}")
        run_dir.mkdir(parents=True, exist_ok=True)
        target_brief = run_dir / "brief.yaml"
        shutil.copyfile(brief_path, target_brief)
        shutil.copyfile(brief_doc, run_dir / "brief.md")
        status = {
            "brief_id": brief["brief_id"],
            "client": brief["client"],
            "created_at": utc_now_iso(),
            "mode": "dry_run_until_api_keys_added",
            "stages": {stage: {"status": "pending"} for stage in STAGES},
            "notes": [
                "Writer routes come from model_registry.yaml -> models.writer.enabled_routes.",
                "No Strapi publish is allowed; draft-only after explicit approval.",
            ],
        }
        write_text(run_dir / "status.json", json.dumps(status, indent=2))
        write_text(run_dir / "run-log.md", f"# Run log — {brief['brief_id']}\n\nCreated: {status['created_at']}\n\n")
        for stage in STAGES:
            packet = self.render_stage_packet(run_dir, stage)
            write_text(run_dir / "stage-prompts" / f"{stage}.md", packet)
        return RunPaths(run_dir=run_dir, brief=target_brief, status=run_dir / "status.json", log=run_dir / "run-log.md")

    def render_stage_packet(self, run_dir: Path, stage: str) -> str:
        if stage not in STAGES:
            raise ValueError(f"Unknown stage: {stage}")
        brief = load_yaml(run_dir / "brief.yaml") if (run_dir / "brief.yaml").exists() else {}
        client = brief.get("client", "sua")
        style = (CLIENTS_DIR / f"{client}/style-guide.md").read_text(encoding="utf-8")
        guardrails = (CLIENTS_DIR / f"{client}/lead-quality-guardrails.yaml").read_text(encoding="utf-8")
        brief_doc_path = run_dir / "brief.md"
        brief_doc = brief_doc_path.read_text(encoding="utf-8") if brief_doc_path.exists() else ""
        registry = load_yaml(self.registry_path)
        prompt_file = self._prompt_file_for_stage(stage)
        prompt = prompt_file.read_text(encoding="utf-8")
        model_route = self._model_route_for_stage(stage, registry)
        prior_artifacts = self._collect_prior_artifacts(run_dir, stage)
        sections = [
            f"# Stage packet: {stage}",
            "## Model route",
            "```json\n" + json.dumps(model_route, indent=2) + "\n```",
            "## Brief (manifest)",
            "```yaml\n" + yaml.safe_dump(brief, sort_keys=False) + "```",
            "## Brief document",
            brief_doc,
            "## Style guide",
            style,
            "## Lead-quality guardrails",
            "```yaml\n" + guardrails + "```",
        ]
        if prior_artifacts:
            sections.append("## Prior stage artifacts")
            sections.append("\n\n---\n\n".join(prior_artifacts))
        sections.append("## Stage prompt")
        sections.append(prompt)
        return "\n\n".join(sections)

    def _collect_prior_artifacts(self, run_dir: Path, stage: str) -> List[str]:
        """Return text content of all prior-stage artifacts that exist on disk."""
        current_idx = STAGES.index(stage)
        artifacts: List[str] = []
        for prior_stage in STAGES[:current_idx]:
            candidates = [
                run_dir / f"{prior_stage}.md",
                run_dir / f"{prior_stage}.json",
                run_dir / "drafts" / f"{prior_stage}.md",
                run_dir / "reviews" / f"{prior_stage}.json",
            ]
            # For the draft stage specifically, also check model-suffixed filenames
            # (draft-primary.md, draft-challenger.md, draft-sonnet.md, draft-glm.md)
            if prior_stage == "draft":
                drafts_dir = run_dir / "drafts"
                if drafts_dir.exists():
                    for draft_file in sorted(drafts_dir.glob("draft*.md")):
                        label = draft_file.relative_to(run_dir)
                        artifacts.append(f"### {prior_stage} ({label})\n\n{draft_file.read_text(encoding='utf-8')}")
                    continue  # skip the single-file candidates below
            for path in candidates:
                if path.exists() and path.stat().st_size > 0:
                    label = path.relative_to(run_dir)
                    artifacts.append(f"### {prior_stage} ({label})\n\n{path.read_text(encoding='utf-8')}")
                    break
        return artifacts

    def _prompt_file_for_stage(self, stage: str) -> Path:
        mapping = {
            "research": "research.md",
            "outline": "outline.md",
            "draft": "writer.md",
            "seo-review": "seo-review.md",
            "brand-commercial-review": "brand-commercial-review.md",
            "factual-review": "factual-review.md",
            "comparison": "comparison.md",
        }
        return self.prompts_dir / mapping[stage]

    def _model_route_for_stage(self, stage: str, registry: Dict[str, Any]) -> Dict[str, Any]:
        models = registry.get("models", {})
        mapping = {
            "research": "research_synthesis",
            "outline": "outline",
            "draft": "writer",
            "seo-review": "seo_reviewer",
            "brand-commercial-review": "brand_commercial_reviewer",
            "factual-review": "factual_reviewer",
            "comparison": "conductor",
        }
        entry = models.get(mapping[stage], {})
        if stage != "draft":
            return entry
        # ponytail: one draft stage, N routes from YAML. Add "challenger" to
        # enabled_routes to run a bake-off; drop it again once you have a winner.
        enabled = entry.get("enabled_routes") or ["primary"]
        return {route: entry[route] for route in enabled if route in entry}

    def status(self, run_dir: Path) -> Dict[str, Any]:
        return json.loads((run_dir / "status.json").read_text(encoding="utf-8"))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="SUA content conductor")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("validate-config", help="Validate local conductor scaffold")

    init = sub.add_parser("init", help="Create a run folder from a brief")
    init.add_argument("--brief", required=True, type=Path)
    init.add_argument("--overwrite", action="store_true")

    render = sub.add_parser("render-stage", help="Render a stage prompt packet")
    render.add_argument("--run-dir", required=True, type=Path)
    render.add_argument("--stage", required=True, choices=STAGES)

    status = sub.add_parser("status", help="Show run status")
    status.add_argument("--run-dir", required=True, type=Path)
    return parser


def main(argv: Optional[Iterable[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    conductor = ContentConductor()
    if args.command == "validate-config":
        result = conductor.validate_config()
        print(json.dumps(result, indent=2))
        return 0 if result["ok"] else 1
    if args.command == "init":
        paths = conductor.init_run(args.brief, overwrite=args.overwrite)
        print(json.dumps({"run_dir": str(paths.run_dir), "brief": str(paths.brief), "status": str(paths.status)}, indent=2))
        return 0
    if args.command == "render-stage":
        print(conductor.render_stage_packet(args.run_dir, args.stage))
        return 0
    if args.command == "status":
        print(json.dumps(conductor.status(args.run_dir), indent=2))
        return 0
    raise AssertionError(args.command)


if __name__ == "__main__":
    raise SystemExit(main())
