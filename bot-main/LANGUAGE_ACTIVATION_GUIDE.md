# How to Activate and Test the Language System
# كيفية تفعيل واختبار نظام اللغة

## Quick Start (English)

The language system is **already fully implemented** in the bot. Follow these steps to activate and test it:

### Step 1: Verify Installation ✅

Run the verification script to check everything is configured:

```bash
cd /path/to/bot-main
python3 verify_language_system.py
```

You should see: `✅ All critical checks passed!`

### Step 2: Start the Bot 🚀

```bash
python main.py
```

**Look for these messages in the logs:**
```
✓ Loaded language_manager cog
✓ Loaded 27/27 cogs
Logged in as YourBotName
✓ Synced X slash command(s)
✓ /language command registered successfully
```

✅ If you see all these messages, the language system is active!

### Step 3: Test in Discord 🎮

**Method 1: Using /language command**
1. In any Discord channel, type `/language`
2. The command should appear in autocomplete
3. Click it or press Enter
4. A language selector will appear
5. Choose your language (🇬🇧 English or 🇸🇦 العربية)
6. You'll see a success message

**Method 2: Using Theme Settings**
1. Type `/settings` in Discord
2. Click on "Theme Settings" button
3. In Row 3, click the "🌍 Language" button
4. Choose your language from the dropdown
5. You'll see a success message

### Step 4: Verify It Works 🎉

After selecting a language:
- Use `/language` again - it should show your selected language
- The interface should display in your chosen language
- Your preference is saved to the database

---

## البدء السريع (عربي)

نظام اللغة **مطبق بالكامل بالفعل** في البوت. اتبع هذه الخطوات لتفعيله واختباره:

### الخطوة 1: التحقق من التثبيت ✅

قم بتشغيل سكريبت التحقق للتأكد من أن كل شيء مهيأ:

```bash
cd /path/to/bot-main
python3 verify_language_system.py
```

يجب أن ترى: `✅ All critical checks passed!`

### الخطوة 2: تشغيل البوت 🚀

```bash
python main.py
```

**ابحث عن هذه الرسائل في السجلات:**
```
✓ Loaded language_manager cog
✓ Loaded 27/27 cogs
Logged in as YourBotName
✓ Synced X slash command(s)
✓ /language command registered successfully
```

✅ إذا رأيت كل هذه الرسائل، فنظام اللغة نشط!

### الخطوة 3: اختبر في Discord 🎮

**الطريقة 1: استخدام أمر /language**
1. في أي قناة Discord، اكتب `/language`
2. يجب أن يظهر الأمر في الإكمال التلقائي
3. انقر عليه أو اضغط Enter
4. سيظهر محدد اللغة
5. اختر لغتك (🇬🇧 English أو 🇸🇦 العربية)
6. سترى رسالة نجاح

**الطريقة 2: استخدام إعدادات المظهر**
1. اكتب `/settings` في Discord
2. انقر على زر "Theme Settings"
3. في الصف 3، انقر على زر "🌍 Language"
4. اختر لغتك من القائمة المنسدلة
5. سترى رسالة نجاح

### الخطوة 4: تحقق من أنه يعمل 🎉

بعد اختيار لغة:
- استخدم `/language` مرة أخرى - يجب أن يعرض لغتك المختارة
- يجب أن تظهر الواجهة بلغتك المختارة
- تفضيلك محفوظ في قاعدة البيانات

---

## Troubleshooting / استكشاف الأخطاء

### Problem: /language command doesn't appear

**Wait Time**: Discord may take 1-5 minutes to sync new slash commands after bot startup. Be patient!

**Check these:**
1. Did you see "✓ /language command registered successfully" in logs?
2. Try refreshing Discord (Ctrl+R or Cmd+R)
3. Try in a different server
4. Try in DM with the bot

**Still not working?**
```bash
# Run troubleshooting
cat LANGUAGE_TROUBLESHOOTING.md

# Re-verify installation
python3 verify_language_system.py
```

### المشكلة: أمر /language لا يظهر

**وقت الانتظار**: قد يستغرق Discord من 1-5 دقائق لمزامنة أوامر slash الجديدة بعد بدء تشغيل البوت. كن صبورًا!

**تحقق من هذه:**
1. هل رأيت "✓ /language command registered successfully" في السجلات؟
2. جرب تحديث Discord (Ctrl+R أو Cmd+R)
3. جرب في سيرفر آخر
4. جرب في رسالة خاصة مع البوت

**لا يزال لا يعمل؟**
```bash
# تشغيل استكشاف الأخطاء
cat LANGUAGE_TROUBLESHOOTING.md

# إعادة التحقق من التثبيت
python3 verify_language_system.py
```

---

## Features Included / الميزات المضمنة

✅ **Two Languages** / لغتان
- English (🇬🇧) - Default
- Arabic (🇸🇦) - Full RTL support

✅ **Two Access Methods** / طريقتان للوصول
- `/language` slash command
- Language button in Theme Settings

✅ **Persistent Storage** / تخزين دائم
- User preferences saved in SQLite database
- Survives bot restarts

✅ **Complete Documentation** / وثائق كاملة
- LANGUAGE_SYSTEM.md - Technical docs
- LANGUAGE_USER_GUIDE.md - User guide
- LANGUAGE_TROUBLESHOOTING.md - Troubleshooting
- verify_language_system.py - Automated checks

---

## Screenshots / لقطات شاشة

### English Interface
```
┌─────────────────────────────────────────────────┐
│  🌍 Language Settings                           │
├─────────────────────────────────────────────────┤
│  Select your preferred language for bot        │
│  interactions.                                  │
│                                                 │
│  Current Language:                              │
│  🇬🇧 English                                     │
│                                                 │
│  [Choose a language... ▼]                       │
└─────────────────────────────────────────────────┘
```

### Arabic Interface / الواجهة العربية
```
┌─────────────────────────────────────────────────┐
│  🌍 إعدادات اللغة                               │
├─────────────────────────────────────────────────┤
│  اختر لغتك المفضلة للتفاعل مع البوت.          │
│                                                 │
│  اللغة الحالية:                                │
│  🇸🇦 العربية                                    │
│                                                 │
│  [اختر لغة... ▼]                                │
└─────────────────────────────────────────────────┘
```

---

## Technical Details / التفاصيل التقنية

### Files / الملفات
- `languages.json` - Translation strings
- `cogs/language_manager.py` - Language system cog
- `db/language.sqlite` - User preferences (auto-created)

### Database Schema / مخطط قاعدة البيانات
```sql
CREATE TABLE user_languages (
    user_id INTEGER PRIMARY KEY,
    language TEXT NOT NULL DEFAULT 'en',
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
```

### Adding More Languages / إضافة المزيد من اللغات

To add a new language, edit `languages.json`:
```json
{
  "en": { ... },
  "ar": { ... },
  "fr": {
    "language_name": "Français",
    "language_flag": "🇫🇷",
    "language_selector": {
      "title": "🌍 Paramètres de langue",
      ...
    }
  }
}
```

And update `AVAILABLE_LANGUAGES` in `cogs/language_manager.py`:
```python
AVAILABLE_LANGUAGES = {
    'en': {'name': 'English', 'flag': '🇬🇧'},
    'ar': {'name': 'العربية', 'flag': '🇸🇦'},
    'fr': {'name': 'Français', 'flag': '🇫🇷'},  # New!
}
```

---

## Support / الدعم

Need help? / تحتاج مساعدة؟

1. **Check the logs** / تحقق من السجلات
   ```bash
   python main.py 2>&1 | grep language
   ```

2. **Run verification** / شغل التحقق
   ```bash
   python3 verify_language_system.py
   ```

3. **Read troubleshooting guide** / اقرأ دليل استكشاف الأخطاء
   ```bash
   cat LANGUAGE_TROUBLESHOOTING.md
   ```

4. **Check documentation** / تحقق من الوثائق
   - LANGUAGE_SYSTEM.md
   - LANGUAGE_USER_GUIDE.md
   - LANGUAGE_VISUAL_GUIDE.md

---

## Summary / الملخص

✅ **Language system is ready!** / نظام اللغة جاهز!

The language feature is **fully implemented and activated**. Just start your bot and use `/language` command or the Language button in Theme Settings.

ميزة اللغة **منفذة ومفعلة بالكامل**. فقط ابدأ البوت الخاص بك واستخدم أمر `/language` أو زر اللغة في إعدادات المظهر.

🎉 Enjoy the bot in your preferred language! / استمتع بالبوت بلغتك المفضلة!
