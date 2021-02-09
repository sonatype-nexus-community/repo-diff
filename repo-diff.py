import json
import logging
import requests
import numpy as np

DEFAULT_HEADERS = {
    'User-Agent': 'iq-momo'}

REPO_HOSTNAME= "http://localhost:8081"
USER = 'username'
TOKEN = 'password'

REPOS = {
    # hosted: proxy
    "python-hosted": "pypi-proxy",
    "npm-hosted": "npm-group-proxy"
}

log = logging.getLogger('repo-diff')

def main():
    logging.basicConfig(filename='repo-diff.log', level=logging.INFO)
    for hosted, proxy in REPOS.items():
        print("-------------------")
        print("Hosted: {0} | Proxy: {1}".format(hosted, proxy))
        hosted_list = get_artifacts(hosted)
        proxy_list = get_artifacts(proxy)
        print(np.intersect1d(hosted_list, proxy_list))


def get_artifacts(repo_name):

    component_list = []

    response = requests.get('{0}/service/rest/v1/search/?sort=name&repository={1}'.format(
       REPO_HOSTNAME, repo_name),
       auth=(USER, TOKEN)
    )

    if response.ok:
        res = json.loads(response.text)
        # print("REPO NAME: {0} - {1}".format(repo_name, res))
        for artifact in res['items']:
            component = "{0}:{1}".format(artifact['group'], artifact['name'])
            component_list.append(component)
    return component_list


if __name__ == '__main__':
    main()


