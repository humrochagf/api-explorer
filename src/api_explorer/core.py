import json
import logging
from pathlib import Path

from httpx import AsyncClient
from rich import print
from rich.logging import RichHandler

from api_explorer.config import settings

FORMAT = "%(message)s"
logging.basicConfig(
    level="DEBUG", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

DATA_FOLDER = Path(__file__).parent / "data"


async def search_images(client: AsyncClient) -> dict:
    response = await client.get(
        f"{settings.base_url}/images/search",
        params={"has_breeds": True},
    )

    return response.json()


async def get_breed(client: AsyncClient, breed_id: str) -> dict:
    response = await client.get(f"{settings.base_url}/breeds/{breed_id}")

    return response.json()


async def vote_from_file(client: AsyncClient) -> dict:
    with (Path(DATA_FOLDER) / "vote.json").open() as fp:
        data = json.load(fp)
        response = await client.post(f"{settings.base_url}/votes", json=data)

        return response.json()


async def main() -> None:
    headers = {
        "x-api-key": settings.auth_token,
    }

    async with AsyncClient(headers=headers) as client:
        cat = await search_images(client)
        print(cat)

        print(await get_breed(client, cat[0]["breeds"][0]["id"]))

        print(await vote_from_file(client))
