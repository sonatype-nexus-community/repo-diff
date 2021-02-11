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
    "ruby-hosted": "ruby-proxy",
    "npm-hosted": "npm-proxy"
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
    continuation_token =""

    baseurl = (
        f"{REPO_HOSTNAME}/service/rest/v1/search/?sort=name&repository={repo_name}"
    )

    while continuation_token is not None:
        url = baseurl
        if continuation_token:
            url += f"&continuationToken={continuation_token}"
        response = requests.get(url, auth=(USER, TOKEN))
        response.raise_for_status()

        if response.ok:
            res = json.loads(response.text)
            for artifact in res['items']:
                component = "{0}:{1}".format(artifact['group'], artifact['name'])
                component_list.append(component)
        
        continuation_token = res["continuationToken"]
    
    return component_list

if __name__ == '__main__':
    main()


