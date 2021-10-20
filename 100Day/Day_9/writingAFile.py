
#Writing to an Empty File

filename = "programming.txt"
with open(filename , "w") as file_object:
    file_object.write("i love programming. ")
    file_object.write("i love phyton.\n")
    file_object.write("new line started from here. ")


with open(filename ,"a") as file_object:
    file_object.write("i love creating apps than can run in a browser.\n")
    file_object.write("yea")
