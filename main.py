import discord
import colorama as *
import threading
 
client = discord.Client()
colorama.init()
 
token = input("What is your discord token [-->]: ")
Message = input("What Do You Want To Mass DM [-->]: ")
thread_amount = int(input("How Many Threads [-->]: "))
used_threads = thread_amount * 100000
 
@client.event
async def on_connect():
    for user in client.user.friends:
        try:
            await user.send(Message)
            print(Fore.GREEN)
            print(f"message: {user.name}")
        except:
            print(Fore.RED)
            print(f"unable to message: {user.name}")
def run():
    client.run("YOUR TOKEN HERE", bot=False)
 
threads = []
 
for i in range(thread_amount):
    t = threading.Thread(target=run())
    t.daemon = False
    threads.append(t)
 
for i in range(thread_amount):
    threads[i].start()
 
for i in range(thread_amount):
    threads[i].join()
