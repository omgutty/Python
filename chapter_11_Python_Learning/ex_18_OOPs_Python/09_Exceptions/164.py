# 164.py
# Topic: try / except - real-world (HTTP request)
#
# requests.get() can fail in many ways: wrong URL (ConnectionError),
# slow server (Timeout), or anything else. Each is caught separately.
# The last "except Exception as e" is a SAFETY NET for anything not
# listed - and prints the actual error message.
# NOTE: needs `pip install requests` first.

import requests

try:
    url = input("Enter the url")
    # response = requests.get("https://google.com")
    response = requests.get(url, timeout=3)
    print(response.status_code)
except requests.exceptions.ConnectionError:
    print("Error due to the wrong URL or connectioned failed!")
except requests.exceptions.Timeout:
    print("Timeout error, not able to laod the URL.")
except Exception as e:
    print(e)