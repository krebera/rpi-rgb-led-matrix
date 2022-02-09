import aiohttp
import asyncio
import aiofiles
from PIL import Image

async def get_pokemon_data(name):
    async with aiohttp.ClientSession() as session:
        pokemon_url = f'https://pokeapi.co/api/v2/pokemon/wooper'

        async with session.get(pokemon_url) as resp:
            pokemon_data = await resp.json()
            print("Got pokemon data")
            return pokemon_data

async def get_pokemon_sprite(pokemon_data):
    sprite_url = pokemon_data['sprites']['front_default']

    async with aiohttp.ClientSession() as session:
        async with session.get(sprite_url) as resp:
            if resp.status == 200:
                f = await aiofiles.open('./temp/pokemon.png', mode='wb')
                await f.write(await resp.read())
                await f.close()
                print("Got pokemon sprite")
            return

async def show_pokemon():
    pokemon_data = await asyncio.create_task(get_pokemon_data("wooper"))
    # print(pokemon_data)
    await asyncio.create_task(get_pokemon_sprite(pokemon_data))
    # im = Image.open('./temp/pokemon.png')
    # im.show()

asyncio.run(show_pokemon())