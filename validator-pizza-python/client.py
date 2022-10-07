import aiohttp
import requests
from .models.domain_status import DomainStatus


class AioPizzaValidator:
    def __init__(self, session=None):
        """
        Asynchronous Pizza Validator client.
        """
        self.session = session or aiohttp.ClientSession()

    async def close(self):
        """
        Close the session.
        """
        await self.session.close()

    async def validate(self, domain: str) -> DomainStatus:
        """
        Validate email.
        Return a DomainStatus object.
        """

        response = await self.session.get(f"https://api.mailcheck.ai/domain/{domain}")
        if response.status != 200:
            raise Exception(
                f'Error: {response.status} - Fail to validate domain.')

        data = await response.json()
        return DomainStatus(**data)

    async def is_disposable(self, domain: str) -> bool:
        """
        Validate domain.
        Return a boolean.
        """

        email_status = await self.validate(domain)
        return email_status.disposable


class PizzaValidator:
    @staticmethod
    def validate(domain: str) -> DomainStatus:
        """
        Validate email.
        Return a DomainStatus object.
        """

        response = requests.get(f'https://api.mailcheck.ai/domain/{domain}')
        if response.status_code != 200:
            raise Exception(
                f'Error: {response.status} - Fail to validate domain.')

        data = response.json()
        return DomainStatus(**data)

    @staticmethod
    def is_disposable(domain: str) -> bool:
        """
        Validate domain.
        Return a boolean.
        """

        email_status = PizzaValidator.validate(domain)
        return email_status.disposable
