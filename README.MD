# Nexus Repository Manager coordinate diff script
This repository contains a script to check if you have artifacts containing the same name between your repositories. 

For example 
````
npm-hosted has packages published with the @mycompany/artifact@2.0.1
npm-proxy has a package called @mycompany/artifact2@10.0.1
````

This would be a match.

## Requirements
* Python3
* NXRM3 OSS or PRO

## Instructions

### 0 - Customise values
You'll need to modify the script to include 
1. Auth creds or tokens from your NXRM3.
1. URL to your Nexus
1. Repositories to compare in REPOS. e.g. to compare ruby and npm hosted to their proxies

```python
REPOS = {
    # hosted: proxy
    "ruby-hosted": "ruby-proxy",
    "npm-hosted": "npm-group-proxy"
}
```

### 1 - Create new virtual environment
```python
python3 -m venv my-venv
```
### 2 - Activate your virtual environment
Do this in your terminal or by using your favorite IDE
#### Windows
```
my-venv\Scripts\activate.bat
```

#### MacOs *NIX Linux
```bash
source my-venv/bin/activate
```

### 3 - Install dependencies
```python
pip install -r requirements.txt
```

### 4 - Run script
To run the script simply type - results will be printed out to stout and can be piped to a file for later use.
```python
 python3 repo-diff.py
 ````

