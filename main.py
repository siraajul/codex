import requests
import time

# Target URL
url = "https://geekssort.com/"

# Optional: headers
headers = {
    "User-Agent": "LoadTester/1.0"
}

# Optional: delay between hits in seconds
delay = 0.1

# Counter
count = 0

try:
    while True:
        response = requests.get(url, headers=headers, timeout=5)

        if response.status_code == 200:
            count += 1
            print(f"[{count}] Success: {response.status_code}")
        else:
            print(f"[{count}] Failed with status code: {response.status_code}")
            break

        time.sleep(delay)

except requests.exceptions.RequestException as e:
    print(f"[{count}] Request failed: {e}")
