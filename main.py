""" Slash Commando
Slash Commands Bot Using discordpy and discord-py-slash-command client """
import discord
import os
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils import manage_commands

"""---------IMPORTS-----------"""

bot = commands.Bot(command_prefix="/",intents=discord.Intents.all())
slash = SlashCommand(bot,auto_register=True,auto_delete=True)

"""-----BOT & SLASH CLIENT-----"""

bot.remove_command("help")

@bot.event
async def on_ready():
	print(f'LOGGED IN AS:\nNAME : {bot.user.name}\nID : {bot.user.id}')

guild_ids = [727770350229782570,793226316862062593]
# SERVER IDS (THE SERVERS IN WHICH THE BOT IS ADDED)

@bot.command()
async def help(ctx):
	em = discord.Embed(title="Slash-Commando",description="**Commands**\n• /slashy : some bot info\n• /ping : gives bot ping",color=discord.Color.green ())
	em.set_footer(text="All these commands are slash commands and are in beta (may not execute sometimes)")
	await ctx.send(embed=em)

@slash.slash(name="slash",
description="Some info about SlashCommmando.",
guild_ids=guild_ids)
async def _slash(ctx: SlashContext):
    embed = discord.Embed(title="SlashCommando",description="Slash Commands bot made by Ansh, this is a open-source bot which uses `discord.py` and `discord-py-slash-command` client to execute slash commands.\n\n**Bot Repository**\nYes! Its posted on Github and updates almost everyday.\n[AnshAg2007/slash-commando](https://github.com/AnshAg2007/slash-commando)\n\n**Bot Repl**\nThis bot is being developed and hosted on repl.it and the repl is also public.\n[@AnshAg2007/slash-commando](https://repl.it/@AnshAg2007/slash-commando)\n_ _",color=discord.Color.green())
    embed.set_footer(text="Discord Slash Commands are in beta, commands may not execute sometimes")
    await ctx.send(embeds=[embed])
    
@slash.slash(name="ping",description="Get bot latency.",guild_ids=guild_ids)
async def ping(ctx: SlashContext):
	em = discord.Embed(title="Ping",description=f"Pong! {round(bot.latency*1000)}ms.",color=discord.Color.green())
	await ctx.send(embeds=[em])
	
@slash.slash(name="echo",description="Echoes what you say.",options=[manage_commands.create_option("content","the content you want to be echoed.",3,True)],guild_ids=guild_ids)
async def echo(ctx:SlashContext,msg:SlashContext):
	em = discord.Embed(description=f"{msg}",color=discord.Color.green())
	await ctx.send(embeds=[em])
	
@slash.slash(name="embed",description="Makes a custom embed.",options=[manage_commands.create_option("title","the embed title.",3,True),manage_commands.create_option("description","the embed description.",3,True),manage_commands.create_option("color","the embed color(hex).",3,True),manage_commands.create_option("footer","the embed footer.",3,True)],guild_ids=guild_ids)
async def embed(ctx:SlashContext,title,description,color,footer):
	embed = discord.Embed(title=f"{title}",description=f"{description}",color=int(color))
	embed.set_footer(text=footer)
	await ctx.send(embeds=[embed])
	
@slash.slash(name="color",description="Change color of someone's pfp to the color you wish.",options=[manage_commands.create_option("member","the person you wanna colorize.",3,False),manage_commands.create_option("color","the color(hex).",3,True)],guild_ids=guild_ids)
async def _color(ctx:SlashContext,member:discord.Member=None,color):
	if member == None:
		member = ctx.author
		em = discord.Embed(color=discord.Color.black())
		em.set_image(url=f"https://some-random-api.ml/canvas/color?avatar={member.avatar_url()}&color=%23{color}")
		await ctx.send(embeds=[em])
	else:
		em = discord.Embed(color=discord.Color.black())
		em.set_image(url=f"https://some-random-api.ml/canvas/color?avatar={member.avatar_url()}&color=%23{color}")
		await ctx.send(embeds=[em])
		
		


"""---------COMMANDS---------"""

bot.run(os.getenv("TOKEN"))

"""----------START----------"""