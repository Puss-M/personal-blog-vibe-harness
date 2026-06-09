#!/usr/bin/env python3
"""Structural audit for a non-coder-friendly personal blog project."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def exists(root: Path, *parts: str) -> bool:
    return (root.joinpath(*parts)).exists()


def load_package(root: Path) -> dict[str, Any]:
    package_path = root / "package.json"
    if not package_path.exists():
        return {}
    try:
        return json.loads(package_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {"__error__": "package.json is not valid JSON"}


def detect_stack(root: Path, package: dict[str, Any]) -> list[str]:
    stacks: list[str] = []
    deps = {}
    for key in ("dependencies", "devDependencies"):
        value = package.get(key)
        if isinstance(value, dict):
            deps.update(value)

    if "astro" in deps or exists(root, "astro.config.mjs") or exists(root, "astro.config.ts"):
        stacks.append("astro")
    if exists(root, "hugo.toml") or exists(root, "hugo.yaml") or exists(root, "config", "_default"):
        stacks.append("hugo")
    if "next" in deps or exists(root, "next.config.js") or exists(root, "next.config.mjs"):
        stacks.append("next")
    if exists(root, ".pages.yml"):
        stacks.append("pages-cms")
    if exists(root, ".github", "workflows"):
        stacks.append("github-actions")
    return stacks


def audit(root: Path) -> dict[str, Any]:
    package = load_package(root)
    scripts = package.get("scripts", {}) if isinstance(package.get("scripts"), dict) else {}
    stacks = detect_stack(root, package)
    findings: list[dict[str, str]] = []

    def add(level: str, item: str, detail: str) -> None:
        findings.append({"level": level, "item": item, "detail": detail})

    if not root.exists():
        add("error", "project-root", "Project root does not exist.")
        return {"root": str(root), "stacks": [], "findings": findings}

    if package.get("__error__"):
        add("error", "package.json", str(package["__error__"]))

    if "astro" in stacks:
        if "build" not in scripts:
            add("error", "build-script", "Astro project has no package.json build script.")
        if "dev" not in scripts:
            add("warn", "dev-script", "Astro project has no package.json dev script.")
        if not exists(root, "src", "content"):
            add("warn", "content", "No src/content folder found for Markdown content.")
        if not (exists(root, "src", "content", "blog") or exists(root, "src", "content", "posts")):
            add("warn", "posts", "No obvious blog/posts content collection found.")

    if "hugo" in stacks:
        if not (exists(root, "content") or exists(root, "config", "_default")):
            add("warn", "hugo-structure", "No obvious Hugo content/config structure found.")

    if "pages-cms" in stacks:
        pages_config = root / ".pages.yml"
        text = pages_config.read_text(encoding="utf-8", errors="ignore")
        if "media:" not in text:
            add("error", "pages-cms-media", ".pages.yml has no media section.")
        if "content:" not in text:
            add("error", "pages-cms-content", ".pages.yml has no content section.")
        if "src/content" in text and not exists(root, "src", "content"):
            add("warn", "pages-cms-paths", ".pages.yml references src/content, but it does not exist.")
    else:
        add("info", "cms", "No Pages CMS configuration detected.")

    if "github-actions" in stacks:
        workflows = list((root / ".github" / "workflows").glob("*.yml"))
        workflows += list((root / ".github" / "workflows").glob("*.yaml"))
        if not workflows:
            add("warn", "workflow", ".github/workflows exists but contains no YAML workflows.")
    else:
        add("info", "deployment", "No GitHub Actions workflow detected.")

    if not (exists(root, "public", "media") or exists(root, "static") or exists(root, "assets")):
        add("warn", "media", "No obvious media folder found.")

    if not exists(root, ".gitignore"):
        add("warn", "gitignore", "No .gitignore found.")

    if not findings:
        add("ok", "project", "No structural issues detected.")

    return {"root": str(root), "stacks": stacks, "findings": findings}


def print_markdown(result: dict[str, Any]) -> None:
    print(f"# Blog Project Audit\n\nRoot: `{result['root']}`")
    stacks = ", ".join(result["stacks"]) if result["stacks"] else "unknown"
    print(f"\nDetected stack: {stacks}\n")
    for finding in result["findings"]:
        print(f"- **{finding['level']}** `{finding['item']}`: {finding['detail']}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_root", help="Path to the blog project root")
    parser.add_argument("--json", action="store_true", help="Print JSON instead of Markdown")
    args = parser.parse_args()

    result = audit(Path(args.project_root).resolve())
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print_markdown(result)

    return 1 if any(item["level"] == "error" for item in result["findings"]) else 0


if __name__ == "__main__":
    raise SystemExit(main())
