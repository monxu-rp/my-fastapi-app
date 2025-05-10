from fastapi import APIRouter, Depends
from fastapi import Path
from fastapi import HTTPException
from typing import Dict

from app.domain.exceptions.exceptions import CountryNotFoundException
from app.domain.ports.country_service import CountryService
from app.domain.use_cases.get_country_name import GetCountryName
from app.infrastructure.client.rest_country_client import RestCountryClient
from pydantic import BaseModel

class CountryResponse(BaseModel):
    country: str

router = APIRouter()

def get_country_service() -> CountryService:
    return RestCountryClient()

@router.get("/country/{code}", response_model=CountryResponse)
async def get_country_name(
        code: str = Path(..., pattern="^[a-zA-Z]{2,3}$"),
        country_service: CountryService = Depends(get_country_service)
) -> CountryResponse:
    use_case = GetCountryName(country_service)
    try:
        country_name = await use_case.execute(code)
        return CountryResponse(country=country_name)
    except CountryNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")