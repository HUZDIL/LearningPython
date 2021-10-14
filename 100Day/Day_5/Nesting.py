
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)


# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range(30):
 new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
 aliens.append(new_alien)
# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
    print("...")
# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")


# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range(30):
 new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
 aliens.append(new_alien)
# Show the first 5 aliens.
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:5]:
    print(alien)
    print("...")
# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")



#dictionary nin icerisine liste koymak
pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}
for topping in pizza['toppings']:
    print("\t" + topping)

#A Dictionary in a Dictionary

users = {
    'aeinstein': {
    'first': 'albert',
    'last': 'einstein',
    'location': 'princeton',
    },
    'mcurie': {
    'first': 'marie',
    'last': 'curie',
    'location': 'paris',
    },
}
for username, user_info in users.items():
    print(f'\nUsername = {username}')
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

 #user input and While loops
