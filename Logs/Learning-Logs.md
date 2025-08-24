Understood. Here is your **updated single-file Learning Log (Days 1–6)** with Day 1 expanded to include **GitHub account setup + repo creation**. Everything else remains as you requested (no Q\&A, no time tracking, Day 2↔Day 5 switched, Day 6 left blank).

---

# 📓 Learning Log — Week 1 (Days 1–6)

---

## 📅 Day 1 — Python, VS Code, Git, and GitHub Setup

### ✅ What I Did

* Installed **Python 3.13** (system-wide).

  * Verified:

    ```bash
    python --version
    pip --version
    py --version    # Windows launcher
    ```
* Installed **VS Code** and confirmed the integrated terminal works.
* Installed **Git for Windows**.

  * Set global identity so commits are labeled correctly:

    ```bash
    git config --global user.name "Your Name"
    git config --global user.email "you@example.com"
    ```
* Created a working folder and first script:

  ```bash
  mkdir sekai-week1
  cd sekai-week1
  notepad hello.py
  ```

  `hello.py`:

  ```python
  print("Hello, Sekai!")
  ```

  Run:

  ```bash
  python hello.py
  ```

  Expected → `Hello, Sekai!`
* Initialized **local Git repo** and made first commit:

  ```bash
  git init
  git add hello.py
  git commit -m "First commit: hello.py"
  ```

### ✅ GitHub Account & First Remote Repo (Detailed)

* Created **GitHub account** (github.com → Sign up → verify email).
* (Optional but recommended) Enabled **2FA** (Settings → Password and authentication → Two-factor).
* Created **new repository** on GitHub:

  * Top-right **+** → **New repository**
  * **Repository name:** `sekai-week1`
  * **Public**
  * Do **not** add a README for this flow (we already have a local commit).
  * Click **Create repository**.
* Linked local repo to GitHub using **HTTPS** remote:

  ```bash
  git remote add origin https://github.com/<your-username>/sekai-week1.git
  git branch -M main
  git push -u origin main
  ```

  * On first push, GitHub may open a browser window → authorize Git → push completes.
  * `-u` sets “upstream tracking,” so later `git push`/`git pull` work without extra args.

### 📖 Key Definitions

* **Python interpreter:** Program that runs `.py` files.
* **Script:** A file with Python code you execute (`python file.py`).
* **VS Code (editor):** Code editor with integrated terminal and Git UI.
* **Git:** Version control tool that tracks file changes over time.
* **Repository (repo):** Folder tracked by Git; contains history and configuration.
* **Commit:** A snapshot of changes with a message.
* **Remote:** The copy of your repo hosted online (e.g., GitHub).
* **origin:** Conventional name for the primary remote.
* **Branch (`main`):** A line of development (your default branch).
* **Upstream tracking (`-u`):** Links local branch to its remote so `git push/pull` know where to go.
* **HTTPS vs SSH:** Two ways to connect to GitHub. You used **HTTPS** (browser-based auth); SSH uses keys.

### 🛠️ Mini Project

* **hello.py** → first successful Python run.
* Local repo created, first commit made, remote connected, push confirmed on GitHub.

---

## 📅 Day 2 — Website Status Checker (HTTP Basics)

### ✅ What I Did

* Activated project virtual environment when needed:

  ```bash
  python -m venv venv
  .\venv\Scripts\activate     # Windows PowerShell
  ```
* Installed `requests`:

  ```bash
  pip install requests
  pip freeze > requirements.txt
  ```
* Built **`check_site.py`**: prompts for a URL, sends an HTTP **GET**, checks **status code**.

  * 200 → “UP”
  * Else → “responded with status”
  * Network error → prints exception
* Tested with valid and invalid URLs.
* Added/committed/pushed changes to GitHub.

### 📖 Key Definitions

* **HTTP:** Protocol for web communication.
* **Client/Server:** Your script (client) talks to a website (server).
* **GET request:** Retrieve data from a URL.
* **Status codes:** `200 OK`, `404 Not Found`, `500 Server Error`, etc.
* **Timeout:** How long to wait for a response before failing.
* **Exception:** Error raised during execution (e.g., network failures).

### 🛠️ Mini Project

* **check\_site.py** → practical health checker for URLs.

---

## 📅 Day 3 — Git Workflow (Deeper) + .gitignore Hygiene

### ✅ What I Did

* Practiced the **Git cycle** repeatedly:

  ```bash
  git status
  git add <files>
  git commit -m "message"
  git push
  ```
* Created a proper **`.gitignore`** to exclude local environment files:

  ```
  venv/
  __pycache__/
  *.pyc
  ```
* Cleaned accidental files (e.g., temporary text files), committed the removal, pushed.

### 📖 Key Definitions

* **Working directory:** Your current files on disk.
* **Staging area (index):** Files prepared for commit (`git add`).
* **HEAD:** Pointer to the current commit.
* **.gitignore:** File patterns Git should not track.
* **Remote tracking branch:** Local branch linked to a remote counterpart (e.g., `main` ↔ `origin/main`).

### 🛠️ Mini Project

* Repo streamlined; only relevant source tracked; environment-specific files ignored.

---

## 📅 Day 4 — First Web Request & API Response Objects

### ✅ What I Did

* Wrote **`test_request.py`** using `requests`:

  ```python
  import requests
  res = requests.get("https://httpbin.org/get")
  print(res.status_code)
  print(res.json())
  ```
* Learned to inspect **`Response`**:

  * `status_code`
  * `headers`
  * `text` vs `json()`
* Confirmed JSON payload structure by printing the raw response, then parsing.

### 📖 Key Definitions

* **API:** Program-to-program interface over HTTP.
* **Endpoint:** Specific URL for API functionality.
* **Headers:** Metadata in requests/responses (e.g., `User-Agent`, `Content-Type`).
* **Body:** Main content of a request/response (often JSON).
* **JSON:** Text format for structured data (maps to Python dicts/lists).

### 🛠️ Mini Project

* **test\_request.py** → verified HTTP basics and JSON parsing.

---

## 📅 Day 5 — Input/Output Practice (Strings & Formatting)

### ✅ What I Did

* Built **`io_practice.py`**:

  * Asked for favorite **anime** and **character** using `input()`.
  * Cleaned input with `.strip()`.
  * Fallback defaults if user pressed Enter.
  * Printed a formatted summary using **f-strings**.
  * Constructed a “prompt stub” string for future LLM use.
* Ran in terminal and verified output formatting.

### 📖 Key Definitions

* **Variable:** Named reference to a value (e.g., `anime = "Naruto"`).
* **String:** Text data; supports methods like `.strip()`.
* **f-string:** Interpolation syntax: `f"{name} is great"`.
* **Branching (if):** Execute code conditionally (e.g., if blank input, set default).

### 🛠️ Mini Project

* **io\_practice.py** → first interactive console workflow, foundation for future prompts.


---

# 📓 Daily Learning Log — Day 6


**The Struggle with Hugging Face (and Victory): First LLM Story Generator**

---

## 📝 Tasks Done

**Step 1:** Created a new Python file `story-gen.py`.
**Step 2:** Attempted to call a Hugging Face model directly from its webpage URL → got errors (`404`, `"Method Not Allowed"`).
**Step 3:** Misconfigured `.env` with an API key (later deleted, since the Space was public and didn’t need it).
**Step 4:** Learned the difference between Hugging Face **model pages** vs. **Space endpoints**.
**Step 5:** Created my **own Hugging Face Space**, which auto-generated a real endpoint:

```
https://<username>-<space-name>.hf.space/run/predict
```

**Step 6:** Updated Python script:

* Printed raw responses first.
* Adjusted parsing to handle varied JSON structures.
* Fixed `KeyError: 'data'` and `JSONDecodeError`.

**Step 7:** Sent test prompts until I got the first working **isekai anime-style story output**.

---

## 🐛 Errors & Fixes

* **Error:** `"Method Not Allowed"` and `"404 Not Found"`.
  **Fix:** Realized I was using the wrong link → needed the Space endpoint, not the model’s web page.

* **Error:** `KeyError: 'data'` and broken JSON parsing.
  **Fix:** Printed full response first → updated code to handle Hugging Face’s actual response format.

* **Error:** Overcomplicated setup with `.env`.
  **Fix:** Deleted `.env` → Space endpoint was public and didn’t need API keys.

---

## 📖 Definitions Learned

* **Hugging Face Space** → A hosted mini-app built with Gradio/Streamlit that auto-generates an API endpoint.
* **Endpoint** → The real URL a program calls to get results from an API.
* **KeyError** → Python error when trying to access a dictionary key that doesn’t exist.
* **JSONDecodeError** → Happens when trying to parse invalid or unexpected JSON data.
* **Prompt Engineering** → The act of refining text instructions to shape better AI outputs.

---

## 🏗️ Mini-Project Created

**`story-gen.py`**

* Calls Hugging Face Space API.
* Sends an anime story prompt.
* Receives generated text output (first light novel–style story).

**Why it matters:**
This was the first **end-to-end AI integration** I built — proof I can connect Python with a hosted LLM API.

---

