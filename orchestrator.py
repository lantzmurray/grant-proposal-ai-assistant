"""Orchestrator for Project 23."""

import os
import sys
from typing import Any, Dict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from agents.base import generate_session_id, log_agent_response
from agents.outline_designer_agent import design_outline
from agents.budget_estimator_agent import estimate_budget
from agents.reviewer_simulation_agent import simulate_review

AGENT_SEQUENCE = (
    ("Outline Designer", design_outline),
    ("Budget Estimator", estimate_budget),
    ("Reviewer Simulation Agent", simulate_review),
)


class Orchestrator:
    """Run the proposal-planning workflow using a stable agent order."""

    def generate_session_id(self) -> str:
        return generate_session_id()

    def run_workflow(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        session_id = self.generate_session_id()
        results = {}

        log_agent_response(
            session_id,
            "Workflow Input",
            "\n".join(
                f"- {key.replace('_', ' ').title()}: {value or 'Not provided'}"
                for key, value in inputs.items()
            ),
            {"kind": "input"},
        )

        for agent_name, agent_runner in AGENT_SEQUENCE:
            results[agent_name] = agent_runner(session_id, inputs)

        return {"session_id": session_id, "results": results}
