# NaturismTLL Discord Bot

A Discord bot that allows people to connect with Mahdi through social media links directly from Discord!

## Features

- **!profile** - View Mahdi's profile with clickable Instagram and Telegram buttons
- **!hello** - Get a friendly greeting from the bot
- **!ping** - Check the bot's latency
- **!serverinfo** - Display server statistics and information
- **!userinfo** - Get detailed information about a Discord user
- **!help** - View all available commands

## Setup Instructions

### 1. Discord Bot Token

You need a Discord bot token to run this bot:

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application or select an existing one
3. Go to the "Bot" section
4. Click "Reset Token" to generate a new token
5. Copy the **complete** token (should be 59-72 characters long)
6. Add it to Replit Secrets as `DISCORD_BOT_TOKEN`

### 2. Social Media Usernames

The bot uses your Instagram and Telegram usernames to create profile links:

- `INSTAGRAM_USERNAME` - Your Instagram username (without @)
- `TELEGRAM_USERNAME` - Your Telegram username (without @)

These are already configured in Replit Secrets.

### 3. Bot Permissions

When inviting the bot to your Discord server, make sure it has these permissions:
- Read Messages/View Channels
- Send Messages
- Embed Links
- Read Message History

### 4. Bot Intents

The bot requires these intents (already configured in code):
- Message Content Intent
- Server Members Intent
- Presence Intent

Enable these in the Discord Developer Portal under Bot > Privileged Gateway Intents.

## How to Use

Once the bot is running and added to your server:

1. Type `!profile` to see Mahdi's profile with social media links
2. Click the Instagram or Telegram buttons to connect
3. Use `!help` to see all available commands

## Commands

| Command | Description |
|---------|-------------|
| `!profile` | View Mahdi's profile with social media links |
| `!hello` | Get a friendly greeting |
| `!ping` | Check bot latency |
| `!serverinfo` | View server information |
| `!userinfo [@user]` | View user information (optional: mention a user) |
| `!help` | List all commands |

## Running the Bot

The bot runs automatically when you start the Replit. Make sure your Discord bot token is properly set in Replit Secrets.

## Current Status

- ✅ Bot code created with social media profile feature
- ✅ Instagram and Telegram usernames configured
- ⏳ Waiting for valid Discord bot token

## Support

If you encounter any issues, check that:
1. Your Discord bot token is complete and valid
2. The bot has the required permissions in your server
3. All required intents are enabled in the Discord Developer Portal
