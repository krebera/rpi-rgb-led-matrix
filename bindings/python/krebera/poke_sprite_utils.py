from os import listdir
from os.path import isfile, join
import aiohttp
import asyncio
import aiofiles
from im_utils import center_crop, alpha_comp
from PIL import Image, ImageDraw

from krebera.im_utils import ImagePreview

# ==================== LITTLE POKEMON SPRITES LOCAL ================ #
# Not internet api based. Just fetching them from file
def get_little_sprites_list(poke_list):
    icons = []

    filtered_pokes = list(filter(lambda poke: "-" not in poke, [f for f in listdir("./assets/pokesprites") if isfile(join("./assets/pokesprites", f))]))

    print(filtered_pokes)

    for team_member in poke_list:
        icon_path = next(filter(lambda poke: team_member in poke, filtered_pokes), None)
        icons.append(icon_path)

    return icons

def fetch_cleaned_poke_sprite_local(name, w, h):
    sprite_list = get_little_sprites_list([name])
    im = center_crop(Image.open('./assets/pokesprites/' + sprite_list[0] +'.png').convert('RGBA'), w, h)
    return alpha_comp(im)

def fetch_team_little_sprites_list(poke_list, w, h):
    icon_list = get_little_sprites_list(poke_list)
    imgs = []
    for icon in icon_list:
        imgs.append(fetch_cleaned_poke_sprite_local(icon, w, h))
    return imgs

def team_canvas(poke_list):
    bg = Image.new("RGB", (64, 64), (0, 0, 0))
    team_imgs = fetch_team_little_sprites_list(poke_list, 20, 20)
    bg.paste(team_imgs[0], (0,0))
    return bg

# ===================== POKE API V2 ================================ #
async def get_pokemon_data(name):
    async with aiohttp.ClientSession() as session:
        pokemon_url = f'https://pokeapi.co/api/v2/pokemon/' + name

        async with session.get(pokemon_url) as resp:
            pokemon_data = await resp.json()
            return pokemon_data

async def get_pokemon_sprite(pokemon_data):
    sprite_url = pokemon_data['sprites']['front_default']

    async with aiohttp.ClientSession() as session:
        async with session.get(sprite_url) as resp:
            if resp.status == 200:
                f = await aiofiles.open('./temp/pokemon.png', mode='wb')
                await f.write(await resp.read())
                await f.close()
            return

async def fetch_cleaned_poke_sprite_api(name, w, h):
    pokemon_data = await asyncio.create_task(get_pokemon_data(name))
    print(pokemon_data)
    await asyncio.create_task(get_pokemon_sprite(pokemon_data))
    im = center_crop(Image.open('./temp/pokemon.png').convert('RGBA'), w, h)
    return alpha_comp(im)

if __name__ == "__main__":
    my_team = ["pikachu", "bulbasaur", "squirtle", "charmander", "meowth", "lapras"]
    canvas = team_canvas(my_team)
    prev = ImagePreview()
    prev.set_im(canvas)
    prev.render()