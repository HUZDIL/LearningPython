

def get_formatted_name(first_name,last_name):
    full_name = f"{first_name},{last_name}"
    return full_name.title()


musician = get_formatted_name("haci","baba")
print(musician)


def get_formatted_name(first_name, last_name, middle_name =""): #middle name optional
    if middle_name:
        full_name = f"{first_name},{middle_name},{last_name}"
    else:
        full_name = f"{first_name},{last_name}"
    return full_name.title()

musician = get_formatted_name("haci","melik","baba")
print(musician)



def great_names(names):
    for name in names:
        message = f"Hello,{name.title()}"
        print(message)

usernames = ["ali","hakki","hasan"]
great_names(usernames)



unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs: #modeller bitene kadar donus yapar
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)



def print_models(unprinted_designs, completed_models):
 """Simulate printing each design, until none are left."""
 """Move each design to completed_models after printing."""
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

