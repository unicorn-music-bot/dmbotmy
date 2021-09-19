import json

from discord.ext import commands

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print(' [!] Started Dmming Ids\n')

    with open("ids.json", "r") as file:
        data = json.load(file)

    indx = 0
    for i in data:
        indx += 1
        member = await bot.fetch_user(i)
        try:
            await member.send("Pixelverse is a fast-paced strategy blockchain-based game with the goal to become the most exciting metaverse gamers have seen with unique planet art. With Player vs Player (PVP) concept, most matches will complete fast. It combines concepts that have already been tested with a unique twist, Pixelverse brings a new experience to the blockchain gaming industry.                                                                                                                                            Fight for your side! Time to save the UNIVERSE!                                                                                                         There can only be PIXELVERSE!                                                                                                                                        Join our Discord for Giveaways (*Bonus when Discord hits 10K members)                                                         Discord: https://discord.gg/264ySUSK76 Check our Twitter here:     https://mobile.twitter.com/pixelverse2777")
            print(f" [+] Sent message {indx} / {len(data)}")
        except Exception as e:
            print(f" [!] {e}")

    print(" [+] Done")

bot.run("ODg5MDcxMTk0ODQ5MDE3ODg2.YUb6Eg.FqMPrc30XYGuIhIgW9y4Qv4iH58", bot = True)
