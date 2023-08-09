from nextcord.ext import commands
import nextcord
import os.path
import sys
from captcha.image import ImageCaptcha
from random_word import RandomWords
from classes import Captcha

def read_token():
    if not os.path.exists("token.in"):
        print("Bot requires token.in with a working token to function")
        sys.exit(1)
    with open("token.in") as f:
        return f.readline()


# the prefix is not used in this example
intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix='%',intents=intents)

TOKEN = read_token()
SERVER_ID = 1119954291831091221
MEM_ROLE_ID = 1138763673905664002

newly_joined = []

@bot.event
async def on_message(message):
    if not SERVER_ID is None:
        def findUser(author):
            for x in newly_joined:
                if author == x.user:
                    return x
            return None
        
        async def assignRole():
            server = None
            server = bot.get_guild(SERVER_ID)
            if server ==None:
                print("Server couldn't be found")
                return False
            
            role = server.get_role(MEM_ROLE_ID)
            if role == None:
                return False
            mem_id = server.get_member(message.author.id)
            await mem_id.add_roles(role)
        user = findUser(message.author)
        if not user is None:
            print(user.word)
            if not user.verify_captcha(message.content):
                return await message.author.send("Please try again")

            if not await assignRole():
                return False

    print(f'Message from {message.author}: {message.content}')

    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    print(SERVER_ID)
    r=RandomWords()

    word = r.get_random_word()

    image = ImageCaptcha(width = 500, height = 100)

    image.generate_image(word)
    count = 0
    while os.path.exists(f"./tmp/{word}{'' if count ==0 else count}.png"):
        count +=1
    f_name = f"./tmp/{word}{count}.png"
    image.write(word, f_name)
    await member.send(file=nextcord.File(f_name))
    newly_joined.append(Captcha(image,member,word))


if __name__ == "__main__":
    if not os.path.exists("./tmp"):
        os.makedirs("tmp")
    bot.run(TOKEN)
