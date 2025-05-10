import pytest
import httpx
from unittest.mock import patch, Mock

from app.infrastructure.client.rest_country_client import RestCountryClient
from app.domain.exceptions.exceptions import CountryNotFoundException

@pytest.mark.asyncio
async def test_get_country_name_success():
    client = RestCountryClient(base_url="https://mock.api")

    mock_response = Mock()
    mock_response.raise_for_status.return_value = None  # No debería lanzar una excepción
    mock_response.json.return_value = [{"name": {"common": "Mockland"}}]  # Respuesta mock

    with patch("httpx.AsyncClient.get", return_value=mock_response):
        result = await client.get_country_name("xx")
        assert result == "Mockland"

@pytest.mark.asyncio
async def test_get_country_name_404_raises_custom_exception():
    client = RestCountryClient(base_url="https://mock.api")

    mock_response = Mock()
    mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
        "Not Found", request=Mock(), response=httpx.Response(404)
    )

    with patch("httpx.AsyncClient.get", return_value=mock_response):
        with pytest.raises(CountryNotFoundException) as exc_info:
            await client.get_country_name("zz")
        assert "country code 'zz' not found" in str(exc_info.value).lower()

@pytest.mark.asyncio
async def test_get_country_name_other_http_error_raises_runtime_error():
    client = RestCountryClient(base_url="https://mock.api")

    mock_response = Mock()
    mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
        "Internal Server Error", request=Mock(), response=httpx.Response(500)
    )

    with patch("httpx.AsyncClient.get", return_value=mock_response):
        with pytest.raises(RuntimeError) as exc_info:
            await client.get_country_name("error")
        assert "error fetching country data" in str(exc_info.value).lower()


@pytest.mark.asyncio
async def test_get_country_name_unexpected_exception_raises_runtime_error():
    client = RestCountryClient(base_url="https://mock.api")

    with patch("httpx.AsyncClient.get", side_effect=Exception("Unexpected")):
        with pytest.raises(RuntimeError) as exc_info:
            await client.get_country_name("oops")
        assert "unexpected error" in str(exc_info.value).lower()
