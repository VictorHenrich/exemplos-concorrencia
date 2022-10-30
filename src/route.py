from typing import Any, Mapping
import json
from threading import Thread

from utils import handle_pokemon, get_pokemons, Timer, create_path_pokemons
from app import app



@app.get('/dowload_pokemons/com_thread')
def download_pokemons_v1():
    with Timer() as timer:
        pokemons: list[Mapping[str, Any]] = get_pokemons()

        create_path_pokemons()

        threads: list[Thread] = [
            Thread(target=handle_pokemon, args=(item['name'], item['url']))
            for item in pokemons
        ]

        [thread.start() for thread in threads]
        [thread.join() for thread in threads]

        return json.dumps({"message": "OK"})



@app.get('/dowload_pokemons/sem_thread')
def download_pokemons_v2():
    with Timer() as timer:
        pokemons: list[Mapping[str, Any]] = get_pokemons()

        create_path_pokemons()

        [
            handle_pokemon(item['name'], item['url'])
            for item in pokemons
        ]

        return json.dumps({"message": "OK"})