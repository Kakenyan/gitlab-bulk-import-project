# GitLab Project CSV Importer

GitLab Project Importer is a Python script for importing GitLab projects from a CSV file.

### Features

- Import project information from CSV file
- Import projects using GitLab API
- Log output of import results

### Requirements

- Python 3.6 or higher
- Required Python libraries: csv, gitlab, requests, logging, argparse, os, datetime 

### Installation

GitLab Project Importer does not require special installation. Simply clone the repository and use it directly.

```bash
git clone https://github.com/kakenyan/gitlab-project-csv-importer.git
cd gitlab-project-importer
```

Before running the script, you need to install some dependencies. You can use the following pip command:

```bash
pip3 install python-gitlab requests
```

### Usage

The script is operated from the command line. It requires a private token for GitLab API and path to a CSV file with information about the projects to be imported.

```bash
python import_projects.py --token your_token --csv path_to_your_csv_file.csv
```

### CSV File Format

The CSV file needs to contain the file_path, namespace, and path for each project. Please structure your data in the following format:

```
file_path,namespace,path
/path/to/your/project.tar.gz,your_namespace,your_project_path
```

### Log Output

The result of the project import is logged and output in a file named 'import_result.log'. Each log entry is prefixed with a timestamp.

### License

MIT License

---

Please feel free to provide feedback if you encounter any issues! Use it at your own risk.
