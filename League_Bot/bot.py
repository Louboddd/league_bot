import os
import discord
from discord.ext import commands 
from dotenv import load_dotenv
from champs import top_lane, jungle_lane, mid_lane, adc_lane, support_lane
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    
    if "test" in message.content.lower():
        await message.channel.send("test complete")
        
    if message.content.startswith("!top"):
        await message.channel.send(f"Your Top Laner is: {get_top()}")
    
    if message.content.startswith("!jungle"):
        await message.channel.send(f"Your Jungler is: {get_jungle()}")
        
    if message.content.startswith("!mid"):
        await message.channel.send(f"Your Mid Laner is: {get_mid()}")
        
    if message.content.startswith("!adc"):
        await message.channel.send(f"Your ADC is: {get_adc()}") 
        
    if message.content.startswith("!support"):
        await message.channel.send(f"Your Support is: {get_support()}")         
 
    if message.content.startswith("!all"):
        await message.channel.send(f"Your Top Laner is: {get_top()}")
        await message.channel.send(f"Your Jungler is: {get_jungle()}")
        await message.channel.send(f"Your Mid Laner is: {get_mid()}")
        await message.channel.send(f"Your ADC is: {get_adc()}")
        await message.channel.send(f"Your Support is: {get_support()}")
        
    if message.content.startswith("!tip"):
        await message.channel.send("Remember its D to dance!")
       
    await bot.process_commands(message)

def get_top():
    random_top = random.choice(top_lane)
    return random_top

def get_jungle():
    random_jungle = random.choice(jungle_lane)
    return random_jungle

def get_mid():
    random_mid = random.choice(mid_lane)
    return random_mid

def get_adc():
    random_adc = random.choice(adc_lane)
    return random_adc

def get_support():
    random_support = random.choice(support_lane)
    return random_support

client.run(TOKEN)