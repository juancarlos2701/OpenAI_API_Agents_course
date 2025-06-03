"""Entry point for the AdventureBot application. Handles trip planning initialization and execution."""

from dotenv import load_dotenv

import asyncio

from manager import AdventureManager
from models import TripQuery


load_dotenv()


async def main() -> None:
    """
    Main entry point for the AdventureBot application.
    Creates a sample trip query and runs the adventure planning process.
    """
    # Sample trip query data
    query = TripQuery(
        start_date="2025-06-05",
        end_date="2025-06-14",
        location="Bogota",
        participant_number=3,
        participant_ages=[32, 35, 10],
    )

    # Initialize and run the adventure manager
    await AdventureManager().run(query)


if __name__ == "__main__":
    asyncio.run(main())
