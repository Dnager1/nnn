# Language System Documentation

## Overview

The bot now includes a comprehensive language/internationalization (i18n) system that allows users to select their preferred language for bot interactions. The system currently supports:
- **English (en)** 🇬🇧
- **Arabic (ar)** 🇸🇦

## Features

✅ **User Language Preferences**: Each user can set their own language preference
✅ **Guild Language Settings**: Server-wide language settings (if needed in future)
✅ **Persistent Storage**: Language preferences are stored in SQLite database
✅ **Easy Translation Management**: All translations in a single JSON file
✅ **Fallback System**: Falls back to English if translation is missing
✅ **Discord Integration**: Accessible via `/language` command and Theme Settings menu

## How to Use

### For Users

1. **Via Slash Command**:
   - Type `/language` in any channel
   - Select your preferred language from the dropdown
   - Your preference is saved automatically

2. **Via Settings Menu**:
   - Use `/settings` command
   - Navigate to Theme Settings
   - Click the "Language 🌍" button
   - Select your preferred language

### For Developers

#### Adding New Languages

1. **Edit `languages.json`**:
   ```json
   {
     "en": { ... existing English translations ... },
     "ar": { ... existing Arabic translations ... },
     "es": {
       "language_name": "Español",
       "language_flag": "🇪🇸",
       "language_selector": {
         "title": "🌍 Configuración de idioma",
         "description": "Selecciona tu idioma preferido...",
         ...
       },
       "common": {
         "back": "Atrás",
         "cancel": "Cancelar",
         ...
       }
     }
   }
   ```

2. **Update `cogs/language_manager.py`**:
   ```python
   AVAILABLE_LANGUAGES = {
       'en': {'name': 'English', 'flag': '🇬🇧'},
       'ar': {'name': 'العربية', 'flag': '🇸🇦'},
       'es': {'name': 'Español', 'flag': '🇪🇸'},  # Add new language here
   }
   ```

#### Using Translations in Code

```python
from cogs.language_manager import language_manager

# Get user's language preference
user_id = interaction.user.id
user_lang = language_manager.get_user_language(user_id)

# Get translated text
title = language_manager.get_text('language_selector.title', user_lang)

# Get translated text with format parameters
description = language_manager.get_text(
    'language_selector.success_description',
    user_lang,
    language='English'
)
```

#### Translation Key Structure

The `languages.json` file uses dot-notation keys:

```
language_name                          - Full language name
language_flag                          - Flag emoji
language_selector.title                - Language selector dialog title
language_selector.description          - Language selector description
language_selector.current_language     - "Current Language" label
language_selector.select_placeholder   - Dropdown placeholder text
language_selector.success_title        - Success message title
language_selector.success_description  - Success message description
common.back                            - "Back" button
common.cancel                          - "Cancel" button
common.confirm                         - "Confirm" button
common.settings                        - "Settings" label
common.save                            - "Save" button
common.close                           - "Close" button
```

## Database Schema

The language system uses `db/language.sqlite` with two tables:

### `user_languages`
| Column      | Type      | Description                    |
|-------------|-----------|--------------------------------|
| user_id     | INTEGER   | Discord user ID (Primary Key)  |
| language    | TEXT      | Language code (e.g., 'en')     |
| updated_at  | TIMESTAMP | Last update timestamp          |

### `guild_languages`
| Column      | Type      | Description                    |
|-------------|-----------|--------------------------------|
| guild_id    | INTEGER   | Discord guild ID (Primary Key) |
| language    | TEXT      | Language code (e.g., 'en')     |
| updated_at  | TIMESTAMP | Last update timestamp          |

## File Structure

```
bot-main/
├── languages.json                    # Translation strings
├── cogs/
│   └── language_manager.py          # Language management cog
└── db/
    └── language.sqlite               # Language preferences database
```

## Future Enhancements

Potential improvements for the language system:

1. **More Languages**: Add support for:
   - Spanish (es)
   - French (fr)
   - German (de)
   - Chinese (zh)
   - Russian (ru)

2. **UI Translation**: Extend translations to all bot UI elements:
   - Alliance management
   - Gift operations
   - Bear trap schedules
   - Minister menus

3. **Regional Variants**: Support regional language variants:
   - English: US, UK, AU
   - Arabic: SA, EG, UAE
   - Spanish: ES, MX, AR

4. **Translation Helper**: Create a command for translators to:
   - Export untranslated keys
   - Track translation progress
   - Validate translation files

5. **Automatic Translation**: Integrate with translation APIs for:
   - Quick draft translations
   - Translation suggestions

## Contributing Translations

To contribute a new language translation:

1. Fork the repository
2. Copy the `en` section in `languages.json`
3. Translate all strings to your language
4. Add your language to `AVAILABLE_LANGUAGES` in `cogs/language_manager.py`
5. Test your translations
6. Submit a pull request

### Translation Guidelines

- Keep formatting placeholders (e.g., `{language}`) unchanged
- Maintain the same tone and formality as English
- Use native speakers for review if possible
- Test with RTL languages (Arabic, Hebrew) to ensure proper rendering
- Keep emoji and special characters consistent

## Support

For issues or questions about the language system:
- Open an issue on GitHub
- Contact the development team on Discord
- Check the [common issues](https://github.com/whiteout-project/bot/wiki/Common-Issues) page

---

**Last Updated**: February 2026
**Version**: 1.0.0
