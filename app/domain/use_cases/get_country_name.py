from app.domain.ports.country_service import CountryService

class GetCountryName:
    def __init__(self, country_service: CountryService):
        self.country_service = country_service

    async def execute(self, code: str) -> str:
        return await self.country_service.get_country_name(code)