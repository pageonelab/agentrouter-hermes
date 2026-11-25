import json
from pathlib import Path


def register(ctx):
    root = Path(__file__).parent
    skills = json.loads((root / "skills.json").read_text(encoding="utf-8"))
    for name, description in skills.items():
        ctx.register_skill(name, root / "skills" / name / "SKILL.md", description=description)
