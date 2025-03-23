# Example 65 - Request API data

import requests

base_url = "https://pokeapi.co/api/v2"


def get_pokemon_data(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    data = None

    if response.status_code == 200:
        data = response.json()
    else:
        print("Pokemon was not found")

    return data


pokemon_info = get_pokemon_data("Shadow the Hedgehog")

if pokemon_info:
    print(f"Name: {pokemon_info["name"].capitalize()}")
    print(f"Id: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")
