from abc import ABC, abstractmethod

class CountryService(ABC):
    @abstractmethod
    async def get_country_name(self, code: str) -> str:
        pass