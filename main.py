""" Slash Commando
Slash Commands Bot Using discordpy and discord-py-slash-command client """
import discord
import os
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

"""---------IMPORTS-----------"""

bot = commands.Bot(command_prefix="/",intents=discord.Intents.all())
slash = SlashCommand(bot,auto_register=True,auto_delete=True)

"""-----BOT & SLASH CLIENT-----"""

bot.remove_command("help")

@bot.event
async def on_ready():
	print(f'LOGGED IN AS:\nNAME : {bot.user.name}\nID : {bot.user.id}')

guild_ids = [727770350229782570]

@bot.command()
async def help(ctx):
	em = discord.Embed(title="Slashy-Commando",description="**Commands**\n• /slashy : some bot info\n• /ping : gives bot ping",color=discord.Color.green ())
	em.set_footer(text="All these commands are slash commands and are in beta (may not execute sometimes)")
	await ctx.send(embed=em)

@slash.slash(name="slashy",
description="Slash Commands Bot",
guild_ids=guild_ids)
async def slashy(ctx: SlashContext):
    embed = discord.Embed(title="SlashCommando",description="Slash Commands bot made by Ansh, this is so cool!",color=discord.Color.green())
    await ctx.send(embeds=[embed])
    
@slash.slash(name="ping",description="Gives Bot Latency",guild_ids=guild_ids)
async def ping(ctx: SlashContext):
	em = discord.Embed(title="Ping",description=f"Pong! {round(bot.latency*1000)}ms.",color=discord.Color.green())
	await ctx.send(embeds=[em])
	
"""---------COMMANDS---------"""

bot.run(os.getenv("TOKEN"))

"""----------START----------"""