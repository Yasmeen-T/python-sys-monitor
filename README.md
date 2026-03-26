# 🚀 System Monitoring Tool - Docker & GitHub Workflow

This project demonstrates a foundational DevOps workflow by deploying a Python-based system utility inside an isolated **Ubuntu Docker Container**. The source code is managed via **GitHub** and pulled into the container environment manually to simulate live server provisioning.

## 🎯 Project Objective
- Develop a Python script for system diagnostics.
- Version control the script using Git/GitHub.
- Provision a containerized Ubuntu environment.
- Manually install dependencies and execute the script within the container.

---

## 🛠️ Features
The Python utility (`sys_monitor.py`) provides the following diagnostics:
- **Real-time Clock:** Displays current date and time.
- **Hostname Discovery:** Identifies the unique Docker container ID.
- **Environment Check:** Prints the installed Python version.
- **User Identity:** Identifies the current active user (e.g., `root`).
- **File System Audit:** Lists all files in the current directory and provides a **total file count**.
- **Interactive Logging:** Accepts user input to tag logs.

---

## 🚀 DevOps Workflow Steps

### 1. Local Development & Source Control
The script was authored locally and pushed to this repository:
```bash
git init
git add sys_monitor.py
git commit -m "Initial commit: System Monitor Tool"
git push origin master
docker run -it --name devops-project ubuntu
apt update
apt install -y python3 git

--- 🚀 SYSTEM MONITOR TOOL ---
📅 Date & Time: 2026-03-26 09:56:16
💻 Hostname: ec8cecaf0cb2
🐍 Python Version: 3.12.3
👤 Current User: root
📁 Files in Directory (2 total):
   - sys_monitor.py
   - .git
------------------------------
Enter a tag for this log: Final_Test_Pass
✅ Log tagged as: Final_Test_Pass
