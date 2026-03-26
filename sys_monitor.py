import os
import platform
import socket
from datetime import datetime

def run_monitor():
    print("\n--- 🚀 SYSTEM MONITOR TOOL ---")
    print(f"📅 Date & Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"💻 Hostname: {socket.gethostname()}")
    print(f"🐍 Python Version: {platform.python_version()}")
    
    # Bonus: Current User
    try:
        current_user = os.getlogin()
    except:
        current_user = os.getenv('USER', 'root')
    print(f"👤 Current User: {current_user}")
    
    # Bonus: File List & Count
    files = os.listdir('.')
    print(f"📁 Files in Directory ({len(files)} total):")
    for file in files:
        print(f"   - {file}")
        
    print("\n------------------------------")
    user_msg = input("Enter a tag for this log: ")
    print(f"✅ Log tagged as: {user_msg}")
    print("------------------------------\n")

if __name__ == "__main__":
    run_monitor()
