from captcha.image import ImageCaptcha
from random_word import RandomWords
import nextcord
from classes import Captcha, Rule


async def captcha(member,newly_joined):
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


async def on_message_captcha(SERVER_ID, newly_joined,MEM_ROLE_ID,message):
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