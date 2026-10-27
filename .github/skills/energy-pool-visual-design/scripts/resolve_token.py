#!/usr/bin/env python3
"""Resolve Energy Pool design tokens from the Figma exports stored in this repository.

Read-only helper (standard library only). It never edits the exports.

Usage:
  resolve_token.py palette.orange-popsicle.orange-popsicle   # resolve one token
  resolve_token.py --search orange                           # find tokens by name
  resolve_token.py --audit                                   # list unresolved references
Run from anywhere; paths are computed from this file's location.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
FILES = {
    "primitive": ROOT / "colors" / "Default.tokens.json",
    "component": ROOT / "colors" / "Mode 1.tokens 3.json",
    "typography": ROOT / "typography" / "Mode 1.tokens.json",
    "spacing": ROOT / "spacing" / "Mode 1.tokens 2.json",
}
REF = re.compile(r"^\{(.+)\}$")


def load():
    tokens = {}
    for source, path in FILES.items():
        data = json.loads(path.read_text(encoding="utf-8"))

        def walk(node, trail):
            if "$type" in node or "$value" in node:
                tokens[".".join(trail)] = (source, node)
                return
            for key, child in node.items():
                if not key.startswith("$") and isinstance(child, dict):
                    walk(child, trail + [key])

        walk(data, [])
    return tokens


def raw(node):
    value = node.get("$value")
    return value["hex"] if isinstance(value, dict) and "hex" in value else value


def resolve(name, tokens, seen=()):
    """Return (final value, chain). The value is None when a reference is unresolved."""
    if name not in tokens:
        return None, list(seen) + [f"UNRESOLVED:{name}"]
    source, node = tokens[name]
    value = raw(node)
    match = REF.match(value) if isinstance(value, str) else None
    if not match:
        return value, list(seen) + [f"{name} [{source}]"]
    if name in seen:
        return None, list(seen) + [f"CYCLE:{name}"]
    return resolve(match.group(1), tokens, tuple(seen) + (name,))


def alias_name(node):
    return node.get("$extensions", {}).get("com.figma.aliasData", {}).get("targetVariableName")


def main(argv):
    tokens = load()
    if argv[:1] == ["--audit"]:
        bad = 0
        for name, (_, node) in tokens.items():
            value, chain = resolve(name, tokens)
            if value is None:
                bad += 1
                print(f"UNRESOLVED  {name}: {chain[-1]}")
        # Figma aliases that point to a collection which is not in the exports
        figma_only = {}
        for name, (_, node) in tokens.items():
            target = alias_name(node)
            if target and target not in ("null", "inherit") and not target.startswith(("palette/", "rem/", "em/")):
                figma_only.setdefault(target, []).append(name)
        for target, users in sorted(figma_only.items()):
            print(f"FIGMA-ONLY ALIAS  {target}  (used by {', '.join(users)}); semantic layer not exported")
        print(f"{len(tokens)} tokens, {bad} unresolved references")
    elif argv[:1] == ["--search"] and len(argv) > 1:
        for name in tokens:
            if argv[1].lower() in name.lower():
                print(name)
    elif argv:
        value, chain = resolve(argv[0], tokens)
        print("value:", value if value is not None else "UNRESOLVED (report it, do not guess)")
        print("chain:", " -> ".join(chain))
        target = alias_name(tokens[argv[0]][1]) if argv[0] in tokens else None
        if target:
            print("figma alias:", target)
    else:
        print(__doc__)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
