import discord
from discord.ext import commands
import g4f

intents = discord.Intents.default()
intents.messages = True  # Enable message-related intents

bot = commands.Bot(command_prefix='!', intents=intents)

# Initialize the AI model or any other setup required here

history = []

def ChatGpt(*args):
    global history
    messages = [
    {
        "role": "system",
        "content": "I am Abhay?"
    }

    ]
    
    assert args != ()

    message = ""
    for i in args:
        message += i

    # Add the new message to the history
    history.append({"role": "user", "content": message})

    # If the history is too long, remove the oldest message
    if len(history) > 10:
        history.pop(0)

    # Use the history in the response
    response = g4f.ChatCompletion.create(
        model="gpt-4-32k-0613",
        provider=g4f.Provider.GPTalk,
        messages=history,
        stream=True,
    )
    ms = ""
    for message in response:
        ms += message
    return ms

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    response = ChatGpt(message.content)
    await message.channel.send(response)

    await bot.process_commands(message)

bot.run('MTE0NDExMjMxNTkwNjY2MjQ2Mg.GcGt7L.n09BCaDFQYDBPw5i59lvO1ZDS61Pg4HqlQhM88')
