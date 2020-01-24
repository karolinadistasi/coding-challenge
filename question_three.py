import requests
import pprint

def get_public_repos(user):
    base_url = 'https://api.github.com'
    user_specs = f'/users/{user}/repos'
    query_string_param = {'type': 'public'}

    response = requests.get(url = base_url + user_specs, params = query_string_param)

    data = response.json()
    # pp = pprint.PrettyPrinter(indent=2)
    # pp.pprint(data)

    repo_names = []
    for each in range(len(data)):
        repo_names.append(data[each]['name'])

    print(repo_names)
