# Sekai Week 1
Practicing Python + Git + Requests library+ LLM MINI Project
This is my first Python + Git project, built as part of my learning journey.  
It contains simple scripts, a test for HTTP requests, and dependency tracking.


## 📂 Project Structure

* `hello.py` → Simple Python script
* `io_practice.py` → Collects user’s favorite anime/character, shows formatted summary
* `test_request.py` → Makes a web request using the `requests` library
* `check_site.py` → HTTP checker script (Day 5 milestone)
* `story-gen.py` → Calls a Hugging Face Space API to generate short anime-style stories (Day 6 milestone)
* `requirements.txt` → List of dependencies
* `venv/` → Virtual environment (not pushed to GitHub)

---

## ⚙️ Setup & Usage

1. Clone this repo:

```bash
git clone https://github.com/rudranoir0-dot/sekai-week1.git
cd sekai-week1
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
.\venv\Scripts\activate   # Windows PowerShell
source venv/bin/activate  # Mac/Linux
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the scripts (examples):

```bash
python io_practice.py
python check_site.py
python story-gen.py
```

Example run of `check_site.py`:

```bash
Enter a website URL to check: https://google.com
✅ https://google.com is UP (status 200)
```

---

## 📈 Week 1 Progress (Milestones Only)

✅ Learned basic **Python syntax** (print, loops, input/output).
✅ Practiced **Git workflow** (init, add, commit, push).
✅ Built small scripts (`hello.py`, `io_practice.py`).
✅ Used **Requests library** to fetch data from the web.
✅ Built a working **site checker** (`check_site.py`).
✅ First **API integration with Hugging Face Space** (`story-gen.py`) → generated anime-style short stories.

---

## 🏆 Key Takeaway

By the end of Week 1, I moved from **basic Python scripts** → to **web requests** → to my **first LLM-powered project**.
This closed the loop from coding fundamentals to a working AI mini-project.

