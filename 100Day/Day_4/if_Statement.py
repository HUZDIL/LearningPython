

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

age = 18

if age == 18:
    print("your age is OK")


requested_toppings = ["mushrooms","onions","pineapple"]

if "elma" in requested_toppings:
    print("yes")
else:
    print("no")

#Second Way

requested_toppings = ["mushrooms","onions","pineapple"]
pizza = 'onions'

if pizza in requested_toppings:
    print("yes")
else:
    print("no")

print("####################################")

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")


age = 50

if age < 5 :
    print(" your admission cost is 0")
elif age < 18:
    print (" your admission cost is $25")
else:
    print("your admission cost is $50")



requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")



available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")


#Dictionaries












