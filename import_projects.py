
import csv
import gitlab
import requests
import os
import logging
import argparse

# Configuring the parsing of command line arguments
parser = argparse.ArgumentParser(description='Import GitLab project from CSV file.')
parser.add_argument('--token', required=True, help='Private token for GitLab API.')
parser.add_argument('--csv', required=True, help='Path to the CSV file.')
args = parser.parse_args()

# Setting up the Proxy 
# os.environ['http_proxy'] = "http://PROXY_HOST:PROXY_PORT"  
# os.environ['https_proxy'] = "https://PROXY_HOST:PROXY_PORT"

# Setting the GitLab host and private token to create an API client
gl = gitlab.Gitlab('https://gitlab.com', private_token=args.token)

# Setting up logging
logging.basicConfig(filename='import_result.log', level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y/%m/%d %H:%M:%S')

# Opening the CSV file and reading each row
with open(args.csv, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        file_path, namespace, path = row  # Reading data from each row of the CSV

        # Loading the export file
        with open(file_path, 'rb') as f:
            data = f.read()

        # Sending a request to the GitLab API endpoint to upload the export data
        url = "https://gitlab.com/api/v4/projects/import"
        headers = {"PRIVATE-TOKEN": args.token}
        payload = {"path": path, "namespace": namespace}
        files = [("file", ("project.tar.gz", data, "application/gzip"))]
        response = requests.post(url, headers=headers, files=files, data=payload)

        # Checking the response and logging
        if response.status_code != 201:
            log_message = f' ERROR - File Path: {file_path}, Status Code: {response.status_code}, Response: {response.text}'
            print(log_message)
            logging.error(log_message)
        else:
            log_message = f' INFO  - File Path: {file_path}, Status Code: {response.status_code}, Created'
            print(log_message)
            logging.info(log_message)
