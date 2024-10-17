import requests

def retrieve_user(username):
    api_endpoint = 'https://api.getgrass.io/retrieveUser'
    query_params = {
        'query': {
            'username': username
        }
    }

    response = requests.post(api_endpoint, json=query_params)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Request failed with status code {response.status_code}")

# Prompt the user for the username
username = input("Enter the username to retrieve: ")

# Retrieve user data
user_data = retrieve_user(username)
print(user_data)
