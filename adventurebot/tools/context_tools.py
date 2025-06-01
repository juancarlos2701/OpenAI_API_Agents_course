"""Utility tools for managing and processing trip context data."""

from agents import RunContextWrapper, function_tool
from ..models import TripContext, CHILD_AGE_THRESHOLD


@function_tool
def check_child_threshold_status(context: RunContextWrapper[TripContext]) -> str:
    """Check if any participants meet the child age threshold.

    :param context: The trip context wrapper containing participant information
    :return: True if any participant is below the child age threshold, False otherwise
    """
    
    if not context.context or not context.context.query:
        return "Error:Trip query context not found."
    
    meets_threshold = any(age < CHILD_AGE_THRESHOLD for age in context.context.query.participant_ages)
    context.context.meets_child_threshold = meets_threshold

    return f"Child threshold check complete. Children present: {"Yes" if meets_threshold else "No"}."

