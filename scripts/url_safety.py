#!/usr/bin/env python3
"""Small URL safety helper for SEO fetch/adapters.

Adapted conceptually from AgriciDaniel/claude-seo's URL safety pattern.
This compact version rejects non-http(s) URLs, localhost, metadata hosts, and
private/reserved IP literals or DNS results before a script fetches a URL.
"""
from __future__ import annotations

import argparse
import ipaddress
import socket
from urllib.parse import urlparse

BLOCKED_HOSTS = {
    "localhost",
    "metadata.google.internal",
}
BLOCKED_SUFFIXES = (".local", ".internal")


class URLSafetyError(ValueError):
    """Raised when a URL is unsafe for server-side fetching."""


def is_safe_ip(ip: str) -> bool:
    parsed = ipaddress.ip_address(ip)
    return not any(
        [
            parsed.is_private,
            parsed.is_loopback,
            parsed.is_link_local,
            parsed.is_multicast,
            parsed.is_reserved,
            parsed.is_unspecified,
        ]
    )


def validate_url(url: str, *, resolve: bool = True) -> str:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        raise URLSafetyError("URL scheme must be http or https")
    if not parsed.hostname:
        raise URLSafetyError("URL must include a hostname")

    host = parsed.hostname.lower().rstrip(".")
    if host in BLOCKED_HOSTS or host.endswith(BLOCKED_SUFFIXES):
        raise URLSafetyError(f"blocked hostname: {host}")

    try:
        if not is_safe_ip(host):
            raise URLSafetyError(f"blocked IP address: {host}")
    except ValueError:
        pass  # not an IP literal

    if resolve:
        try:
            infos = socket.getaddrinfo(host, parsed.port or (443 if parsed.scheme == "https" else 80), type=socket.SOCK_STREAM)
        except socket.gaierror as exc:
            raise URLSafetyError(f"DNS resolution failed: {host}") from exc
        ips = {str(info[4][0]) for info in infos}
        unsafe = [ip for ip in ips if not is_safe_ip(ip)]
        if unsafe:
            raise URLSafetyError(f"hostname resolves to blocked IP(s): {', '.join(sorted(unsafe))}")

    return parsed.geturl()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("--no-resolve", action="store_true")
    args = parser.parse_args()
    try:
        print(validate_url(args.url, resolve=not args.no_resolve))
    except URLSafetyError as exc:
        print(f"URL unsafe: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
