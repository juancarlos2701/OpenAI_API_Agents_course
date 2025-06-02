"""Agent for performing web searches to find activities and information."""

from agents import Agent, WebSearchTool, handoff
from models import TripContext, CHILD_AGE_THRESHOLD, ActivityResult, SearchResult
from tools.context_tools import check_child_threshold_status

PROMPT = f"""You research and find suitable activities for a trip based on provided details.

            Given the trip details (location, dates, participant ages) and weather information:

                1. **Check for young children:** Use the `check_child_threshold_status` tool to determine if any 
                   participant is under {CHILD_AGE_THRESHOLD} years old. If the tool indicates the threshold is met,
                   **HANDOFF** the task to the 'Kid-Friendly Activity Agent'. Provide the original trip details 
                   and weather summary in the handoff notes.

                2. **If no young children (threshold not met):**
                    a. Internally brainstorm 3-5 relevant search queries focusing on general activities, age-appropriate options (for the adult/older group), weather suitability, and local experiences.
                    b. Execute searches using the **WebSearchTool**.
                    c. For each promising activity found, extract and structure key information:
                        - Name and description
                        - Location
                        - Price range (if available)
                        - Duration (if available)
                        - Weather dependency
                        - Source URL
                    d. Compile a list of structured ActivityResult objects.
                    e. Provide a concise summary of your findings.

            Return the results in the SearchResult format. You MUST use the web search tool."""


def create_activity_search_agent() -> Agent[TripContext]:
    """Create an agent that searches for activities, uses tools, and hands off based on context."""

    from .kid_friendly_agent import create_kid_friendly_activity_agent  # Import locally to avoid potential circular dependency
    kid_friendly_agent = create_kid_friendly_activity_agent()

    return Agent[TripContext](
        name="Activity Search Agent",
        instructions=PROMPT,
        output_type=SearchResult,
        tools=[WebSearchTool(), check_child_threshold_status],
        handoffs=[handoff(kid_friendly_agent)],
        model="gpt-4.1-mini",
    )
