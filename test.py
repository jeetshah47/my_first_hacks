import discord
from discord.ext import commands

C = commands.Bot(command_prefix = ".")

@commands.command()
async def test(ctx):
   s = "https://google.com/"
   await ctx.send(s)

C.add_command(test)

@C.event
async def on_ready():
    print("Bot is ready.")

@C.event
async def on_member_join(member):
    print(f"{member} has joined the server")

@C.event
async def on_member_remove(member):
    print(f"{member} has left the server. Goodbyes")

C.run("NzU5NDk0MTU2OTI1NTM0Mjc4.X2-UDQ.gekAShyFSGn_XUgiJ1WzWrzSX0Y")