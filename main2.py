from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents,Client,Message
from responses import get_response

#step 0:LOAD OUR TOKEN FROM SOMEWHERE SAFE
load_dotenv()
TOKEN:Final[str] = os.getenv('DISCORD_TOKEN')
CHANNEL_ID: Final[int] = int(os.getenv('DISCORD_CHANNEL_ID'))
print(TOKEN)


#step 1:BOT SETUP
intents:Intents = Intents.default()
intents.message_content = True
client:Client = Client(intents=intents)

#step 2: message Functionality

async def send_message(message:Message, user_message:str)->None:
    if not user_message:
        print("Message was empty")
        return
    is_private = user_message[0] =='?'
    if is_private:
        user_message = user_message[1:]

    try:
        response:str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

#step 3:handling the startup for our bot
@client.event
async def on_ready() -> None:
    print(f"{client.user} is now online!")
    channel = client.get_channel(CHANNEL_ID)
    if channel is not None:
        await channel.send("Bot is Online!")
    else:
        print("Failed to get channel")

#step 6:when message is edited
@client.event
async def on_message_edit(before,after):
    await before.channel.send(f'{before.author} edit a message.\n'
                              f'Before: {before.content}\n'
                              f'After: {after.content}'
                              )
    return

#step 4: handling incoming messages
@client.event
async def on_message(message:Message)->None:
    if message.author == client.user:
        return
    username: str = str(message.author)
    user_message:str = message.content
    channel:str = str(message.channel)
    print(f"[{channel}] {username}: '{user_message}'")
    if user_message.lower() == 'happy':
        await message.add_reaction('\U0001F600')
        return
    await send_message(message,user_message)

#step 5:main entry point
def main() -> None:
    client.run(token=TOKEN)



if __name__ == "__main__":
    main()