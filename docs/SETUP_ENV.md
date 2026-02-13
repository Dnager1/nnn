# 🔐 Environment Setup Guide

## Quick Start

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and set your values:
   ```bash
   DISCORD_BOT_TOKEN=your_actual_token_here
   ```

3. Run the bot:
   ```bash
   python main.py
   ```

## Environment Variables

### Required
- `DISCORD_BOT_TOKEN`: Your Discord bot token

### Optional (with defaults)
- `WOS_API_SECRET`: API secret for Whiteout Survival (default: tB87#kPtkxqOS2)
- `SOCKS5_PROXY`: Proxy URL in format `socks5://user:pass@ip:port`
- `SOCKS5_PROXY_ENABLED`: Enable proxy (true/false)
- `DB_PATH`: Database directory path (default: db/)
- `LOG_LEVEL`: Logging level (default: INFO)
- `LOG_PATH`: Log directory path (default: log/)

## Backward Compatibility

The bot still supports `bot_token.txt` for backward compatibility. If `DISCORD_BOT_TOKEN` is not set in `.env`, it will fall back to reading from `bot_token.txt`.

## Migration from Old Setup

If you're upgrading from an older version:

1. Create `.env` file
2. Copy your bot token from `bot_token.txt` to `.env`:
   ```
   DISCORD_BOT_TOKEN=<your token from bot_token.txt>
   ```
3. (Optional) Delete `bot_token.txt` - it's no longer needed

## Security Notes

- ✅ `.env` is in `.gitignore` - your secrets won't be committed
- ✅ Use `.env.example` to share required variables without exposing secrets
- ✅ Never commit actual tokens or passwords
