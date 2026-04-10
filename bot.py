import os
import string
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
CHANNEL_ID = 1491948321038929970  # Change this to your channel ID

PIRATE_WORDS = [
    "ahoy", "arggh", "argh", "arghh", "arghhh", "arghhhh", "avast", "aye",
    "belay", "bilge", "blimey", "booty", "buccaneer", "cap’n", "captain",
    "corsair", "cutlass", "doubloon", "galleon", "grog", "hardtack", "heave ho",
    "hoist", "keelhaul", "landlubber", 'lanyard', 'lookout', 'loot', 'marooned',
    'matey', 'mizzenmast', 'plunder', 'poop deck', 'quarterdeck', "rigging",
    "scallywag", "schooner", "scurvy", "shanty", "shipshape", "shiver me timbers",
    "splice the mainbrace", "swab", "swashbuckler", "three sheets to the wind",
    "tis", "treasure", "walk the plank", "yardarm", "yargh", "yo-ho", 'yo-ho-ho', 'yoho'
]

RESTRICTED_PUNCTUATION = set(string.punctuation) - set("-'’")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("argh im running now")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.channel.id == CHANNEL_ID:
        lowercase = message.content.lower() == message.content
        has_punctuation = any(char in RESTRICTED_PUNCTUATION for char in message.content)
        pirate = any(word in message.content for word in PIRATE_WORDS)

        if has_punctuation or not pirate or not lowercase:
            try:
                await message.delete()
            except discord.Forbidden:
                print("I don't have the 'Manage Messages' permission in this channel")
            except discord.HTTPException as e:
                print(f"Failed to delete a message: {e}")
        else:
            try:
                await message.add_reaction("🏴‍☠️")
            except Exception as e:
                print(f"Failed to add reaction: {e}")

if __name__ == "__main__":
    if not TOKEN:
        print("No token found, make sure your env file is set up properly.")
    else:
        client.run(TOKEN)
