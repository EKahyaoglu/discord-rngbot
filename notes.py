# notes.py

import discord
from discord import app_commands
from discord.ext import commands
import responses

bot = commands.Bot(command_prefix="*", intents = discord.Intents.all())

async def send_message(message, user_message, is_private):
   try:
      response = responses.handle_response(user_message)
      await message.author.send(response) if is_private else await message.channel.send(response)
   except Exception as e:
      print(e)

def run_discord_bot():
   TOKEN = "BOT_TOKEN"
   intents = discord.Intents.default()
   intents.message_content = True
   client = discord.Client(intents=intents)

   @bot.command(name="hello")
   async def hello(ctx):
       await ctx.send(f"Hey {ctx.author.mention}!")
   
   bot.tree.command(name="hello")
   async def hello(interaction: discord.Interaction):
      await interaction.response.send_message(f"Hey {interaction.user.mention}!") 
      ephemeral=True
   
   @bot.command(name="say")
   async def say(ctx, *, thing_to_say: str):
       await ctx.send(f"Hey {ctx.author.name} said: '{thing_to_say}'")
   
   bot.tree.command(name="say")
   app_commands.describe(thing_to_say = "What should I say?")
   async def say(interaction: discord.Interaction, thing_to_say: str):
      await interaction.response.send_message(f"Hey {interaction.user.name} said: '{thing_to_say}'")
    
   @bot.event
   async def on_message(message):
       if message.author == bot.user:
           return
   
       try:
           response = responses.handle_response(message.content)
           await message.author.send(response)
       except Exception as e:
           print(e)
   
       await bot.process_commands(message)
   
   @bot.event
   async def on_ready():
       print('We are now running!')
       try:
           synced = await bot.tree.sync()
           print(f"Synced {len(synced)} command(s)")
       except Exception as e:
           print(e)
   
       await send_message(message, message.content, False)  # Assuming it's not a private message
   
   def run_discord_bot():
       TOKEN = "BOT_TOKEN"
       bot.run(TOKEN)
       
       
       
   @bot.command(name="hello")
async def hello(ctx):
    await ctx.send(f"Hey {ctx.author.mention}!")    
    

@bot.command(name="say")
async def say(ctx, *, thing_to_say: str):
    await ctx.send(f"Hey {ctx.author.name} said: '{thing_to_say}'")
       
       
       async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        if is_private:
            await message.author.send(response)
        else:
            await message.channel.send(response)
    except Exception as e:
        print(e)
       
       