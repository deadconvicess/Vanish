import os
import sys
import time
import platform
import subprocess
import urllib.request
import pkg_resources
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.text import Text
from rich.table import Table
console = Console()
BANNER = Text("""
   =*===
   $$- - $$$
   $ <    D$$
   $ -   $$$
,  $$$$  |
///; ,---' _ |----.
 \\ )(           /  )
 | \\/ \\.   '  _.|  \\              $
 |  \\ /(   /    /\\_ \\          $$$$$
  \\ /  (       / /  )         $$$ $$$
       (  ,   /_/ ,`_,-----.,$$  $$$
       |   <----|  \\---##     \\   $$
       /         \\\\\           |    $
      '   '                    |
      |                 \\      /
      /  \\_|    /______,/     /
     /   / |   /    |   |    /
    (   /--|  /.     \\  (\\  (_
     `----,( ( _\\     \\ / / ,/
           | /        /,_/,/
          _|/        / / (
         / (        ^-/, |
        /, |          ^-    
""", style="bold red")
POPULAR_PACKAGES = [
    "requests", "numpy", "pandas", "flask", "django", "pyinstaller", "nuitka",
    "pyarmor", "rich", "tk", "termcolor", "colorama",
    "pycryptodome", "cryptography",
    "discord.py", "aiohttp", "aiofiles",
    "pyautogui", "pynput", "pycaw", "pywin32", "psutil", "screeninfo",
    "pyperclip", "pyttsx3", "comtypes",
    "opencv-python", "pillow", "sounddevice", "scipy",
    "textual", "click",
    "python-dotenv", "jsonlines", "reportlab",
    "beautifulsoup4", "lxml"
]
def is_pip_working():
    try:
        subprocess.check_output([sys.executable, "-m", "pip", "--version"], stderr=subprocess.DEVNULL)
        return True
    except:
        return False
def repair_pip():
    console.print("\n[bold yellow]Pip is broken.[/bold yellow]")
    try:
        import ensurepip
        console.print("[cyan]Reinstalling pip...[/cyan]")
        ensurepip.bootstrap()
        subprocess.call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
    except Exception as e:
        console.print(f"[red]{e}[/red]")
    if not is_pip_working():
        console.print("[cyan]Trying..[/cyan]")
        try:
            url = "https://bootstrap.pypa.io/get-pip.py"
            urllib.request.urlretrieve(url, "get-pip.py")
            subprocess.call([sys.executable, "get-pip.py"])
        except Exception as e:
            console.print(f"[red]{e}[/red]")
    if is_pip_working():
        console.print("[green]Pip has been repaired[/green]\n")
    else:
        console.print("[bold red]Pip repair failed[/bold red]")
def upgrade_pip():
    console.print("\n[blue]Checking for pip upgrade...[/blue]")
    subprocess.call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"],
                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    console.print("[green]Pip is up to date.[/green]")
def open_current_folder():
    if platform.system() == "Windows":
        os.system("explorer .")
    else:
        console.print("[yellow]Only works on Windows.[/yellow]")
def generate_requirements_file(packages, output_path="requirements.txt"):
    installed = {pkg.key: pkg.version for pkg in pkg_resources.working_set}
    with open(output_path, "w") as f:
        for name in sorted(packages):
            key = name.lower().replace("_", "-")
            version = installed.get(key)
            if version:
                f.write(f"{key}=={version}\n")
            else:
                f.write(f"{key}\n")
    console.print(f"[bold green]\u2713 {output_path} generated.[/bold green]")
    open_current_folder()
def install_package(pkg, max_retries=3):
    for attempt in range(1, max_retries + 1):
        with Progress(SpinnerColumn(), TextColumn(f"[cyan]Installing [bold]{pkg}[/bold]")) as progress:
            progress.add_task("install", total=None)
            result = subprocess.call([sys.executable, "-m", "pip", "install", pkg],
                                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if result == 0:
            console.print(f"[green]\u2713 {pkg} installed.[/green]")
            return
        else:
            console.print(f"[yellow]Retrying {pkg}...[/yellow]")
            time.sleep(1)
    console.print(f"[red]\u2717 Failed to install {pkg} after {max_retries} attempts.[/red]")
def install_main_packages():
    for pkg in POPULAR_PACKAGES:
        install_package(pkg)
    generate_requirements_file(POPULAR_PACKAGES)
def install_custom_packages():
    console.print("[yellow]Enter Packages [/yellow]")
    try:
        user_input = sys.stdin.read().strip()
    except Exception as e:
        console.print(f"[red]Input failed: {e}[/red]")
        return
    packages = user_input.split()
    for pkg in packages:
        install_package(pkg)
    generate_requirements_file(packages)
def show_environment_info():
    os_name = platform.system()
    arch = platform.machine()
    py_version = platform.python_version()
    pip_version = subprocess.getoutput("pip --version") if is_pip_working() else "Unavailable"
    table = Table(title="System Specs", style="bold white")
    table.add_column("Detail", justify="right", style="cyan")
    table.add_column("Value", style="green")
    table.add_row("OS", os_name)
    table.add_row("Architecture", arch)
    table.add_row("Python", py_version)
    table.add_row("Pip", pip_version)
    console.print(table)
def display_menu():
    console.clear()
    console.print(BANNER)
    console.print(Panel.fit("[bold cyan]@deadconvicess", style="red"))
    show_environment_info()
    console.print("\n[bold magenta]Main Menu[/bold magenta]")
    console.print("[1] Install Packs")
    console.print("[2] Exit\n")
def main():
    if not is_pip_working():
        repair_pip()
    if is_pip_working():
        upgrade_pip()
    while True:
        display_menu()
        console.print("[yellow]->>[/yellow]")
        try:
            choice = sys.stdin.read(1).strip()
        except Exception as e:
            console.print(f"[red]Na - {e}[/red]")
            break
        if choice == '1':
            install_main_packages()
        if choice == '2':
            break
if __name__ == "__main__":
    main()
