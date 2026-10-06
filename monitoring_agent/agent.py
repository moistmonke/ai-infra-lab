from google.adk.agents import Agent

def check_disk_usage() -> dict:
    """Checks disk usage and returns status."""
    import shutil
    total, used, free = shutil.disk_usage("/")
    percent_used = round((used / total) * 100, 1)
    return {
        "status": "ok" if percent_used < 85 else "warning",
        "percent_used": percent_used
    }

root_agent = Agent(
    name="monitoring_agent",
    model="gemini-3.5-flash-lite",
    description="Monitors system health and reports on disk, memory, and service status.",
    instruction=(
        "You are a monitoring agent. Use your tools to check system health "
        "and clearly report any issues found, including specific numbers."
    ),
    tools=[check_disk_usage],
)