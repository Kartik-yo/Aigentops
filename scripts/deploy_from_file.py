import requests
import json
import sys

if len(sys.argv) != 2:
    print("Usage: python deploy_from_file.py <config.json>")
    sys.exit(1)

config_path = sys.argv[1]

with open(config_path, 'r') as f:
    config = json.load(f)

response = requests.post("http://localhost:8000/deploy", json=config)

if response.status_code == 200:
    print("✅ Agent Deployed:", response.json())
else:
    print("❌ Deployment Failed:", response.status_code, response.text)
