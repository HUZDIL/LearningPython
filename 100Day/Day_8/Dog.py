class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age): #ne zaman bu siniftan bir instace olustursak bu fonksiyon cagrilacak.
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")


    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")



my_dog = Dog("allie",6) #kopek instance olusturmus olduk
print(f"My dog's name is {my_dog.name}.") #icerisindeki attributelere erismis olduk.
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()

your_dog = Dog("sanet",7)
your_dog.sit()
your_dog.roll_over()

