"""
Language Manager for bot internationalization (i18n).
Handles translation loading, user language preferences, and provides translation utilities.
"""
import discord
from discord.ext import commands
import sqlite3
import os
import json
import logging
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)

# Database path for language preferences
LANGUAGE_DB_PATH = 'db/language.sqlite'

# Default language
DEFAULT_LANGUAGE = 'en'

# Available languages
AVAILABLE_LANGUAGES = {
    'en': {'name': 'English', 'flag': '🇬🇧'},
    'ar': {'name': 'العربية', 'flag': '🇸🇦'}
}


class LanguageManager:
    """Manages translations and user language preferences."""
    
    def __init__(self):
        self.translations: Dict[str, Dict[str, Any]] = {}
        self.load_translations()
        self.init_database()
    
    def load_translations(self):
        """Load translations from languages.json file."""
        try:
            translations_file = 'languages.json'
            if os.path.exists(translations_file):
                with open(translations_file, 'r', encoding='utf-8') as f:
                    self.translations = json.load(f)
                logger.info(f"Loaded translations for languages: {', '.join(self.translations.keys())}")
            else:
                logger.warning(f"Translations file '{translations_file}' not found.")
                self.translations = {}
        except Exception as e:
            logger.error(f"Error loading translations: {e}")
            self.translations = {}
    
    def init_database(self):
        """Initialize the language preferences database."""
        try:
            os.makedirs('db', exist_ok=True)
            conn = sqlite3.connect(LANGUAGE_DB_PATH)
            cursor = conn.cursor()
            
            # Create table for user language preferences
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS user_languages (
                    user_id INTEGER PRIMARY KEY,
                    language TEXT NOT NULL DEFAULT 'en',
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Create table for guild language preferences
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS guild_languages (
                    guild_id INTEGER PRIMARY KEY,
                    language TEXT NOT NULL DEFAULT 'en',
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            conn.commit()
            conn.close()
            logger.info("Language database initialized successfully.")
        except Exception as e:
            logger.error(f"Error initializing language database: {e}")
    
    def get_user_language(self, user_id: int) -> str:
        """Get the preferred language for a user."""
        try:
            conn = sqlite3.connect(LANGUAGE_DB_PATH)
            cursor = conn.cursor()
            cursor.execute('SELECT language FROM user_languages WHERE user_id = ?', (user_id,))
            result = cursor.fetchone()
            conn.close()
            
            if result:
                return result[0]
            return DEFAULT_LANGUAGE
        except Exception as e:
            logger.error(f"Error getting user language: {e}")
            return DEFAULT_LANGUAGE
    
    def set_user_language(self, user_id: int, language: str) -> bool:
        """Set the preferred language for a user."""
        try:
            if language not in self.translations:
                logger.warning(f"Language '{language}' not available in translations.")
                return False
            
            conn = sqlite3.connect(LANGUAGE_DB_PATH)
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO user_languages (user_id, language, updated_at)
                VALUES (?, ?, CURRENT_TIMESTAMP)
                ON CONFLICT(user_id) DO UPDATE SET
                    language = excluded.language,
                    updated_at = CURRENT_TIMESTAMP
            ''', (user_id, language))
            conn.commit()
            conn.close()
            
            logger.info(f"Set language '{language}' for user {user_id}")
            return True
        except Exception as e:
            logger.error(f"Error setting user language: {e}")
            return False
    
    def get_guild_language(self, guild_id: int) -> str:
        """Get the preferred language for a guild."""
        try:
            conn = sqlite3.connect(LANGUAGE_DB_PATH)
            cursor = conn.cursor()
            cursor.execute('SELECT language FROM guild_languages WHERE guild_id = ?', (guild_id,))
            result = cursor.fetchone()
            conn.close()
            
            if result:
                return result[0]
            return DEFAULT_LANGUAGE
        except Exception as e:
            logger.error(f"Error getting guild language: {e}")
            return DEFAULT_LANGUAGE
    
    def set_guild_language(self, guild_id: int, language: str) -> bool:
        """Set the preferred language for a guild."""
        try:
            if language not in self.translations:
                logger.warning(f"Language '{language}' not available in translations.")
                return False
            
            conn = sqlite3.connect(LANGUAGE_DB_PATH)
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO guild_languages (guild_id, language, updated_at)
                VALUES (?, ?, CURRENT_TIMESTAMP)
                ON CONFLICT(guild_id) DO UPDATE SET
                    language = excluded.language,
                    updated_at = CURRENT_TIMESTAMP
            ''', (guild_id, language))
            conn.commit()
            conn.close()
            
            logger.info(f"Set language '{language}' for guild {guild_id}")
            return True
        except Exception as e:
            logger.error(f"Error setting guild language: {e}")
            return False
    
    def get_text(self, key: str, language: str = DEFAULT_LANGUAGE, **kwargs) -> str:
        """
        Get translated text for a given key.
        
        Args:
            key: Dot-notation key (e.g., 'language_selector.title')
            language: Language code (e.g., 'en', 'ar')
            **kwargs: Format parameters for the translation string
        
        Returns:
            Translated and formatted text, or the key itself if not found
        """
        try:
            # Get the translation dictionary for the language
            lang_dict = self.translations.get(language, self.translations.get(DEFAULT_LANGUAGE, {}))
            
            # Navigate through nested keys
            keys = key.split('.')
            value = lang_dict
            for k in keys:
                if isinstance(value, dict):
                    value = value.get(k)
                else:
                    value = None
                    break
            
            # If translation not found, try default language
            if value is None and language != DEFAULT_LANGUAGE:
                value = self.get_text(key, DEFAULT_LANGUAGE, **kwargs)
                return value
            
            # Format the string if kwargs provided
            if isinstance(value, str) and kwargs:
                return value.format(**kwargs)
            
            return value if value is not None else key
        except Exception as e:
            logger.error(f"Error getting text for key '{key}': {e}")
            return key
    
    def get_available_languages(self) -> Dict[str, Dict[str, str]]:
        """Get all available languages with their metadata."""
        return AVAILABLE_LANGUAGES


# Global language manager instance
language_manager = LanguageManager()


class LanguageSwitcher(commands.Cog):
    """Cog for language switching functionality."""
    
    def __init__(self, bot):
        self.bot = bot
        self.lang_manager = language_manager
    
    @discord.app_commands.command(name="language", description="Change your language preference")
    async def language_command(self, interaction: discord.Interaction):
        """Slash command to open language selector."""
        user_id = interaction.user.id
        current_lang = self.lang_manager.get_user_language(user_id)
        
        # Create embed
        embed = discord.Embed(
            title=self.lang_manager.get_text('language_selector.title', current_lang),
            description=self.lang_manager.get_text('language_selector.description', current_lang),
            color=discord.Color.blue()
        )
        
        # Add current language field
        current_lang_name = AVAILABLE_LANGUAGES.get(current_lang, {}).get('name', current_lang)
        current_lang_flag = AVAILABLE_LANGUAGES.get(current_lang, {}).get('flag', '🌍')
        embed.add_field(
            name=self.lang_manager.get_text('language_selector.current_language', current_lang),
            value=f"{current_lang_flag} {current_lang_name}",
            inline=False
        )
        
        # Create view with language selector
        view = LanguageSelectorView(self.lang_manager, current_lang)
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)


class LanguageSelectorView(discord.ui.View):
    """View for language selection."""
    
    def __init__(self, lang_manager: LanguageManager, current_lang: str):
        super().__init__(timeout=180)
        self.lang_manager = lang_manager
        self.current_lang = current_lang
        
        # Add language select dropdown
        self.add_item(LanguageSelect(lang_manager, current_lang))


class LanguageSelect(discord.ui.Select):
    """Select menu for choosing a language."""
    
    def __init__(self, lang_manager: LanguageManager, current_lang: str):
        self.lang_manager = lang_manager
        
        # Create options for each available language
        options = []
        for lang_code, lang_info in AVAILABLE_LANGUAGES.items():
            options.append(
                discord.SelectOption(
                    label=lang_info['name'],
                    value=lang_code,
                    emoji=lang_info['flag'],
                    default=(lang_code == current_lang)
                )
            )
        
        super().__init__(
            placeholder=lang_manager.get_text('language_selector.select_placeholder', current_lang),
            options=options,
            min_values=1,
            max_values=1
        )
    
    async def callback(self, interaction: discord.Interaction):
        """Handle language selection."""
        selected_lang = self.values[0]
        user_id = interaction.user.id
        
        # Update user's language preference
        success = self.lang_manager.set_user_language(user_id, selected_lang)
        
        if success:
            # Get language name for confirmation
            lang_name = AVAILABLE_LANGUAGES.get(selected_lang, {}).get('name', selected_lang)
            
            # Create success embed
            embed = discord.Embed(
                title=self.lang_manager.get_text('language_selector.success_title', selected_lang),
                description=self.lang_manager.get_text(
                    'language_selector.success_description',
                    selected_lang,
                    language=lang_name
                ),
                color=discord.Color.green()
            )
            
            await interaction.response.edit_message(embed=embed, view=None)
        else:
            await interaction.response.send_message(
                "❌ Failed to update language preference. Please try again.",
                ephemeral=True
            )


async def setup(bot):
    """Setup function for loading the cog."""
    await bot.add_cog(LanguageSwitcher(bot))
