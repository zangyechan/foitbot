import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("포잇봇")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startwith("안녕")
        await channel.send("안녕 난 포잇봇이야 흫")
    if message.content.startwith("흫")
            await channel.send("흐흫")
    if message.content.startwith("바이")
        await channel.send("잘가")
    if message.content.startwith("이름 뜻")
        await channel.send("foit4한테 물어보세오")
        
acess_token = os.envion["BOT_TOKEN"]
client.run("acess_token")
