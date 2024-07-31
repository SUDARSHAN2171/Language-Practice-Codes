import requests
import json
def getinfo(username):
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data: {response.status_code}")
        print(response.json())
        return None
def save(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(filename)
    print(f"Data saved to {filename}")
def main():
    username = input("Enter the GitHub username : ")
    user_info = getinfo(username)
    if user_info:
        filename = f"{username}_info.json"
        save(user_info, filename)
if __name__ == "__main__":
    main()