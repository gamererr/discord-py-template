import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
	print("hello world!")

with open("tokenfile", "r") as tokenfile:
		token=tokenfile.read()

# VVVVVV commands VVVVVV'

@client.command()
async def test(ctx):
	await ctx.send("test")

client.run(token)