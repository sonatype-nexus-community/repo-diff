# Nexus Repository Manager dependency/namespace confusion checker
This repository contains a script to check if you have artifacts containing the same name between your repositories. This can be used to check if you're affected by a [Dependency Confusion Attack](https://blog.sonatype.com/dependency-hijacking-software-supply-chain-attack-hits-more-than-35-organizations)

For example 
````
npm-hosted has packages published with the @mycompany/artifact@2.0.1
npm-proxy has a package called @mycompany/artifact@10.0.1
````

This would be a match.

## Requirements
* Python3
* NXRM3 OSS or PRO
* NXRM2 OSS or PRO

## Instructions

### Step 1: Customise values in repo-diff.py (NXRM3) or repo-diff-nxrm2.py (NXRM2)
You'll need to modify the script to include 
1. Auth creds or tokens from your NXRM. (`USER` and `TOKEN`)
1. URL to your Nexus (`REPO_HOSTNAME`)
1. Repositories to compare in `REPOS`. e.g. to compare ruby and npm hosted to their proxies

```python
REPOS = {
    # hosted: proxy
    "ruby-hosted": "ruby-proxy",
    "npm-hosted": "npm-group-proxy"
}
```
You'll find examples of all in the script.

### Step 2: Create new virtual environment
```python
python3 -m venv my-venv
```
### Step 3: Activate your virtual environment
Do this in your terminal or by using your favorite IDE
#### Windows
```
my-venv\Scripts\activate.bat
```

#### MacOs *NIX Linux
```bash
source my-venv/bin/activate
```

### Step 4: Install dependencies
```python
pip install -r requirements.txt
```

### Step 5: Run script
To run the script simply type - results will be printed out to stdout and can be piped to a file for later use.
```python
 python3 repo-diff.py
 ````

