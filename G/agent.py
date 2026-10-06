from google.adk.agents import Agent
from monitoring_agent.agent import root_agent as monitoring_agent
from configuration_agent.agent import root_agent as configuration_agent

root_agent = Agent(
    name="orchestrator_agent",
    model="gemini-3.5-flash-lite",
    description="Coordinates monitoring and configuration agents to keep systems healthy.",
    instruction=(
        "First use the monitoring agent to check system health. "
        "If any issues are found, pass them to the configuration agent "
        "to get a suggested fix, then report both the issue and the fix."
    ),
    sub_agents=[monitoring_agent, configuration_agent],
)