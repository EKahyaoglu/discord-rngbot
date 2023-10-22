# Rutgers-Newark Gaming Discord Bot
# Created June 16, 2023
# Author: Eren Kahyaoglu

# bot.py

import discord
from discord import app_commands
from discord.ext import commands
import responses

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('We are now running!')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.command(name="hello")
async def hello(ctx):
    await ctx.send(f"Hey {ctx.author.mention}!!!!")

@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
   await interaction.response.send_message(f"Hey {interaction.user.mention}!") 
   ephemeral=True

@bot.command(name="say")
async def say(ctx, *, thing_to_say: str):
    await ctx.send(f"Hey {ctx.author.name} said: '{thing_to_say}'")

@bot.tree.command(name="say")
@app_commands.describe(thing_to_say = "What should I say?")
async def say(interaction: discord.Interaction, thing_to_say: str):
   await interaction.response.send_message(f"Hey {interaction.user.name} said: '{thing_to_say}'")

@bot.event
async def on_message(message):
  if message.channel.type == discord.ChannelType.private:
    reply_to = 202892883475300354
    await interaction.response.send_message(message.channel, "This is a reply to your message.")

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

def run_discord_bot():
    TOKEN = "BOT_TOKEN"
    bot.run(TOKEN)

run_discord_bot()