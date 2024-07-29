# import discord
# import os
# from dotenv import load_dotenv


# load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')


# class MyClient(discord.Client):

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#     async def on_ready(self):
#         print('Ready')



# client = MyClient()
# client.run(token = DISCORD_TOKEN)

import discord
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Define a subclass of discord.Client
class MyClient(discord.Client):

    def __init__(self, *args, **kwargs):
        intents = discord.Intents.default()  # Create an instance of Intents
        # You can enable specific events here
        intents.messages = True  # Enable message-related events
        super().__init__(intents=intents, *args, **kwargs)

    async def on_ready(self):
        print('Ready')

# Create an instance of MyClient and run it with the token
client = MyClient()
client.run(TOKEN)
