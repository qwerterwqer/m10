import discord
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('                  '):
        await message.channel.send("\\U0001f642")
    else:
        await message.channel.send(message.content)
        
client.run("MTE2MzA1MTA1OTQ1NjAwNDE0OA.G7Ptjj.KUjv9OKkFaW-ouvdn4KK5a1cdhCWW_SkqIxFDg")



                          