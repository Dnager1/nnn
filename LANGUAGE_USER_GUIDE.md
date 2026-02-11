# Language Switcher - User Guide

## Quick Start Guide

### Method 1: Using the /language Command

The easiest way to change your language is with the `/language` slash command:

1. Type `/language` in any channel where the bot is present
2. A dropdown menu will appear showing available languages:
   - 🇬🇧 English
   - 🇸🇦 العربية (Arabic)
3. Click on your preferred language
4. You'll see a confirmation message
5. Your preference is saved automatically!

### Method 2: Via Settings Menu

You can also access the language switcher through the bot's settings:

1. Type `/settings` to open the main settings menu
2. Navigate to **Theme Settings** (the palette/customization option)
3. Look for the **🌍 Language** button (Row 3, between "Share Online" and "Main Menu")
4. Click the Language button
5. Select your preferred language from the dropdown
6. Confirmation message will appear

## What Gets Translated?

Currently, the language system translates:
- Language selector interface
- Common UI elements (Back, Cancel, Confirm, Settings, Save, Close)
- System messages related to language selection

### Upcoming Translations

Future updates will include translations for:
- Alliance management messages
- Gift code redemption interfaces
- Event scheduling and reminders
- Minister appointment planning
- And more!

## Supported Languages

### English (en) 🇬🇧
- Default language
- Fully supported
- All features available

### Arabic (ar) 🇸🇦
- Right-to-left (RTL) text support
- Full Arabic translations
- All features available

## FAQ

**Q: Will my language preference sync across servers?**
A: Yes! Your language preference is tied to your Discord user ID, so it works across all servers where the bot is present.

**Q: Can server admins set a default language for their server?**
A: Currently, language preferences are per-user. Server-wide defaults may be added in future updates.

**Q: How do I switch back to English?**
A: Just use the `/language` command or Language button again and select English.

**Q: Are all bot messages translated?**
A: Currently, the language system covers the language selector interface and common UI elements. More translations are being added in future updates.

**Q: Can I help translate the bot to my language?**
A: Yes! Check the [LANGUAGE_SYSTEM.md](LANGUAGE_SYSTEM.md) file for contribution guidelines.

## Screenshots

### Language Selector Dialog
```
┌──────────────────────────────────────┐
│  🌍 Language Settings                │
├──────────────────────────────────────┤
│  Select your preferred language for  │
│  bot interactions.                   │
│                                      │
│  Current Language:                   │
│  🇬🇧 English                          │
│                                      │
│  [Choose a language... ▼]            │
│                                      │
└──────────────────────────────────────┘
```

### After Selection
```
┌──────────────────────────────────────┐
│  ✅ Language Updated                 │
├──────────────────────────────────────┤
│  Your language preference has been   │
│  saved to **العربية**.               │
│                                      │
└──────────────────────────────────────┘
```

### Arabic Interface Example
```
┌──────────────────────────────────────┐
│  🌍 إعدادات اللغة                    │
├──────────────────────────────────────┤
│  اختر لغتك المفضلة للتفاعل مع       │
│  البوت.                              │
│                                      │
│  اللغة الحالية:                     │
│  🇸🇦 العربية                         │
│                                      │
│  [اختر لغة... ▼]                     │
│                                      │
└──────────────────────────────────────┘
```

## Technical Details

- **Storage**: Your language preference is stored in a SQLite database
- **Performance**: Instant language switching with no lag
- **Persistence**: Your preference persists even if the bot restarts
- **Privacy**: Only your Discord user ID and language preference are stored

## Need Help?

If you encounter any issues with the language system:
1. Try using the `/language` command to reset your preference
2. Contact server administrators
3. Report issues on the bot's GitHub repository
4. Join the support Discord server

---

Enjoy the bot in your preferred language! 🌍
