import discord
client = discord.Client()
import colorama
from colorama import Fore, Back, Style
colorama.init()

Message = input("What would you like to Mass DM? [==>]: ")

@client.event
async def on_connect():
    for user in client.user.friends:
        try:
            await user.send(message)
            Fore.GREEN
            print(f"message: {user.name}")
        except:
            Fore.RED
            print(f"couldnt message: {user.name}")

client.run("YOUR DISCORD TOKEN HERE", bot=False)
