import discord
import chatter

client = discord.Client()
f = { }
slurs =  [ ]
prefix = [ ]

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    text = message.content
    if not str(message.guild.id) in f:
        f[str(message.guild.id)] = chatter.Chatter(str(message.guild.id))
    if message.author == client.user:
        return
    elif text == ";help":
        await message.channel.send("Hi I'm SpiceBot! I'm a great listener, but I'm a little shy. If you keep talking I'll learn to come out of my shell! If you type \";\", I'll try my best to speak. If you want me to meantion a certain word or phrase, just use \";YourPhraseHere\" and I'll try my best to use it if it's been recorded.")
    elif text.startswith(";"):
        try:
            await message.channel.send(f[str(message.guild.id)].respond(text.strip(";")))
        except IndexError:
            await message.channel.send("Woah woah, slow down! Nothing has been said since I entered. I only record messages as they are sent, so if none have been recorded I'll have nothing to say! Type \";help\" for more info.")
    else:
        for word in slurs:
            if word in text.lower():
                return
        for string in prefix:
            if text.startswith(string):
                return
        print(text)
        if "@here" in text or "@everyone" in text or "<@!" in text:
            print("Group mentioned, omitting...")
            return
        f[str(message.guild.id)].learn(text)

try:
    client.run("") # put your bot's token in the string here
except:
    print("Login unsuccessful...")
finally:
    for inst in f:
        f[inst].close()
