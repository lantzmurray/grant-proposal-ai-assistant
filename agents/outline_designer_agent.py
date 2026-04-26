"""Outline designer agent for Project 23."""

from agents.base import run_agent_task


def design_outline(session_id: str, context_data: dict) -> str:
    """Turn the project idea into a grant-ready narrative structure."""
    return run_agent_task(
        session_id=session_id,
        agent_name="Outline Designer",
        context_data=context_data,
        objective=(
            "Translate the user's topic, goals, and funding agency into a clear "
            "grant narrative structure with sections worth drafting next."
        ),
        sections=[
            "Proposal structure",
            "Evidence or detail gaps",
            "Immediate drafting plan",
        ],
        extra_guidance=(
            "Make the outline feel credible for a real submission while staying "
            "honest about assumptions or missing source material."
        ),
    )
