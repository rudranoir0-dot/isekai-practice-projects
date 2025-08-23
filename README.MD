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


## 📡 HTTP Checker Script 


# check_site.py
import requests

def check_site(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"✅ {url} is UP (status {response.status_code})")
        else:
            print(f"⚠️ {url} responded with status {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ {url} is DOWN. Error: {e}")

if __name__ == "__main__":
    site = input("Enter a website URL to check: ")
    check_site(site)


This repository includes a simple tool to verify if a website is accessible:

```bash
python check_site.py
```

You'll be asked to enter a website URL (e.g., `https://google.com`).  
The script will report if the site is **UP** ✅, **Error** ⚠️, or **DOWN** ❌.


