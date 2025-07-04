"""Agent definitions for the AdventureBot application"""

from agents import Agent, Runner, trace, gen_trace_id

# Import the consolidated agent creation functions and their output types
from local_agents.weather_agent import create_weather_agent, WeatherAnalysis
from local_agents.recommender_agent import create_recommendation_agent, TripPlan, ActivityRecommendation
from local_agents.kid_friendly_agent import create_kid_friendly_activity_agent
from local_agents.search_agent import create_activity_search_agent

# Import models from the central models file
from models import SearchResult, ActivityResult

__all__ = [
    # Agent creation functions
    'create_weather_agent',
    'create_recommendation_agent',
    'create_kid_friendly_activity_agent',
    'create_activity_search_agent',

    # Model types (consolidated)
    'WeatherAnalysis',
    'ActivityResult',
    'TripPlan',
    'ActivityRecommendation',
    'SearchResult',

    # SDK re-exports
    'Agent',
    'Runner',
    'trace',
    'gen_trace_id'
]