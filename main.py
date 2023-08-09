from nextcord.ext import commands
import nextcord
import os.path
import sys

def read_token():
    if not os.path.exists("token.in"):
        print("Bot requires token.in with a working token to function")
        sys.exit(1)
    with open("token.in") as f:
        return f.readline()


# the prefix is not used in this example
intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix='$',intents=intents)

TOKEN = read_token()

@bot.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')


if __name__ == "__main__":
    bot.run(TOKEN)