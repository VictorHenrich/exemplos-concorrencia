from requests import get, Response
from pathlib import Path
from typing import Mapping, Any
from .constantes import LIMIT_POKEMONS, PATH_IMAGES





def download_image(pokemon_name: str, image_url: str) -> None:
    response: Response = get(image_url)

    file_path: Path = PATH_IMAGES / f"{pokemon_name}.png"

    with open(str(file_path), mode="wb") as file:
        file.write(response.content)


def handle_pokemon(pokemon_name: str, pokemon_url: str) -> None:
    response: Response = get(pokemon_url)

    data: Mapping[str, Any] = response.json()

    image_url: str = data['sprites']['back_default']

    download_image(pokemon_name, image_url)


def get_pokemons() -> list[Mapping[str, Any]]:
    url: str = f"https://pokeapi.co/api/v2/pokemon?limit={LIMIT_POKEMONS}"

    response: Response = get(url)

    data: Mapping[str, Any] = response.json()

    return data['results']


def create_path_pokemons() -> None:
    if not PATH_IMAGES.exists():
        PATH_IMAGES.mkdir()