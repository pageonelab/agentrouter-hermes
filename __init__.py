from pathlib import Path


def register(ctx):
    ctx.register_skill(
        "competitor-brief",
        Path(__file__).parent / "skills" / "competitor-brief" / "SKILL.md",
        description="Compare organic search results and recent Reddit mentions for up to three competitors.",
    )
