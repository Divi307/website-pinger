import requests
import sys
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

    # Fail workflow if ping fails
    if status != 200:
        sys.exit(1)  # GitHub Actions will mark run as failed

if __name__ == "__main__":
    ping()
