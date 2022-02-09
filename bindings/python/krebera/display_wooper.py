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
    # pokemon_data = await asyncio.create_task(get_pokemon_data("wooper"))
    # print(pokemon_data)
    # await asyncio.create_task(get_pokemon_sprite(pokemon_data))
    im = Image.open('./temp/pokemon.png').convert('RGBA')
    w, h = im.size

    nw = 50
    nh = 50

    left = (w - nw)//2
    top = (h - nh)//2
    right = (w + nw)//2
    bottom = (h + nh)//2

    # Crop the center of the image
    im = im.crop((left, top, right, bottom))

    print(w)
    background = Image.new('RGBA', im.size, (0,0,0))
    alpha_composite = Image.alpha_composite(background, im).convert('RGB')
    alpha_composite.show()

asyncio.run(show_pokemon())