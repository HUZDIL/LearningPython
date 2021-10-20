import json

username = input('what is your name : ')
filename = "username.json"
with open(filename, 'w') as f:
    json.dump(username,f)
    print(f"We'll remember you when you come back, {username}!")


filename  = "username.json"
with open(filename) as file:
    username2 = json.load(file)
    print(f"Welcome back")