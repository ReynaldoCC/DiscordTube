import json
import os
import urllib.request

from discord.ext import commands
from discord import Intents
from dotenv import load_dotenv

env = load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
TY_KEY = os.getenv('TY_KEY')

all_intents = Intents.all()

bot = commands.Bot(command_prefix='/', intents=all_intents)


def fetch_yt_data(url: str) -> dict:
    data = urllib.request.urlopen(url).read()
    return json.loads(data)


def get_channel_id(channel_name: str) -> str | None:
    url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&q={channel_name}&type=channel&key={TY_KEY}'
    data = fetch_yt_data(url)
    channel_id = data.get('items')[0].get('id', {}).get('channelId') if len(data.get('items', [])) > 0 else None
    return channel_id


def get_subscribers(channel_id: str) -> str | None:
    url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}&key={TY_KEY}'
    data = fetch_yt_data(url)
    subs = data.get('items')[0].get('statistics', {}).get('subscriberCount') if len(data.get('items', [])) > 0 else None
    return subs


@bot.command(name='subs')  # Funcion que mostrara los suscriptores de un canal de Youtube que le pasemos como parametro
async def subscriptores(ctx, username):
    channel_id = get_channel_id(username)
    if not channel_id:
        return await ctx.send(f'No channel with name {username}')
    subs = get_subscribers(channel_id)
    if not subs:
        return await ctx.send(f'No subscribers or data found for {username}')
    response = f'{username} tiene {int(subs):,d} suscriptores!'
    await ctx.send(response)


@bot.command(name='s')  # Funcion que realizara la suma entre dos numeros enteros
async def sum_nums(ctx, num1, num2):
    response = int(num1) + int(num2)
    await ctx.send(response)


@bot.command(name='m')  # Funcion que realizara la suma entre dos numeros enteros
async def multiplication(ctx, num1, num2):
    response = int(num1) * int(num2)
    await ctx.send(response)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bot.run(DISCORD_TOKEN)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
