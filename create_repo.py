#!/usr/bin/env python3
"""
Create GitHub repository using API directly
"""
import os
import json
import urllib.request
import urllib.error

TOKEN = (
    os.environ.get("GH_TOKEN")
    or os.environ.get("GITHUB_TOKEN")
    or os.environ.get("GITHUB_PAT")
    or ""
)
if not TOKEN:
    raise SystemExit("Error: missing GitHub token (set GH_TOKEN / GITHUB_TOKEN / GITHUB_PAT)")

url = "https://api.github.com/user/repos"
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github.v3+json",
    "Content-Type": "application/json"
}
data = json.dumps({
    "name": "claw-companion",
    "description": "My first independent project - Created by Astra's Claw companion",
    "private": False
}).encode('utf-8')

try:
    req = urllib.request.Request(url, data=data, headers=headers, method='POST')
    with urllib.request.urlopen(req, timeout=30) as response:
        result = response.read().decode('utf-8')
        print(f"Success: {result}")
except urllib.error.HTTPError as e:
    print(f"Error: {e.code} - {e.read().decode('utf-8')}")
except Exception as e:
    print(f"Error: {e}")
