# api/service/me.py
import httpx
import random
import logging
from datetime import datetime, timezone
from typing import Optional

from core.settings import settings

logger = logging.getLogger("me-service")

# Fallback cat facts if external API fails
LOCAL_FALLBACK_FACTS = [
    "Cats have five toes on their front paws, but only four on their back paws.",
    "A group of cats is called a clowder.",
    "Cats sleep 12–16 hours a day on average.",
    "The world's oldest cat lived to be 38 years old."
]


async def fetch_cat_fact() -> Optional[str]:
    """Fetch a random cat fact from the Cat Facts API."""
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(settings.CATFACT_URL, timeout=settings.CATFACT_TIMEOUT_SECONDS)
            resp.raise_for_status()
            data = resp.json()
            return data.get("fact")
    except Exception as e:
        logger.error(f"Failed to fetch cat fact: {e}")
        return None


def utc_iso_now() -> str:
    """Return current UTC time in ISO 8601 format."""
    return datetime.now(timezone.utc).isoformat(timespec="microseconds").replace("+00:00", "Z")


async def get_me_response() -> dict:
    """Build and return the /me response data."""
    timestamp = utc_iso_now()
    fact = await fetch_cat_fact()

    if fact is None:
        if settings.FAIL_ON_CATFACT_ERROR:
            return {
                "status": "error",
                "message": "Failed to fetch cat fact from external API"
            }
        # fallback fact
        fact = random.choice(LOCAL_FALLBACK_FACTS)
        logger.info("Using fallback cat fact.")

    return {
        "status": "success",
        "user": {
            "email": settings.EMAIL,
            "name": settings.FULL_NAME,
            "stack": settings.STACK,
        },
        "timestamp": timestamp,
        "fact": fact,
    }
