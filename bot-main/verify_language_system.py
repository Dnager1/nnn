#!/usr/bin/env python3
"""
Language System Startup Verification Script
Checks all components needed for the language system to work.
"""

import os
import sys
import json
import sqlite3

def print_header(text):
    print("\n" + "=" * 70)
    print(f"  {text}")
    print("=" * 70)

def check_mark(passed):
    return "✅" if passed else "❌"

def main():
    print_header("🌍 Language System Verification")
    
    all_checks_passed = True
    
    # Check 1: languages.json exists and is valid
    print("\n📄 Checking languages.json...")
    try:
        if not os.path.exists('languages.json'):
            print("❌ languages.json not found")
            all_checks_passed = False
        else:
            with open('languages.json', 'r', encoding='utf-8') as f:
                langs = json.load(f)
            
            if 'en' not in langs:
                print("❌ English (en) not found in languages.json")
                all_checks_passed = False
            else:
                print("✅ English (en) found")
            
            if 'ar' not in langs:
                print("❌ Arabic (ar) not found in languages.json")
                all_checks_passed = False
            else:
                print("✅ Arabic (ar) found")
            
            print(f"✅ languages.json is valid with {len(langs)} language(s)")
    except json.JSONDecodeError as e:
        print(f"❌ languages.json has invalid JSON: {e}")
        all_checks_passed = False
    except Exception as e:
        print(f"❌ Error reading languages.json: {e}")
        all_checks_passed = False
    
    # Check 2: language_manager.py exists
    print("\n📄 Checking language_manager.py...")
    if not os.path.exists('cogs/language_manager.py'):
        print("❌ cogs/language_manager.py not found")
        all_checks_passed = False
    else:
        print("✅ cogs/language_manager.py exists")
        
        # Check if it compiles
        try:
            with open('cogs/language_manager.py', 'r', encoding='utf-8') as f:
                code = f.read()
            compile(code, 'cogs/language_manager.py', 'exec')
            print("✅ language_manager.py syntax is valid")
            
            # Check for required components
            if 'class LanguageSwitcher' in code:
                print("✅ LanguageSwitcher class found")
            else:
                print("❌ LanguageSwitcher class not found")
                all_checks_passed = False
            
            if 'async def setup(bot):' in code:
                print("✅ setup() function found")
            else:
                print("❌ setup() function not found")
                all_checks_passed = False
            
            if '@discord.app_commands.command(name="language"' in code:
                print("✅ /language command definition found")
            else:
                print("❌ /language command definition not found")
                all_checks_passed = False
                
        except SyntaxError as e:
            print(f"❌ Syntax error in language_manager.py: {e}")
            all_checks_passed = False
    
    # Check 3: main.py loads language_manager
    print("\n📄 Checking main.py configuration...")
    if not os.path.exists('main.py'):
        print("❌ main.py not found")
        all_checks_passed = False
    else:
        with open('main.py', 'r', encoding='utf-8') as f:
            main_content = f.read()
        
        if '"language_manager"' in main_content or "'language_manager'" in main_content:
            print("✅ language_manager in cogs list")
        else:
            print("❌ language_manager not in cogs list")
            all_checks_passed = False
    
    # Check 4: pimp_my_bot.py integration
    print("\n📄 Checking pimp_my_bot.py integration...")
    if not os.path.exists('cogs/pimp_my_bot.py'):
        print("⚠️  pimp_my_bot.py not found (optional)")
    else:
        with open('cogs/pimp_my_bot.py', 'r', encoding='utf-8') as f:
            pimp_content = f.read()
        
        if 'language_btn' in pimp_content:
            print("✅ Language button found in pimp_my_bot.py")
        else:
            print("⚠️  Language button not found (optional)")
        
        if 'open_language' in pimp_content:
            print("✅ open_language callback found")
        else:
            print("⚠️  open_language callback not found (optional)")
    
    # Check 5: Database directory
    print("\n📁 Checking database directory...")
    if not os.path.exists('db'):
        print("⚠️  db directory doesn't exist, creating...")
        try:
            os.makedirs('db', exist_ok=True)
            print("✅ db directory created")
        except Exception as e:
            print(f"❌ Failed to create db directory: {e}")
            all_checks_passed = False
    else:
        print("✅ db directory exists")
    
    # Test database write permissions
    try:
        test_db = 'db/test_permissions.sqlite'
        conn = sqlite3.connect(test_db)
        conn.execute('CREATE TABLE test (id INTEGER)')
        conn.close()
        os.remove(test_db)
        print("✅ Database write permissions OK")
    except Exception as e:
        print(f"❌ Cannot write to db directory: {e}")
        all_checks_passed = False
    
    # Check 6: Documentation
    print("\n📚 Checking documentation...")
    docs = {
        'LANGUAGE_SYSTEM.md': 'Technical documentation',
        'LANGUAGE_USER_GUIDE.md': 'User guide',
        'LANGUAGE_TROUBLESHOOTING.md': 'Troubleshooting guide'
    }
    
    for doc, desc in docs.items():
        if os.path.exists(doc):
            print(f"✅ {doc} exists ({desc})")
        else:
            print(f"⚠️  {doc} not found ({desc}) - optional")
    
    # Final summary
    print_header("Summary")
    
    if all_checks_passed:
        print("\n✅ All critical checks passed!")
        print("\n🎉 The language system is properly configured.")
        print("\nNext steps:")
        print("1. Start your bot: python main.py")
        print("2. Wait for bot to login and sync commands (1-5 minutes)")
        print("3. In Discord, type /language to test")
        print("4. Or use Theme Settings → Language button")
        print("\nIf /language doesn't appear:")
        print("- Wait a few minutes for Discord to sync")
        print("- Try in a different server")
        print("- Check LANGUAGE_TROUBLESHOOTING.md")
        return 0
    else:
        print("\n❌ Some checks failed!")
        print("\nPlease fix the issues above before running the bot.")
        print("See LANGUAGE_TROUBLESHOOTING.md for help.")
        return 1

if __name__ == '__main__':
    # Change to bot directory if needed
    if len(sys.argv) > 1:
        os.chdir(sys.argv[1])
    
    sys.exit(main())
