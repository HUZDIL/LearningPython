

def great_user():
    """Display a simple greeting"""
    print("Hello")

great_user()


def great_user(username):  #bir string deger girmemiz gerekiyor fonksiyounun calismasi icin.
    print(f"Hello, {username.title()}!")

great_user("haci")



def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet("dog","valerin")
describe_pet("hamster","willie")
describe_pet("cat","aliya")


def describe_new_pet(pet_name , animal_type ='dog'): #butun hayvanlar eger dog ise bunu bastan tanimlayabiliriz
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_new_pet("willie")

describe_new_pet("willie" , "cat") #istersek kendimiz buraya deger atayabiliyoruz




