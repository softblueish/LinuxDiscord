# bot.py
import os
import subprocess

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv('token.env')
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')

@bot.command(name='bash')
async def bash(ctx, command):
    
    rawstring = str(subprocess.check_output(command, shell=True)).split('\\n')
    for i in range(len(rawstring)):
        await ctx.send(f"```{rawstring[i]}```")

bot.run(TOKEN)
