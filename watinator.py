import discord, asyncio, threading, math, random
from threading import Timer
from discord.ext import commands, tasks
intents = discord.Intents.default()
intents.members = True 

bot = commands.Bot(command_prefix = '/')
client = discord.Client()

timestarted = False
counter = 0

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    global timestarted
    global counter
    words = len(message.content.split())
    if message.author == bot.user:
        return
    if words > 200:
        await asyncio.sleep(15)
        await message.channel.send('Thank you for coming to my TED talk')
    elif timestarted == False:
        counter = 0
        timestopause = 3
        timetowat = 3600
        while counter < timetowat:
            timestarted = True
            await asyncio.sleep(1)
            if (counter != 0) and ((counter % math.ceil(timetowat / (timestopause+1))) == 0):
                await message.channel.send('...')
            counter += 1
        await message.channel.send('WAT')
        timestarted = False
    else:
        counter = 0

    await bot.process_commands(message)
    return

@bot.event
async def on_reaction_add(reaction, user):
    with open('.\ejikeisms.txt') as file:
        ejikeisms = file.readlines()
        ejikeisms = [x.strip() for x in ejikeisms]

    with open('.\emojil.txt') as file:
        emojil = file.readlines()
        emojil = [x.strip() for x in emojil]
    try:    
        if reaction.emoji.name in emojil:
            choice = random.randrange(0, (len(ejikeisms)+1), 1)
            await reaction.message.channel.send("Ejike: %s" % ejikeisms[choice])
    except:
        print("Error on Emoji Name")

#Production
bot.run('NzY0Mjg0NzM0NzY2OTcyOTM4.X4EBoA.o5U5MfUC-kdK5gr4DlTGz_XyWCY')

#Test
#bot.run('NzY1MzM5NDUwNzc0NjUwODgx.X4TX6A.F5hSNUAcWkpK3eKOKIC043xFB6E')