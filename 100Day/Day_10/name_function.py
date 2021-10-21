
def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {last}"
    return full_name.title()

print(get_formatted_name("aliea","sanal"))


print("Enter 'q' at any time to quit")
while True:
    first  = input("\n Please enter your name : ")
    if first == "q":
        break
    last = input("\n Please enter your last name : ")
    if last == "q":
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")