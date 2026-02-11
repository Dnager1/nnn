# Language System Troubleshooting Guide
# دليل استكشاف أخطاء نظام اللغة

## English Version

### Problem: /language command not appearing after bot startup

#### Step 1: Check Bot Logs
When the bot starts, you should see these messages:
```
✓ Loaded language_manager cog
✓ Loaded X/Y cogs
Logged in as YourBotName
✓ Synced X slash command(s)
✓ /language command registered successfully
```

**If you see:** `✗ Failed to load cog language_manager:`
- **Cause:** The language_manager.py file is missing or has syntax errors
- **Solution:** Verify the file exists at `cogs/language_manager.py`
- **Solution:** Run the bot with `python main.py --repair` to restore files

**If you see:** `⚠ /language command not found in synced commands`
- **Cause:** The command was loaded but not synced to Discord
- **Solution:** Wait 1-5 minutes for Discord to propagate commands
- **Solution:** Try in a different server or DM with the bot
- **Solution:** Restart the bot to force a re-sync

#### Step 2: Check languages.json
```bash
python3 -c "import json; open('languages.json')"
```
- If this fails, the languages.json file is missing or corrupted
- Restore from the repository or recreate it

#### Step 3: Verify Bot Permissions
The bot needs these permissions:
- `applications.commands` scope enabled in Discord Developer Portal
- Bot must be invited with slash commands scope
- If bot was invited before slash commands were added, re-invite it

#### Step 4: Discord Command Sync
Discord may take time to sync commands:
1. Wait 1-5 minutes after bot startup
2. Try using `/` and see if `language` appears in autocomplete
3. If not, try in a different server
4. If still not working, try DM with the bot

#### Step 5: Manual Command Refresh
In Discord:
1. Right-click the bot in the member list
2. Select "Update Application Commands" (if available)
3. Or restart your Discord client

#### Step 6: Check Database Directory
```bash
mkdir -p db
```
The bot needs write access to create `db/language.sqlite`

### Verification Script

Run this script to verify everything is set up correctly:

```python
python3 -c "
import os
import json

# Check files
print('Checking files...')
assert os.path.exists('cogs/language_manager.py'), 'language_manager.py missing'
assert os.path.exists('languages.json'), 'languages.json missing'
print('✓ All files present')

# Check JSON
with open('languages.json') as f:
    langs = json.load(f)
assert 'en' in langs and 'ar' in langs
print('✓ languages.json valid')

# Check database directory
os.makedirs('db', exist_ok=True)
print('✓ Database directory ready')

print('\n✅ All checks passed!')
"
```

### Common Issues

**Issue:** Command appears but shows error when clicked
- **Cause:** Database initialization failed
- **Solution:** Check `db` folder permissions
- **Solution:** Delete `db/language.sqlite` and restart bot

**Issue:** Command works but shows English instead of Arabic
- **Cause:** User preference not set yet
- **Solution:** This is normal for first use - just select Arabic

**Issue:** Language button in Theme Settings doesn't work
- **Cause:** pimp_my_bot.py not updated or language_manager not loaded
- **Solution:** Verify pimp_my_bot.py has the language button code
- **Solution:** Check bot logs for cog loading errors

---

## النسخة العربية

### المشكلة: أمر /language لا يظهر بعد تشغيل البوت

#### الخطوة 1: تحقق من سجلات البوت
عند بدء تشغيل البوت، يجب أن ترى هذه الرسائل:
```
✓ Loaded language_manager cog
✓ Loaded X/Y cogs
Logged in as YourBotName
✓ Synced X slash command(s)
✓ /language command registered successfully
```

**إذا رأيت:** `✗ Failed to load cog language_manager:`
- **السبب:** ملف language_manager.py مفقود أو يحتوي على أخطاء
- **الحل:** تحقق من وجود الملف في `cogs/language_manager.py`
- **الحل:** شغل البوت بـ `python main.py --repair` لاستعادة الملفات

**إذا رأيت:** `⚠ /language command not found in synced commands`
- **السبب:** الأمر تم تحميله لكن لم يتم مزامنته مع Discord
- **الحل:** انتظر 1-5 دقائق حتى ينشر Discord الأوامر
- **الحل:** جرب في سيرفر آخر أو رسالة خاصة مع البوت
- **الحل:** أعد تشغيل البوت لفرض إعادة المزامنة

#### الخطوة 2: تحقق من languages.json
```bash
python3 -c "import json; open('languages.json')"
```
- إذا فشل هذا، فملف languages.json مفقود أو تالف
- استعده من المستودع أو أعد إنشاءه

#### الخطوة 3: تحقق من صلاحيات البوت
البوت يحتاج هذه الصلاحيات:
- `applications.commands` مفعل في بوابة مطوري Discord
- يجب دعوة البوت مع نطاق slash commands
- إذا تمت دعوة البوت قبل إضافة slash commands، أعد دعوته

#### الخطوة 4: مزامنة أوامر Discord
قد يستغرق Discord وقتًا لمزامنة الأوامر:
1. انتظر 1-5 دقائق بعد بدء تشغيل البوت
2. جرب استخدام `/` وانظر إذا ظهر `language` في الإكمال التلقائي
3. إذا لم يظهر، جرب في سيرفر آخر
4. إذا لم ينجح، جرب رسالة خاصة مع البوت

#### الخطوة 5: تحديث الأوامر يدويًا
في Discord:
1. انقر بزر الماوس الأيمن على البوت في قائمة الأعضاء
2. اختر "Update Application Commands" (إن وجد)
3. أو أعد تشغيل تطبيق Discord الخاص بك

#### الخطوة 6: تحقق من مجلد قاعدة البيانات
```bash
mkdir -p db
```
البوت يحتاج صلاحية الكتابة لإنشاء `db/language.sqlite`

### المشاكل الشائعة

**المشكلة:** الأمر يظهر لكن يعرض خطأ عند النقر عليه
- **السبب:** فشل تهيئة قاعدة البيانات
- **الحل:** تحقق من صلاحيات مجلد `db`
- **الحل:** احذف `db/language.sqlite` وأعد تشغيل البوت

**المشكلة:** الأمر يعمل لكن يعرض الإنجليزية بدلاً من العربية
- **السبب:** تفضيل المستخدم لم يتم تعيينه بعد
- **الحل:** هذا طبيعي للاستخدام الأول - فقط اختر العربية

**المشكلة:** زر اللغة في إعدادات المظهر لا يعمل
- **السبب:** pimp_my_bot.py لم يتم تحديثه أو language_manager لم يتم تحميله
- **الحل:** تحقق من أن pimp_my_bot.py يحتوي على كود زر اللغة
- **الحل:** تحقق من سجلات البوت لأخطاء تحميل الـ cogs

---

## Quick Fix Commands

### Check all components:
```bash
cd /path/to/bot
python3 verify_language_system.py
```

### Verify cog loading:
```bash
cd /path/to/bot
python3 -c "
import sys
sys.path.insert(0, '.')
from cogs.language_manager import language_manager
print('✓ language_manager can be imported')
print('Available languages:', list(language_manager.translations.keys()))
"
```

### Create db directory:
```bash
mkdir -p db
chmod 755 db
```

### Test database:
```bash
python3 -c "
import sqlite3
import os
os.makedirs('db', exist_ok=True)
conn = sqlite3.connect('db/language.sqlite')
conn.execute('CREATE TABLE IF NOT EXISTS test (id INTEGER)')
conn.close()
print('✓ Database can be created')
os.remove('db/language.sqlite')
"
```

## Support

If none of these solutions work:
1. Check the bot logs for errors
2. Verify Discord bot token is valid
3. Ensure bot has necessary intents enabled
4. Try restarting the bot
5. Contact support with bot logs

For more help, see:
- LANGUAGE_SYSTEM.md - Technical documentation
- LANGUAGE_USER_GUIDE.md - User guide
- README.md - General bot documentation
