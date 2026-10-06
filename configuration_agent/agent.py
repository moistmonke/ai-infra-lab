from google.adk.agents import Agent

def suggest_fix(issue: str) -> dict:
    """Suggests a configuration fix for a given issue description."""
    fixes = {
        "disk": "Run 'sudo apt autoremove' and clear old logs in /var/log.",
        "memory": "Check for runaway processes with 'top' or 'htop'.",
    }
    for key, fix in fixes.items():
        if key in issue.lower():
            return {"issue": issue, "suggested_fix": fix}
    return {"issue": issue, "suggested_fix": "No known fix for this issue yet."}

root_agent = Agent(
    name="configuration_agent",
    model="gemini-3.5-flash-lite",
    description="Suggests and applies configuration fixes based on reported issues.",
    instruction=(
        "You are a configuration agent. Given a system issue, suggest a clear, "
        "actionable fix using your tools."
    ),
    tools=[suggest_fix],
)