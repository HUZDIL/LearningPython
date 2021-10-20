


with open("pi_digit.txt") as file_object:
    contents = file_object.read()

print(contents)
print(contents.rstrip())

#File Paths

with open("text_files/filename.txt") as file_object:
    contents2 = file_object.read()
print(contents2)

#second way
filepath = 'text_files/filename.txt'
with open(filepath) as file_object2:
    contents3 = file_object2.read()
    print(contents3)

#Reading line by line

filename = 'pi_digit.txt'
with open(filename) as file_object3:
    for line in file_object3:
        print(line)

#second way
with open(filename) as file_object4:
    lines = file_object4.readlines()
for line in lines:
    print(line.rstrip())


with open(filename) as file_object5:
    lines = file_object5.readlines()
pi_string = ''
for line in lines:
    pi_string +=line.rstrip()

print(pi_string)
print(len(pi_string))
