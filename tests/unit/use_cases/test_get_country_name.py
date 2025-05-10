import pytest

from app.domain.exceptions.exceptions import CountryNotFoundException
from app.domain.use_cases.get_country_name import GetCountryName
from app.domain.ports.country_service import CountryService

class MockCountryServiceSuccess(CountryService):
    async def get_country_name(self, code: str) -> str:
        return "Mock Country"

class MockCountryServiceNotFound(CountryService):
    async def get_country_name(self, code: str) -> str:
        raise CountryNotFoundException(f"Country with code {code} not found")

class MockCountryServiceUnexpectedError(CountryService):
    async def get_country_name(self, code: str) -> str:
        raise RuntimeError("Some unexpected error")

@pytest.mark.asyncio
async def test_get_country_name_success():
    use_case = GetCountryName(MockCountryServiceSuccess())
    result = await use_case.execute("us")
    assert result == "Mock Country"

@pytest.mark.asyncio
async def test_get_country_name_not_found():
    use_case = GetCountryName(MockCountryServiceNotFound())
    with pytest.raises(CountryNotFoundException):
        await use_case.execute("xx")

@pytest.mark.asyncio
async def test_get_country_name_unexpected_error():
    use_case = GetCountryName(MockCountryServiceUnexpectedError())
    with pytest.raises(Exception) as exc_info:
        await use_case.execute("us")
    assert "Unexpected error in use case" in str(exc_info.value)