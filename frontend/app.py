import streamlit as st
import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PACKAGE_ROOT = os.path.dirname(os.path.dirname(PROJECT_ROOT))
sys.path.insert(0, PROJECT_ROOT)
if PACKAGE_ROOT not in sys.path:
    sys.path.insert(0, PACKAGE_ROOT)

from agents.base import get_session_history
from orchestrator import Orchestrator
from components import render_app_footer, run_with_status_updates

st.set_page_config(page_title="AI-Powered Grant Proposal Assistant", layout="wide")


def render_session_log(session_id: str) -> None:
    """Show the collaboration log so proposal decisions stay traceable."""
    history = get_session_history(session_id)
    if not history:
        return

    st.subheader("Collaboration Log")
    for entry in history:
        timestamp = entry["timestamp"].replace("T", " ")
        with st.expander(f"{entry['agent']} · {timestamp}", expanded=False):
            st.markdown(entry["content"])


def main():
    st.title("AI-Powered Grant Proposal Assistant")
    st.caption("Assist researchers or nonprofits in drafting grant proposals.")

    st.sidebar.title("Proposal Inputs")
    topic = st.sidebar.text_input(
        "Topic",
        placeholder="Community STEM maker lab",
    )
    funding_agency = st.sidebar.text_input(
        "Funding Agency",
        placeholder="State innovation grant program",
    )
    goals = st.text_area(
        "Goals",
        height=220,
        placeholder="Increase access, train mentors, and measure student outcomes.",
    )

    if st.button("Run Proposal Team", type="primary"):
        if not topic.strip():
            st.warning("Add a topic so the grant team can build a useful draft plan.")
            return

        inputs = {
            "topic": topic.strip(),
            "goals": goals.strip(),
            "funding_agency": funding_agency.strip(),
        }
        orch = Orchestrator()
        output = run_with_status_updates(
            lambda: orch.run_workflow(inputs),
            start_message="Agents are drafting the proposal support plan..."
        )

        st.success(f"Workflow Complete! Session ID: {output['session_id']}")

        for agent, response in output["results"].items():
            with st.expander(f"{agent} Response", expanded=True):
                st.markdown(response)

        render_session_log(output["session_id"])


    render_app_footer()

if __name__ == "__main__":
    main()
