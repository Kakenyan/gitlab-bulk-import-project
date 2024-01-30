# GitLab Project Importer

This Python script allows you to import GitLab projects from a CSV file using the GitLab API.

## Requirements

- Python 3.x
- `requests` library
- `csv` library
- GitLab private token

## Usage

1. Configure the parsing of command line arguments by providing a private token for GitLab API and the path to the CSV file:

```
parser.add_argument('--token', required=True, help='Private token for GitLab API.')
parser.add_argument('--csv', required=True, help='Path to the CSV file.')
```

2. (Optional) Configure proxy settings if needed:
```
# Proxy Settings
os.environ['http_proxy'] = "http://PROXY_HOST:PROXY_PORT"  
os.environ['https_proxy'] = "https://PROXY_HOST:PROXY_PORT"
```

3. Set up logging to record the import results:
```
# Logging Settings
logging.basicConfig(filename='import_result.log', level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y/%m/%d %H:%M:%S')
```

4. Run the script by providing the required arguments:

```
python import_gitlab.py --token YOUR_PRIVATE_TOKEN --csv PATH_TO_CSV_FILE
```

## CSV File Format

The CSV file should contain the following columns in each row:

- File path of the project export file
- Namespace for the project
- Path for the project

## Import Process

The script does the following steps:

1. Opens the CSV file and reads each row.
2. Loads the project export file.
3. Sends a request to the GitLab API endpoint to upload the export data.
4. Checks the response and logs success or error messages.
5. Waits 12 seconds between requests to avoid hitting API call limits.

## Logging

The script generates a `import_result.log` file to log the status of each import attempt, including success and error messages with timestamps.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---
**Note**: This script is designed to work with GitLab API, ensure you have a valid token and correct CSV file format.
