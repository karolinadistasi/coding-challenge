import requests
import pprint

def get_public_repos(user):
    base_url = 'https://api.github.com'
    user_specs = f'/users/{user}/repos'
    query_string_param = {'type': 'public'}

    response = requests.get(url=base_url+user_specs, params=query_string_param)

    if response.status_code == 200:
        data = response.json()
        # pp = pprint.PrettyPrinter(indent=2)
        # pp.pprint(data)

        print(f'Publicly accessible repositories for user {user}:\n')
        for each in range(len(data)):
            print(data[each]['name'])
        
        print()
     
    else:
        print(f'Status code {response.status_code} received. User does not exist.')

user = input('Enter GitHub user: ')
get_public_repos(user)
