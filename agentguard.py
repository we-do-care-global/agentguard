#!/usr/bin/env python3
"""
AgentGuard CLI — Agent Security Scanner
Scans agent tool configurations for security vulnerabilities:
- Overly permissive tool permissions
- Missing input validation
- Indirect prompt injection vectors
- Unrestricted file system access
- Missing rate limiting

Usage:
    python agentguard.py scan <path>
    python agentguard.py scan . --format json
    python agentguard.py scan . --severity high
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any


# Security patterns to detect
SECURITY_PATTERNS = {
    "overly_permissive": {
        "pattern": r"(allow_all|permit_all|unrestricted|no.?limit)",
        "severity": "high",
        "message": "Overly permissive tool permission detected",
    },
    "missing_validation": {
        "pattern": r"(eval|exec|subprocess|os\.system|shell=True)",
        "severity": "critical",
        "message": "Dangerous function call without input validation",
    },
    "prompt_injection": {
        "pattern": r"(ignore.*previous|disregard.*instructions|system.*prompt)",
        "severity": "high",
        "message": "Potential prompt injection vector",
    },
    "unrestricted_fs": {
        "pattern": r"(open\(|read_file|write_file|Path\(|os\.path)",
        "severity": "medium",
        "message": "File system access without path restriction",
    },
    "missing_auth": {
        "pattern": r"(api_key|token|secret|password)\s*=\s*['\"]",
        "severity": "critical",
        "message": "Hardcoded credential detected",
    },
    "no_rate_limit": {
        "pattern": r"(requests\.|httpx\.|urllib|aiohttp)",
        "severity": "medium",
        "message": "HTTP client without rate limiting",
    },
}

# File extensions to scan
SCAN_EXTENSIONS = {".py", ".js", ".ts", ".json", ".yaml", ".yml", ".toml"}


def scan_file(filepath: Path) -> list[dict[str, Any]]:
    """Scan a single file for security issues."""
    issues = []
    try:
        content = filepath.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return issues

    for check_name, check in SECURITY_PATTERNS.items():
        pattern = check["pattern"]
        for match in re.finditer(pattern, content, re.IGNORECASE):
            line_num = content[: match.start()].count("\n") + 1
            issues.append(
                {
                    "file": str(filepath),
                    "line": line_num,
                    "check": check_name,
                    "severity": check["severity"],
                    "message": check["message"],
                    "match": match.group(0),
                }
            )
    return issues


def scan_directory(path: Path) -> list[dict[str, Any]]:
    """Recursively scan directory for security issues."""
    issues = []
    for root, _dirs, files in os.walk(path):
        # Skip common non-source directories
        if any(skip in root for skip in [".git", "__pycache__", "node_modules", ".venv"]):
            continue
        for filename in files:
            filepath = Path(root) / filename
            if filepath.suffix in SCAN_EXTENSIONS:
                issues.extend(scan_file(filepath))
    return issues


def format_text(issues: list[dict[str, Any]]) -> str:
    """Format issues as human-readable text."""
    if not issues:
        return "✓ No security issues found"

    lines = [f"Found {len(issues)} security issue(s):\n"]
    for issue in issues:
        lines.append(
            f"  [{issue['severity'].upper()}] {issue['file']}:{issue['line']}"
        )
        lines.append(f"    → {issue['message']}")
        lines.append(f"    Match: {issue['match']}")
        lines.append("")
    return "\n".join(lines)


def format_json(issues: list[dict[str, Any]]) -> str:
    """Format issues as JSON."""
    return json.dumps(issues, indent=2)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="AgentGuard — Agent Security Scanner"
    )
    parser.add_argument("command", choices=["scan"], help="Command to run")
    parser.add_argument("path", nargs="?", default=".", help="Path to scan")
    parser.add_argument(
        "--format", choices=["text", "json"], default="text", help="Output format"
    )
    parser.add_argument(
        "--severity",
        choices=["low", "medium", "high", "critical"],
        help="Minimum severity to report",
    )
    args = parser.parse_args()

    target = Path(args.path)
    if not target.exists():
        print(f"Error: {target} does not exist", file=sys.stderr)
        return 1

    if target.is_file():
        issues = scan_file(target)
    else:
        issues = scan_directory(target)

    # Filter by severity
    if args.severity:
        severity_order = {"low": 0, "medium": 1, "high": 2, "critical": 3}
        min_level = severity_order[args.severity]
        issues = [
            i
            for i in issues
            if severity_order.get(i["severity"], 0) >= min_level
        ]

    # Output
    if args.format == "json":
        print(format_json(issues))
    else:
        print(format_text(issues))

    # Exit code: 0 = clean, 1 = issues found
    return 0 if not issues else 1


if __name__ == "__main__":
    sys.exit(main())
