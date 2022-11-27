#!/usr/bin/python3
import os, subprocess, rules
from discord.ext import commands
import discord

TOKEN = ''
intents = discord.Intents.default();
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix='$', description='Run a shell command')

@bot.command(name='bash')
async def bash(ctx, command):
    for i in range(len(rules.BLACKLIST_COMMANDS)):
        if command == rules.BLACKLIST_COMMANDS[i]:
            await ctx.send(rules.BLST_ERROR)
            print(f"Blacklisted Command Attempted: {command}")
            return

    rawstring = str(subprocess.check_output(command, shell=True), 'utf8').split('\n')
    print(f"Command Used: {command}")
    for i in range(len(rawstring)):
        await ctx.send(f"``{rawstring[i]} ``")

bot.run(TOKEN)
