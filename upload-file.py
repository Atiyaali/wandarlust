import os
import sys
import requests

# Retrieve command line arguments
if len(sys.argv) < 3:
    print("Usage: python upload-file.py <file_name> <scan_type>")
    sys.exit(1)

file_name = sys.argv[1]
scan_type = sys.argv[2]

# Retrieve configurations from environment variables
api_token = os.environ.get("DEFECTDOJO_TOKEN", "788cde49ef7bc5505e8190706735c41683df4a7f")
engagement_id = os.environ.get("DEFECTDOJO_ENGAGEMENT_ID", "37")
url = os.environ.get("DEFECTDOJO_URL", "https://demo.defectdojo.org/api/v2/import-scan/")

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

try:
    with open(file_name, 'rb') as f:
        files = {'file': f}
        # Connection timeout: 10 seconds, Read timeout: 60 seconds
        response = requests.post(url, headers=headers, data=data, files=files, timeout=(10, 60))

    if response.status_code == 201:
        print(f"Scan results for '{file_name}' imported successfully.")
    else:
        print(f"Failed to import scan results ({response.status_code}): {response.text}")
        sys.exit(1)

except requests.exceptions.ConnectTimeout:
    print(f"Error: Connection timed out attempting to reach {url}.")
    print("GitHub Actions runner IPs are likely blocked by demo.defectdojo.org or the host is down.")
    sys.exit(1)
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
    sys.exit(1)