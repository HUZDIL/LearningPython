

names =["haci", 'ahmet', "ali"];
print(names);

print(names[1]);     #it should be return "ahmet"

print(names[0].title()); #it should be return "Haci" yani bas harf buyuk yapiyor

names[0] = "mamadu";
print(names);

names.append("haci");
print(names);

print("====================")
names.insert(0,"haci");
print(names);


del names[0];
print(names);


popped_names = names.pop();
print(names);
print(popped_names);
print("====================")
names.pop();
print(names);
names.append("haci");
print(names);

names.remove("mamadu");
print(names);

#organizin a list

names.append('namik');
names.insert(0,"ali");
names.append("mahmut");
print("====================")
print(names);
names.sort();
print(names);
names.sort(reverse=true);
print(names);

names.reverse();
print(names);



#Working with list page 87






