# sekai-week1 🚀

# Sekai Week 1
Practicing Python + Git + Requests library
This is my first Python + Git project, built as part of my learning journey.  
It contains simple scripts, a test for HTTP requests, and dependency tracking.

## 📂 Project Structure

- hello.py → Simple Python script  
- test_request.py → Makes a web request using the `requests` library  
- requirements.txt → List of dependencies  
- venv/ → Virtual environment (not pushed to GitHub)

\## ⚙️ Setup
1\. Clone this repo:

&nbsp;  ```bash

&nbsp;  git clone https://github.com/rudranoir0-dot/sekai-week1.git

&nbsp;  cd sekai-week1

DME.MD

# 🚀 Setup Instructions 
🐍 Virtual Environment Guide

1.  A virtual environment (venv) is like a private room for Python.
You create it once per project: 
```python
 
```python -m venv venv


Then, every time you open this project later, you just enter it:
 .\venv\Scripts\activate   # Windows PowerShell
 source venv/bin/activate  # Mac/Linux

 - When you’re done, you can leave it:
deactivate

2.  If PowerShell blocks it (execution policy error), run:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

Then activate again.

3. Install Dependencies
pip install -r requirements.txt

4. Check Installed Packages (optional)
pip freeze

5. Exit Virtual Environment
deactivate


📡 HTTP Checker Script

This repo includes a simple script to check if a website is online:

 python check_site.py


You’ll be prompted to enter a website URL (e.g. https://google.com) → the script will tell you if it’s ✅ UP, ⚠️ Error, or ❌ DOWN.


