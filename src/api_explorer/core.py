import logging

from httpx import AsyncClient
from rich import print
from rich.logging import RichHandler

from api_explorer.config import settings

FORMAT = "%(message)s"
logging.basicConfig(
    level="DEBUG", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)


async def search_images(client: AsyncClient) -> dict:
    response = await client.get(f"{settings.base_url}/images/search")

    return response.json()


async def main() -> None:
    async with AsyncClient() as client:
        print(await search_images(client))
