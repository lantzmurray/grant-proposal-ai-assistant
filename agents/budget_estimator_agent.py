"""Budget estimator agent for Project 23."""

from agents.base import run_agent_task


def estimate_budget(session_id: str, context_data: dict) -> str:
    """Break a proposal budget into defensible categories and risks."""
    return run_agent_task(
        session_id=session_id,
        agent_name="Budget Estimator",
        context_data=context_data,
        objective=(
            "Estimate the budget categories a proposal will need and explain how "
            "the costs connect back to the stated project goals."
        ),
        sections=[
            "Budget categories",
            "Justification notes",
            "Budget risks or watchouts",
        ],
        extra_guidance=(
            "Favor ranges and rationale over fake exact numbers. Call out where "
            "quotes or agency guidance would still be needed."
        ),
    )
