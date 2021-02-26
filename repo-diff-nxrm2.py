import logging
import requests
import numpy as np
from bs4 import BeautifulSoup

REPO_HOSTNAME = "http://localhost:8082"

# Uncomment the correct REPO_PATH for your version or NXRM
REPO_PATH = "nexus/content/repositories"  # REPO 2

# You can use NXRM2 version of the script on NXRM3 by uncommenting the following REPO_PATH
# Using the NXRM2 script for NXRM3 is a workaround to issues when searching against extremely large repos
# REPO_PATH = "service/rest/repository/browse"  # REPO 3

USER = 'username'
TOKEN = 'password'

REPOS = {
    # hosted: proxy
    # "python-hosted": "pypi-proxy",
    "npm-hosted": "npm-proxy"
}

log = logging.getLogger('repo-diff-html')


def main():
    logging.basicConfig(filename='./repo-diff-html.log', level=logging.INFO)
    for hosted, proxy in REPOS.items():
        print("-------------------")
        print("Hosted: {0} | Proxy: {1}".format(hosted, proxy))
        hosted_list = get_page(hosted)
        proxy_list = get_page(proxy)

        print(np.intersect1d(proxy_list, hosted_list))


def get_page(repo):
    component_list = []
    page = requests.get("{0}/{1}/{2}/".format(REPO_HOSTNAME, REPO_PATH, repo), auth=(USER, TOKEN))

    if page.ok:
        soup = BeautifulSoup(page.text, 'html.parser')
        for component in soup.find_all('a'):
            if component.text == "Parent Directory":
                continue
            component_list.append(component.text)

        return component_list


if __name__ == '__main__':
    main()
