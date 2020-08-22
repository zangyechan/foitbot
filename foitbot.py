import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")



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

client.run("NzQ1OTA2NjUxMzk5MzIzNjg5.Xz4lsw.2FCr05GM-RuCAQZA2T2Lcp_E1UE")