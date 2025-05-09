import httpx
from app.domain.ports.country_service import CountryService
from config.config import BASE_URL

class RestCountryClient(CountryService):
    def __init__(self, base_url: str = None):
        self.base_url = base_url or BASE_URL

    async def get_country_name(self, code: str) -> str:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/alpha/{code}")
            response.raise_for_status()
            data = response.json()
            return data[0]['name']['common']