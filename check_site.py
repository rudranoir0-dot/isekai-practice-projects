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
