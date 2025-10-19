# Discord Bot Setup Guide

This guide will help you get your Discord bot up and running.

## Step 1: Get Your Discord Bot Token

### Creating a Discord Application

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" in the top right
3. Give your application a name (e.g., "Mahdi's Profile Bot")
4. Click "Create"

### Setting Up the Bot

1. In your application, click on "Bot" in the left sidebar
2. Click "Add Bot" and confirm
3. Under "Privileged Gateway Intents", enable:
   - ✅ Presence Intent
   - ✅ Server Members Intent
   - ✅ Message Content Intent
4. Click "Reset Token" to generate a new token
5. Copy the token (it should be 59-72 characters long)

**Important**: This token is like a password - never share it publicly!

### Adding Token to Replit

1. In Replit, look for the "Secrets" tab (lock icon) in the left sidebar
2. Find the `DISCORD_BOT_TOKEN` entry
3. Paste your complete Discord bot token
4. The bot will automatically restart with the new token

## Step 2: Invite Your Bot to Discord

### Generate Invite Link

1. In Discord Developer Portal, go to "OAuth2" → "URL Generator"
2. Under "Scopes", select:
   - ✅ bot
3. Under "Bot Permissions", select:
   - ✅ Read Messages/View Channels
   - ✅ Send Messages
   - ✅ Embed Links
   - ✅ Read Message History
4. Copy the generated URL at the bottom
5. Paste it into your browser and select your server
6. Click "Authorize"

## Step 3: Configure Social Media

Your Instagram and Telegram usernames are already configured! If you need to update them:

1. Go to Replit Secrets
2. Update `INSTAGRAM_USERNAME` with your Instagram username (no @ symbol)
3. Update `TELEGRAM_USERNAME` with your Telegram username (no @ symbol)

## Step 4: Test Your Bot

Once the bot is online in your Discord server:

1. In any channel, type: `!profile`
2. You should see an embed with your profile and clickable buttons
3. Click the buttons to test the social media links
4. Try other commands like `!hello` and `!ping`

## Troubleshooting

### Bot shows as offline
- Check that your Discord bot token is complete and valid
- Make sure the token was copied correctly without extra spaces
- Verify the bot workflow is running in Replit

### Commands don't work
- Make sure you're using the correct prefix: `!`
- Verify Message Content Intent is enabled in Discord Developer Portal
- Check that the bot has permission to read and send messages

### Buttons don't appear
- Make sure your bot has "Embed Links" permission
- Check that the social media usernames are set correctly

### "Invalid Discord bot token" error
- Your token is incomplete or incorrect
- Discord bot tokens are 59-72 characters long
- Generate a new token in the Discord Developer Portal

## Need Help?

If you're still having issues:
1. Check the console logs in Replit for error messages
2. Verify all required intents are enabled
3. Make sure the bot has proper permissions in your Discord server
4. Try regenerating your Discord bot token
