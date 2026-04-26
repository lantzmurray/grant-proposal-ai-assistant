"""Reviewer simulation agent for Project 23."""

from agents.base import run_agent_task


def simulate_review(session_id: str, context_data: dict) -> str:
    """Pressure-test the proposal like a skeptical reviewer would."""
    return run_agent_task(
        session_id=session_id,
        agent_name="Reviewer Simulation Agent",
        context_data=context_data,
        objective=(
            "Simulate how a grant reviewer might react to the current proposal "
            "idea, calling out both strengths and likely objections."
        ),
        sections=[
            "Reviewer positives",
            "Likely objections",
            "Fixes before submission",
        ],
        extra_guidance=(
            "Be specific and actionable. The goal is not to reject the idea, but "
            "to make the next draft stronger."
        ),
    )
