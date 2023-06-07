import discord
from discord.ext import commands
import responses

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} is now running!')

@bot.event
async def on_message(message):
    # Make sure bot doesn't get stuck in an infinite loop
    if message.author == bot.user:
        return

    # Get data about the user
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    # Debug printing
    print(f"{username} said: '{user_message}' ({channel})")

    # Check if user_message is not empty
    if user_message.strip().startswith('?'):
        user_message = user_message.strip()[1:]  # Remove '?' and leading/trailing spaces
        await send_message(message, user_message, is_private=True)
    else:
        await send_message(message, user_message, is_private=False)

# Send messages
async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)

        # Check if the response message is empty
        if not response:
            response = "Sorry, I couldn't generate a response."

        if response.startswith("http"):
            await message.channel.send(response)
        else:
            await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

# Remember to run your bot with your personal TOKEN
TOKEN = 'TOKEN'
bot.run(TOKEN)
