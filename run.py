# run.py
import os
# app.py or main.py
import requests

def ping_self():
    try:
        requests.get("https://pythonfinalproj.onrender.com/")
        print("Self-ping successful")
    except Exception as e:
        print(f"Ping failed: {e}")

# Ping on startup
ping_self()

from app import create_app

app = create_app()
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)

