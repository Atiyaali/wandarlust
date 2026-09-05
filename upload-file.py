import os
import sys
import requests

# Retrieve command line arguments
file_name = sys.argv[1]
scan_type = sys.argv[2]

# Retrieve configurations
api_token = "788cde49ef7bc5505e8190706735c41683df4a7f"
engagement_id = 37

url = "https://demo.defectdojo.org/api/v2/import-scan/"

headers = {
    'Authorization': f'Token {api_token}'
}

data = {
    'active': True,
    'verified': True,
    'scan_type': scan_type,
    'minimum_severity': 'Low',
    'engagement': engagement_id
}

files = {
    'file': open(file_name, 'rb')
}

response = requests.post(url, headers=headers, data=data, files=files)

if response.status_code == 201:
    print(f"Scan results for '{file_name}' imported successfully.")
else:
    print(f"Failed to import scan results ({response.status_code}): {response.text}")
    sys.exit(1)