import discord
from discord.ext import commands
from discord.ui import Button, View
import os
from typing import Optional

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_USERNAME', 'your_instagram')
TELEGRAM_USERNAME = os.getenv('TELEGRAM_USERNAME', 'your_telegram')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'Bot is in {len(bot.guilds)} guilds')
    await bot.change_presence(
        activity=discord.Game(name="Type !help for commands | !profile")
    )

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

@bot.command(name='profile', help='View Mahdi\'s profile with social media links')
async def profile(ctx):
    embed = discord.Embed(
        title="👤 Mahdi's Profile",
        description="You're viewing Mahdi's profile! Connect with me on social media:",
        color=discord.Color.purple()
    )
    
    embed.add_field(
        name="📱 Social Media",
        value="Click the buttons below to connect with me on Instagram and Telegram!",
        inline=False
    )
    
    embed.set_footer(text="Thanks for checking out my profile! 💜")
    
    view = View()
    
    instagram_button = Button(
        label="Instagram",
        style=discord.ButtonStyle.link,
        url=f"https://instagram.com/{INSTAGRAM_USERNAME}",
        emoji="📷"
    )
    
    telegram_button = Button(
        label="Telegram",
        style=discord.ButtonStyle.link,
        url=f"https://t.me/{TELEGRAM_USERNAME}",
        emoji="✈️"
    )
    
    view.add_item(instagram_button)
    view.add_item(telegram_button)
    
    await ctx.send(embed=embed, view=view)

@bot.command(name='hello', help='Says hello!')
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}! 👋')

@bot.command(name='ping', help='Check bot latency')
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f'🏓 Pong! Latency: {latency}ms')

@bot.command(name='serverinfo', help='Get server information')
async def serverinfo(ctx):
    guild = ctx.guild
    
    embed = discord.Embed(
        title=f"{guild.name} Server Information",
        color=discord.Color.blue()
    )
    embed.add_field(name="Server ID", value=guild.id, inline=False)
    embed.add_field(name="Owner", value=guild.owner.mention, inline=False)
    embed.add_field(name="Members", value=guild.member_count, inline=True)
    embed.add_field(name="Channels", value=len(guild.channels), inline=True)
    embed.add_field(name="Roles", value=len(guild.roles), inline=True)
    embed.add_field(name="Created At", value=guild.created_at.strftime("%Y-%m-%d"), inline=False)
    
    if guild.icon:
        embed.set_thumbnail(url=guild.icon.url)
    
    await ctx.send(embed=embed)

@bot.command(name='userinfo', help='Get user information')
async def userinfo(ctx, member: Optional[discord.Member] = None):
    member = member or ctx.author
    
    embed = discord.Embed(
        title=f"{member.name}'s Information",
        color=member.color
    )
    embed.set_thumbnail(url=member.display_avatar.url)
    embed.add_field(name="Username", value=member.name, inline=False)
    embed.add_field(name="ID", value=member.id, inline=False)
    embed.add_field(name="Nickname", value=member.nick or "None", inline=True)
    embed.add_field(name="Status", value=str(member.status).title(), inline=True)
    
    joined_at = member.joined_at.strftime("%Y-%m-%d") if member.joined_at else "Unknown"
    embed.add_field(name="Joined Server", value=joined_at, inline=False)
    embed.add_field(name="Account Created", value=member.created_at.strftime("%Y-%m-%d"), inline=False)
    
    roles = [role.mention for role in member.roles if role.name != "@everyone"]
    if roles:
        embed.add_field(name="Roles", value=", ".join(roles), inline=False)
    
    await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("❌ Command not found. Type !help to see available commands.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"❌ Missing required argument. Type !help {ctx.command} for usage.")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ You don't have permission to use this command.")
    else:
        print(f'Error: {error}')
        await ctx.send("❌ An error occurred while processing the command.")

if __name__ == '__main__':
    token = os.getenv('DISCORD_BOT_TOKEN')
    if not token:
        print("ERROR: DISCORD_BOT_TOKEN environment variable not set!")
        print("Please add your Discord bot token to the Replit Secrets.")
        exit(1)
    
    try:
        bot.run(token)
    except discord.LoginFailure:
        print("ERROR: Invalid Discord bot token!")
        print("Please check your token in the Replit Secrets.")
    except Exception as e:
        print(f"ERROR: {e}")
