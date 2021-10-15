

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)


active  = True
while active:
    message = input(prompt)

    if message == "quit":
        active = False
    else:
        print(message)

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")


pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets: #listedeki "cat" bitene kadar bu program calisacaktir.
    pets.remove('cat')
    print(pets)


responses = {}
# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
   #Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
# Store the response in the dictionary.
    responses[name] = response

# Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

#Functions 168