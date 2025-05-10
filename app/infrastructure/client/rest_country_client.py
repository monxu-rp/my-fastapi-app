import httpx

from app.domain.exceptions.exceptions import CountryNotFoundException
from app.domain.ports.country_service import CountryService
from config.config import BASE_URL

class RestCountryClient(CountryService):
    def __init__(self, base_url: str = None):
        self.base_url = base_url or BASE_URL

    async def get_country_name(self, code: str) -> str:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(f"{self.base_url}/alpha/{code}")
                response.raise_for_status()
                data = response.json()
                return data[0]['name']['common']
            except httpx.HTTPStatusError as e:
                if e.response.status_code == 404:
                    raise CountryNotFoundException(f"Country code '{code}' not found")
                raise RuntimeError("Error fetching country data") from e
            except Exception as e:
                raise RuntimeError(f"Unexpected error: {e}") from e