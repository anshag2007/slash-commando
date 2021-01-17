import discord
import os
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())
slash = SlashCommand(bot,auto_register=True,auto_delete=True)

@bot.event
async def on_ready():
	print('🖒')

guild_ids = [727770350229782570]

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

bot.run(os.getenv("TOKEN"))