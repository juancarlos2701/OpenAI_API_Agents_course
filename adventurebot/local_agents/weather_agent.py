"""Agent for analyzing weather conditions and providing trip-specific weather recommendations."""

from datetime import datetime
from typing import Optional, List, Sequence
from pydantic import BaseModel

from agents import Agent, WebSearchTool
from agents.mcp import MCPServer
from models import TripContext

PROMPT = f"""You are a weather analyst that helps travelers prepare for their trip using provided weather tools.
        The current date is {datetime.now().date()}.

        1. Determine the latitude and longitude for the trip destination.
        2. Determine if the trip start date is within 7 days from the current date (use the 'get_forecast' tool for this). The forecast tool provides a 7-day forecast.
        3. If the trip is within 7 days:
           - Use the 'get_forecast' tool to get the daily forecast.
           - Extract relevant information (temperature range, precipitation, weather code) for the specific trip dates.
           - Provide a summary, temperature range, precipitation chance, clothing recommendations, and any warnings based *only* on the forecast data.
        4. If the trip is more than 7 days away:
           - Use the 'get_current_weather' tool to get the current conditions as a general indicator.
           - Provide a summary based on current conditions, stating that a specific forecast is not yet available. Include general clothing recommendations for the current weather.
           - Set temperature_range to the current temperature (as both min and max).
           - Set precipitation_chance based on current precipitation.
        5. Return a structured analysis using the WeatherAnalysis format.

        Always use the 'get_forecast' or 'get_current_weather' tools. Do not use web search."""


class WeatherAnalysis(BaseModel):
    """Weather analysis with recommendations"""

    summary: str
    temperature_range: List[float]  # [min_temp, max_temp]
    precipitation_chance: float
    recommended_clothing: List[str]
    weather_warnings: Optional[List[str]] = None


def create_weather_agent(mcp_servers: Sequence[MCPServer]) -> Agent[TripContext]:
    """Create a weather analysis agent that provides weather information for a trip using provided MCP servers.

    It uses the 'get_forecast' tool for trips within 7 days and 'get_current_weather'
    for trips further out.
    """
    return Agent[TripContext](
        name="Weather Agent",
        instructions=PROMPT,
        output_type=WeatherAnalysis,
        tools=[WebSearchTool()],
        mcp_servers=mcp_servers,
        model="gpt-4o",
    )
