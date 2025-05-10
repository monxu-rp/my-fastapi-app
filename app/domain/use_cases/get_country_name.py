from app.domain.ports.country_service import CountryService
from app.domain.exceptions.exceptions import CountryNotFoundException

class GetCountryName:
    def __init__(self, country_service: CountryService):
        self.country_service = country_service

    async def execute(self, code: str) -> str:
        try:
            return await self.country_service.get_country_name(code)
        except CountryNotFoundException:
            raise
        except Exception as e:
            raise Exception(f"Unexpected error in use case: {e}") from e