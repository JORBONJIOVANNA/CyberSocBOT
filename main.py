from nextcord.ext import commands
import nextcord
import os.path
import sys
from captcha.image import ImageCaptcha
from random_word import RandomWords
import re
import random
from classes import Captcha, Rule

def read_token():
    if not os.path.exists("token.in"):
        print("Bot requires token.in with a working token to function")
        sys.exit(1)
    with open("token.in") as f:
        return f.readline()

def read_rules()->list:
    ret_ls = []
    with open("rules.in") as f:
        for x in f.readlines():
            ret_ls.append(Rule(x))

    return ret_ls

rules = read_rules()

# the prefix is not used in this example
intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix='%',intents=intents)

TOKEN = read_token()
SERVER_ID = 1119954291831091221
MEM_ROLE_ID = 1138763673905664002
RULES_CHANNEL_ID = 1164856076685025390
UNVERIFIED_ROLE_ID=1203637624338911233

newly_joined = []

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def create_rules(ctx):
    if not SERVER_ID is None:
        server = bot.get_guild(SERVER_ID)
        for x in rules:
            colour = x.hex_to_rgb()
            embed = nextcord.Embed(colour=nextcord.Colour.from_rgb(colour[0],colour[1],colour[2]),
                                description=x.msg,
                                title=x.title)
            await server.get_channel(RULES_CHANNEL_ID).send(embed=embed)


@bot.event
async def on_message(message):

    await bot.process_commands(message)


@bot.event
async def on_member_join(member:nextcord.Member):
    member.add_roles(bot.get_guild(SERVER_ID).get_role(UNVERIFIED_ROLE_ID))


if __name__ == "__main__":
    if not os.path.exists("./tmp"):
        os.makedirs("tmp")
    bot.run(TOKEN)
