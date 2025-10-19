# Replit Project Information

## Overview
This is a Discord bot that allows users to view Mahdi's profile and connect with him on Instagram and Telegram through clickable buttons in Discord.

## Current State
- **Type**: Discord Bot (Python)
- **Framework**: discord.py 2.6.4
- **Status**: Code ready, waiting for valid Discord bot token

## Project Structure
```
.
├── bot.py                  # Main Discord bot application
├── .circleci/
│   └── config.yml         # CircleCI configuration
├── .replit                # Replit configuration
├── .gitignore             # Python gitignore
├── pyproject.toml         # Python dependencies
├── uv.lock                # Dependency lock file
├── README.md              # Project documentation
└── replit.md              # This file
```

## Recent Changes
- **2025-10-19**: Repository imported to Replit
- **2025-10-19**: Discord bot created with profile feature
- **2025-10-19**: Added social media links (Instagram & Telegram) with clickable buttons
- **2025-10-19**: Configured Discord integration and installed discord.py
- **2025-10-19**: Added environment variables for social media usernames

## Key Features

### Profile Command (!profile)
- Displays an embed with Mahdi's profile information
- Shows clickable buttons for Instagram and Telegram
- Users can directly connect to social media by clicking buttons

### Additional Commands
- `!hello` - Friendly greeting
- `!ping` - Check bot latency
- `!serverinfo` - Server statistics
- `!userinfo` - User information
- `!help` - List all commands

## Environment Variables
The bot uses the following secrets (stored in Replit Secrets):
- `DISCORD_BOT_TOKEN` - Discord bot authentication token (needs to be valid)
- `INSTAGRAM_USERNAME` - Instagram username for profile links (configured)
- `TELEGRAM_USERNAME` - Telegram username for profile links (configured)

## Architecture

### Bot Structure
- **bot.py**: Main application file containing:
  - Bot initialization with intents
  - Command handlers for all bot commands
  - Profile command with Button UI
  - Error handling for command errors

### Discord.py Features Used
- Commands extension for command handling
- Embeds for rich message formatting
- Button UI components for clickable social media links
- Event handlers for bot lifecycle

### Workflow
- **Discord Bot**: Runs `python bot.py` in console mode
- Automatically starts when Replit starts
- Logs output to console for monitoring

## Next Steps
1. Get a valid Discord bot token from Discord Developer Portal
2. Add the complete token to Replit Secrets
3. Enable required intents in Discord Developer Portal:
   - Message Content Intent
   - Server Members Intent
4. Invite bot to Discord server with proper permissions
5. Test the !profile command to verify social media links work

## User Preferences
- Bot uses purple color theme for profile embeds
- Instagram emoji: 📷
- Telegram emoji: ✈️
- Command prefix: `!`

## Technical Notes
- Python 3.11
- Uses discord.py for Discord API interaction
- Button components for interactive UI
- Environment-based configuration for security
- No database required (stateless bot)
