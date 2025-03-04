import os
import sys
import random
import socket
import base64
import psutil
import requests
import time
from termcolor import colored
from pyfiglet import figlet_format

# Function to Display Header (Always Visible)
def show_header():
    os.system("clear")  
    title = colored(figlet_format("TTT TOOLS"), "white")
    print(title)
    print(colored("TechTrio™ © 2025", "magenta"))
    print(colored("Author: Ashwith", "magenta"))
    print(colored("Team: TechTrio™", "magenta"))
    print()

# Show Header at Start
show_header()

# Function to Show Available Commands
def show_commands():
    commands = f"""
{colored('Commands:', 'cyan')}
{colored('1. clear', 'white')} - Clear terminal but keep header
{colored('2. exit', 'white')} - Exit the tool
{colored('3. battery', 'yellow')} - Show battery status
{colored('4. disk', 'yellow')} - Show disk usage
{colored('5. uptime', 'yellow')} - Show system uptime
{colored('6. ip', 'yellow')} - Show IP address
{colored('7. ping <website>', 'yellow')} - Ping a website
{colored('8. netstat', 'yellow')} - Show active network connections
{colored('9. mkfile <filename>', 'cyan')} - Create a file
{colored('10. mkdir <foldername>', 'cyan')} - Create a folder
{colored('11. ls', 'cyan')} - List files in current directory
{colored('12. rm <filename>', 'cyan')} - Delete a file
{colored('13. install <package>', 'green')} - Install a package
{colored('14. update', 'green')} - Update all packages
{colored('15. random', 'blue')} - Generate a random number
{colored('16. date', 'blue')} - Show current date and time
{colored('17. ascii', 'blue')} - Show cool ASCII art
{colored('18. ps', 'yellow')} - Show running processes
{colored('19. kill <PID>', 'yellow')} - Kill a process
{colored('20. zip <filename> <zipname>', 'cyan')} - Compress file into ZIP
{colored('21. unzip <zipname>', 'cyan')} - Extract ZIP file
{colored('22. cat <filename>', 'cyan')} - Show file contents
{colored('23. edit <filename>', 'cyan')} - Edit file using nano
{colored('24. copy <text>', 'cyan')} - Copy text to clipboard
{colored('25. paste', 'cyan')} - Paste text from clipboard
{colored('26. qr <text>', 'magenta')} - Generate a QR code
{colored('27. scanqr', 'magenta')} - Scan a QR code
{colored('28. say <text>', 'green')} - Speak text using TTS
{colored('29. listen', 'green')} - Convert speech to text
{colored('30. weather <city>', 'blue')} - Get current weather
{colored('31. timezone <city>', 'blue')} - Get time zone
{colored('32. cpu', 'yellow')} - Show CPU usage
{colored('33. memory', 'yellow')} - Show RAM usage
{colored('34. yt <query>', 'cyan')} - Search YouTube
{colored('35. wiki <query>', 'cyan')} - Search Wikipedia
{colored('36. password', 'red')} - Generate a strong password
{colored('37. encrypt <text>', 'red')} - Encrypt text (Base64)
{colored('38. decrypt <text>', 'red')} - Decrypt Base64 text
{colored('39. joke', 'magenta')} - Get a random joke
{colored('40. help', 'cyan')} - Show this help message
"""
    print(commands)

# Function Definitions
def get_battery_status():
    try:
        os.system("termux-battery-status")
    except Exception:
        print("Battery info not available.")

def get_disk_usage():
    disk = psutil.disk_usage('/')
    print(f"Total: {disk.total // (1024**3)}GB | Used: {disk.used // (1024**3)}GB | Free: {disk.free // (1024**3)}GB")

def get_uptime():
    uptime = time.time() - psutil.boot_time()
    print(f"System Uptime: {int(uptime // 3600)} hours, {int((uptime % 3600) // 60)} minutes")

def get_ip():
    try:
        ip = requests.get("https://api64.ipify.org?format=json", timeout=5).json()["ip"]
        print(f"Public IP: {ip}")
    except requests.exceptions.RequestException:
        print("Error: Could not retrieve IP. Check your internet connection.")

def ping_website(site):
    os.system(f"ping -c 4 {site}")

def netstat_info():
    os.system("netstat -tulnp")

def show_processes():
    os.system("ps aux")

def kill_process(pid):
    os.system(f"kill {pid}")

def encrypt_text(text):
    encoded = base64.b64encode(text.encode()).decode()
    print(f"Encrypted: {encoded}")

def decrypt_text(text):
    try:
        decoded = base64.b64decode(text).decode()
        print(f"Decrypted: {decoded}")
    except Exception:
        print("Invalid encrypted text!")

def generate_password():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = "".join(random.choice(chars) for _ in range(12))
    print(f"Generated Password: {password}")

def fetch_joke():
    try:
        joke = requests.get("https://v2.jokeapi.dev/joke/Any").json()
        if joke["type"] == "single":
            print(joke["joke"])
        else:
            print(joke["setup"])
            print(joke["delivery"])
    except:
        print("Error: Unable to fetch a joke.")

def text_to_speech(text):
    os.system(f"termux-tts-speak '{text}'")

def speech_to_text():
    os.system("termux-speech-to-text")

def generate_qr(text):
    os.system(f"qrencode -o qr.png '{text}' && termux-open qr.png")

def scan_qr():
    os.system("termux-qrcode-decode")

# Command Handling
while True:
    command = input(colored("\nTTT> ", "cyan")).strip().lower()

    if command == "exit":
        print(colored("Exiting TTT TOOLS...", "red"))
        sys.exit()
    elif command == "clear":
        show_header()
    elif command == "battery":
        get_battery_status()
    elif command == "disk":
        get_disk_usage()
    elif command == "uptime":
        get_uptime()
    elif command == "ip":
        get_ip()
    elif command.startswith("ping "):
        ping_website(command.split(" ")[1])
    elif command == "netstat":
        netstat_info()
    elif command == "ps":
        show_processes()
    elif command.startswith("kill "):
        kill_process(command.split(" ")[1])
    elif command.startswith("encrypt "):
        encrypt_text(command[8:])
    elif command.startswith("decrypt "):
        decrypt_text(command[8:])
    elif command == "password":
        generate_password()
    elif command == "joke":
        fetch_joke()
    elif command.startswith("say "):
        text_to_speech(command[4:])
    elif command == "listen":
        speech_to_text()
    elif command.startswith("qr "):
        generate_qr(command[3:])
    elif command == "scanqr":
        scan_qr()
    elif command == "help":
        show_commands()
    else:
        print(colored("Invalid command! Type 'help' for a list of commands.", "red"))
