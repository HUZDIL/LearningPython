

try:
    print(5/0)
except ZeroDivisionError:
    print("you can not divide by zero")

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\n First Number:")
    if first_number == "q":
      break
    second_number = input("\n Second Number:")
    if second_number == "q":
      break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("you can not divide by zero")
    else:
        print(answer)

#file not found error

filename ="alice.txt"

try:
    with open(filename, encoding="utf-8") as f:
         contents = f.read()

except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist")