import requests
from datetime import datetime

URL = "https://www.cadservices.in"

def ping():
    try:
        r = requests.get(URL, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        status = r.status_code
    except Exception as e:
        status = "FAILED"
        print("ERROR:", e)

    print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] STATUS: {status}")

if __name__ == "__main__":
    ping()
