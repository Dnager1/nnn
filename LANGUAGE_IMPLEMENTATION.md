# 🌍 نظام اللغة - دليل التطبيق الكامل
# Language System - Complete Implementation Guide

## ✅ التحديثات المنفذة / Implemented Updates

### 1. ملف `languages.json` / File `languages.json`
- ✅ توسيع شامل للترجمات / Comprehensive translation expansion
- ✅ إضافة ترجمات Settings Menu / Added Settings Menu translations
- ✅ إضافة ترجمات Theme Settings / Added Theme Settings translations
- ✅ إضافة ترجمات Common strings / Added Common strings translations
- ✅ إضافة "yes" و "no" للإنجليزية والعربية / Added "yes" and "no" for English and Arabic
- ✅ تحديث العناوين بالرموز التعبيرية (⚙️ للإعدادات، 🎨 للمظهر) / Updated titles with emojis (⚙️ for settings, 🎨 for themes)
- ✅ التأكد من تطابق جميع المفاتيح بين اللغتين / Ensured all keys match between languages

### 2. ملف `cogs/pimp_my_bot.py` / File `cogs/pimp_my_bot.py`
- ✅ إصلاح دالة `open_language` (السطر 1300) / Fixed `open_language` function (line 1300)
- ✅ تحسين التكامل مع language_manager / Improved integration with language_manager
- ✅ إضافة import statements الصحيحة / Added correct import statements
  - `from .language_manager import language_manager, LanguageSelectorView, AVAILABLE_LANGUAGES`
- ✅ استخدام theme.emColor1 للألوان / Using theme.emColor1 for colors
- ✅ عرض اللغة الحالية مع العلم / Display current language with flag
- ✅ إرسال الاستجابة مع LanguageSelectorView / Send response with LanguageSelectorView

### 3. ملف `cogs/alliance.py` / File `cogs/alliance.py`
- ✅ دعم اللغات في Settings Menu موجود بالفعل / Language support in Settings Menu already exists
- ✅ استخدام language_manager للترجمات / Using language_manager for translations
- ✅ دعم RTL للعربية مطبق / RTL support for Arabic applied
- ✅ جميع مفاتيح الترجمة صحيحة / All translation keys are correct

### 4. ملف `cogs/language_manager.py` / File `cogs/language_manager.py`
- ✅ نظام إدارة اللغة كامل / Complete language management system
- ✅ LanguageManager class with translation loading / LanguageManager class مع تحميل الترجمات
- ✅ User and guild language preferences / تفضيلات اللغة للمستخدمين والخوادم
- ✅ LanguageSelectorView for UI / LanguageSelectorView للواجهة
- ✅ /language slash command / أمر /language

## 🚀 كيفية الاستخدام / How to Use

### للمستخدمين / For Users:

#### الطريقة الأولى: من خلال Theme Settings / Method 1: Through Theme Settings
1. افتح `/settings` / Open `/settings`
2. اضغط "Theme Settings" / Click "Theme Settings"
3. اضغط زر "🌍 Language" / Click "🌍 Language" button
4. اختر لغتك من القائمة / Select your language from the dropdown
5. ✅ تم! سيتم حفظ تفضيلاتك / Done! Your preferences are saved

#### الطريقة الثانية: باستخدام أمر Slash / Method 2: Using Slash Command
1. اكتب `/language` في Discord / Type `/language` in Discord
2. اختر لغتك من القائمة / Select your language from the dropdown
3. ✅ تم! / Done!

### للمطورين / For Developers:

#### استخدام نظام الترجمة / Using the Translation System

```python
from cogs.language_manager import language_manager

# Get user's language preference
user_id = interaction.user.id
user_lang = language_manager.get_user_language(user_id)

# Get translated text
title = language_manager.get_text('settings_menu.title', user_lang)
description = language_manager.get_text('settings_menu.description', user_lang)

# Get translated text with format parameters
success_msg = language_manager.get_text(
    'language_selector.success_description',
    user_lang,
    language='العربية'
)
```

#### إضافة ترجمات جديدة / Adding New Translations

1. افتح `languages.json` / Open `languages.json`
2. أضف المفاتيح الجديدة في كل من `en` و `ar` / Add new keys in both `en` and `ar`
3. استخدم dot notation للمفاتيح المتداخلة / Use dot notation for nested keys
4. تأكد من تطابق البنية بين اللغات / Ensure structure matches between languages

مثال / Example:
```json
{
  "en": {
    "new_feature": {
      "title": "New Feature",
      "description": "This is a new feature"
    }
  },
  "ar": {
    "new_feature": {
      "title": "ميزة جديدة",
      "description": "هذه ميزة جديدة"
    }
  }
}
```

#### استخدام الترجمات في الواجهة / Using Translations in UI

```python
# In your embed creation
embed = discord.Embed(
    title=language_manager.get_text('new_feature.title', user_lang),
    description=language_manager.get_text('new_feature.description', user_lang),
    color=theme.emColor1
)

# In button labels
button = discord.ui.Button(
    label=language_manager.get_text('common.save', user_lang),
    style=discord.ButtonStyle.primary
)
```

## 📋 قائمة التحقق / Checklist

- [x] languages.json موسع بالكامل / languages.json fully expanded
- [x] زر اللغة يعمل في Theme Settings / Language button works in Theme Settings
- [x] Settings Menu مترجم بالكامل / Settings Menu fully translated
- [x] دعم RTL للعربية / RTL support for Arabic
- [x] التوثيق الكامل / Complete documentation
- [x] open_language function محدثة / open_language function updated
- [x] استيراد LanguageSelectorView / Import LanguageSelectorView
- [x] استخدام theme.emColor1 / Using theme.emColor1
- [x] عرض اللغة الحالية / Display current language

## 🎨 مفاتيح الترجمة المتاحة / Available Translation Keys

### Language Selector
- `language_selector.title`
- `language_selector.description`
- `language_selector.current_language`
- `language_selector.select_placeholder`
- `language_selector.success_title`
- `language_selector.success_description`

### Settings Menu
- `settings_menu.title`
- `settings_menu.description`
- `settings_menu.menu_categories`
- `settings_menu.alliance_operations`
- `settings_menu.alliance_operations_desc`
- `settings_menu.alliance_member_operations`
- `settings_menu.alliance_member_desc`
- `settings_menu.bot_operations`
- `settings_menu.bot_operations_desc`
- `settings_menu.gift_code_operations`
- `settings_menu.gift_code_desc`
- `settings_menu.alliance_history`
- `settings_menu.alliance_history_desc`
- `settings_menu.support_operations`
- `settings_menu.support_operations_desc`
- `settings_menu.theme_settings`
- `settings_menu.theme_settings_desc`
- `settings_menu.other_features`
- `settings_menu.other_features_desc`

### Theme Settings
- `theme_settings.title`
- `theme_settings.description`
- `theme_settings.info_line1` through `theme_settings.info_line5`
- `theme_settings.global_active`
- `theme_settings.this_server`
- `theme_settings.using_global`
- `theme_settings.total_themes`
- `theme_settings.quick_guide`
- `theme_settings.create`
- `theme_settings.create_desc`
- `theme_settings.edit`
- `theme_settings.edit_desc`
- `theme_settings.import`
- `theme_settings.export`
- `theme_settings.import_export_desc`
- `theme_settings.set_default`
- `theme_settings.set_default_desc`
- `theme_settings.apply_to_server`
- `theme_settings.apply_to_server_desc`
- `theme_settings.revert_to_global`
- `theme_settings.revert_to_global_desc`
- `theme_settings.delete`
- `theme_settings.delete_desc`
- `theme_settings.share_online`
- `theme_settings.share_online_desc`
- `theme_settings.language`
- `theme_settings.main_menu`
- `theme_settings.footer`

### Common Strings
- `common.back`
- `common.cancel`
- `common.confirm`
- `common.settings`
- `common.save`
- `common.close`
- `common.success`
- `common.error`
- `common.loading`
- `common.yes`
- `common.no`

## 🎉 النتيجة / Result

نظام لغة **شامل ومتكامل** يدعم / A **comprehensive and integrated** language system supporting:
- 🇬🇧 الإنجليزية / English
- 🇸🇦 العربية (مع دعم RTL) / Arabic (with RTL support)
- 🌍 سهولة إضافة لغات جديدة / Easy addition of new languages

### الميزات الرئيسية / Key Features:
1. **تفضيلات المستخدم** / **User Preferences**: كل مستخدم يمكنه اختيار لغته الخاصة / Each user can choose their own language
2. **تكامل كامل** / **Full Integration**: جميع القوائم الرئيسية مترجمة / All main menus translated
3. **سهولة الاستخدام** / **Easy to Use**: طريقتان للوصول (أمر Slash وزر في الإعدادات) / Two ways to access (Slash command and button in settings)
4. **دعم RTL** / **RTL Support**: دعم كامل للغة العربية / Full support for Arabic language
5. **قابلية التوسع** / **Extensibility**: سهولة إضافة لغات ومفاتيح جديدة / Easy to add new languages and keys

## 🔧 استكشاف الأخطاء / Troubleshooting

### المشكلة: زر اللغة لا يعمل / Issue: Language button not working
**الحل / Solution:**
- تأكد من أن `cogs/language_manager.py` محمل / Ensure `cogs/language_manager.py` is loaded
- تحقق من أن `languages.json` موجود / Check that `languages.json` exists
- راجع السجلات للأخطاء / Review logs for errors

### المشكلة: الترجمات لا تظهر / Issue: Translations not showing
**الحل / Solution:**
- تحقق من صحة `languages.json` / Verify `languages.json` is valid
- تأكد من وجود قاعدة البيانات `db/language.sqlite` / Ensure database `db/language.sqlite` exists
- أعد تشغيل البوت / Restart the bot

### المشكلة: أمر /language لا يظهر / Issue: /language command not showing
**الحل / Solution:**
- انتظر بضع دقائق لمزامنة Discord / Wait a few minutes for Discord sync
- جرب في خادم مختلف / Try in a different server
- تأكد من تحميل language_manager cog / Ensure language_manager cog is loaded

## 📚 مراجع إضافية / Additional References

- `LANGUAGE_SYSTEM.md` - الوثائق التقنية / Technical documentation
- `LANGUAGE_USER_GUIDE.md` - دليل المستخدم / User guide
- `LANGUAGE_TROUBLESHOOTING.md` - دليل استكشاف الأخطاء / Troubleshooting guide
- `verify_language_system.py` - سكريبت التحقق / Verification script

---

**تاريخ التحديث / Update Date:** 2026-02-12  
**الإصدار / Version:** 2.0.0  
**الحالة / Status:** ✅ مكتمل / Complete
