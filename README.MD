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


# 🚀 Project Setup & Usage

Welcome! This repository contains a simple **HTTP Checker Tool** 🕵️‍♂️ that verifies if a website is accessible.
It also includes setup instructions for using a **Python virtual environment (venv)**.

---

## 🐍 Virtual Environment Setup

1. **Create a virtual environment** (only once per project):

   ```bash
   python -m venv venv
   ```

2. **Activate the environment**:

   * Windows PowerShell:

     ```bash
     .\venv\Scripts\activate
     ```
   * Mac/Linux:

     ```bash
     source venv/bin/activate
     ```

3. **Fix PowerShell execution policy (if blocked)**:

   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   ```

   Then activate again.

4. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

5. **(Optional) Check installed packages**:

   ```bash
   pip freeze
   ```

6. **Exit the virtual environment**:

   ```bash
   deactivate
   ```

---

## 📡 HTTP Checker Script

The core of this project is `check_site.py`, which checks whether a website is online.

```python
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
```

---

## ▶️ How to Run

From inside the virtual environment:

```bash
python check_site.py
```

Enter a website URL (e.g., `https://google.com`) when prompted.
The script will report if the site is:

* ✅ **UP** (status 200)
* ⚠️ **Responded with error status**
* ❌ **DOWN** (network error, timeout, etc.)

---

## 📂 Project Structure

```
sekai-week1/
│-- venv/               # Virtual environment (ignored in Git)
│-- check_site.py        # HTTP checker script
│-- requirements.txt     # Dependencies list
│-- README.md            # Project documentation
```

---

## 🌟 Notes

* Always activate the virtual environment before running the script.
* Keep dependencies tracked in `requirements.txt` (`pip freeze > requirements.txt`).
* This project is a starting point for learning **Python scripting, HTTP requests, and environment management**.

---

