import discord
import math
import random
from discord.ext import commands
import webbrowser

fortnite_URL = ""
Spotify_URL = ""
Nitro_URL = "" 
Minecraft_URL = ""
NordVPN_URL = ""
NetFlix_URL = ""
Origin_URL = ""
UPlay_URL = ""



TOKEN = 'NTI5MzM5NjQ0OTk1OTYwODQy.DwvZ-Q.fZEO5SlSC39mZINGaCfHRzwMHfc'
client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')
    await client.change_presence(status=discord.Status.online,
                activity=discord.Game("!rrhelp for helping commands"))
    

@client.command()
async def ping(ctx):
    await ctx.send("Ping Is {}".format(math.floor(client.latency * 1000)))

@client.command()
async def kick(ctx, member: discord.Member=None, *, reason=None):
    if member == None:
        await ctx.send("Need A Valid Member Darn It!")
    elif reason == None:
        await ctx.send("Need A Reason To Kick! member")
    elif ctx.author._roles is not "TheAngryRaptor":
        await ctx.send("We Can't Do Anything!")
    elif member._roles is "TheAngryRaptor":
        await client.channel.send("No Permission To Kick User")
    else:
        await member.kick(reason)

@client.command()
async def ban(ctx, member: discord.Member=None, *, reason=None):
    if member == None:
        await ctx.send("Need A Valid Member Darn It!")
    elif reason == None:
        await ctx.send("Need A Reason To Kick! member")
    elif ctx.author._roles is not "TheAngryRaptor":
        await ctx.send("We Can't Do Anything!")
    elif member._roles is "TheAngryRaptor":
        await client.channel.send("No Permission To Kick User")
    else:
        await member.ban(reason)

@client.command()
async def BotInfo(ctx):
    # Learn RichEmbed
        
    
    # Use RichEmbed


    
    pass

@client.command()
async def ServerInfo(ctx):
    # Learn RichEmbed
    # Use RichEmbed
    pass

@client.command()
async def addStock(ctx, Type, url):
    await ctx.send(Type)
    
    if (Type == 'fortnite'):
        await ctx.send("Done!")
        fortnite_URL = url
        
    if (Type == 'spotify'):
        await ctx.send("Done!")
        Spotify_URL = url
        
    if (Type == 'nitro'):
        await ctx.send("Done!")
        Nitro_URL = url
        
    if (Type == 'minecraft'):
        await ctx.send("Done!")
        Minecraft_URL = url
        
    if (Type == 'nordvpn'):
        await ctx.send("Done!")
        NordVPN_URL = url
        
    if (Type == 'netflix'):
        await ctx.send("Done!")
        NetFlix_URL = url

    if (Type == 'origin'):
        await ctx.send("Done!")
        Origin_URL = url

    if (Type == 'uplay'):
        await ctx.send("Done!")
        UPlay_URL = url
    pass
    
@client.command()
async def getAccount(ctx, Type : str):
    #await ctx.send(Type)
    
    if (Type == 'fortnite'):
        if fortnite_URL != "":
                #webbrowser.open_new_tab(fortnite_URL)
                # fortnite_URL read it using pastebin
                # Identfy The Row
                # Paste The Email:Password at requested target user DM
                pass
        elif fortnite_URL == "":
            await ctx.send("Account Is Not Stocked Yet! Try Again Later")
        
    if (Type == 'spotify'):
        if Spotify_URL != "":
                webbrowser.open_new_tab(Spotify_URL)
        elif Spotify_URL == "":
            await ctx.send("Account Is Not Stocked Yet! Try Again Later")
        
    if (Type == 'nitro'):
        if Nitro_URL != "":
            webbrowser.open_new_tab(Nitro_URL)
        elif Nitro_URL == "":
            await ctx.send("Account Is Not Stocked Yet! Try Again Later")
        
        
    if (Type == 'minecraft'):
        if Minecraft_URL != "":
            webbrowser.open_new_tab(Minecraft_URL)
        elif Minecraft_URL == "":
            await ctx.send("Account Is Not Stocked Yet! Try Again Later")
        
        
    if (Type == 'nordvpn'):
        if NordVPN_URL != "":
            webbrowser.open_new_tab(NordVPN_URL)
        elif NordVPN_URL == "":
            await ctx.send("Account Is Not Stocked Yet! Try Again Later")
        
    if (Type == 'netflix'):
        if NetFlix_URL != "":
            webbrowser.open_new_tab(NetFlix_URL)
        elif NetFlix_URL == "":
            await ctx.send("Account Is Not Stocked Yet! Try Again Later")

    if (Type == 'origin'):
         if Origin_URL != "":
            webbrowser.open_new_tab(Origin_URL)
         elif Origin_URL == "":
            await ctx.send("Account Is Not Stocked Yet! Try Again Later")

    if (Type == 'uplay'):
        if UPlay_URL != "":
            webbrowser.open_new_tab(UPlay_URL)
        elif UPlay_URL == "":
            await ctx.send("Account Is Not Stocked Yet! Try Again Later")

@client.command()
async def clearStock(ctx, Type : str):
    pass

client.run(TOKEN)
