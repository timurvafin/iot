import requests
import argparse
import logging
import http.client
import os

# Base URL
BASE_URL = "https://ha.dacha.vafin.ru/api/unifiprotect"

# Setup argument parser
parser = argparse.ArgumentParser(
    description="Script to fetch a file from Home Assistant API"
)
parser.add_argument(
    "endpoint_path", type=str, help="Additional path for the API endpoint"
)
parser.add_argument("token", type=str, help="The long-lived access token")
parser.add_argument("path", type=str, help="The full path to file to save")
parser.add_argument("--debug", action="store_true", help="Enable debug mode")

# Parse arguments
args = parser.parse_args()

# Construct the full API endpoint URL
full_api_endpoint = f"{BASE_URL}/{args.endpoint_path}"

# Enable detailed logging if debug mode is set
if args.debug:
    http.client.HTTPConnection.debuglevel = 1
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True

# Headers for the request
headers = {"Authorization": f"Bearer {args.token}", "Content-Type": "application/json"}

# Perform the request
response = requests.get(full_api_endpoint, headers=headers, stream=True)

# Check if the request was successful
if response.status_code == 200:
    # Save the file
    with open(args.path, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    print(f"File successfully saved as {args.path}")
else:
    print(f"Error in request: {response.status_code}")
