import csv

filename  = "patient_information.csv"

headers = ["name","lastname","username","email","medicaidID"]

info = ["ali","hakan","alihakan","alihakan@gmail.com","234444234"]



with open(filename, mode = "w", newline='') as nf:
        writer =csv.writer(nf)
        writer.writerow((1,headers))
        writer.writerow((2,info))

with open(filename, mode= "r") as file:
        reader = csv.reader(file)
        for row in reader:
                print(row)


