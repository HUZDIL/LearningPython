

names = ["ali","hakki","sefer"]
for name in names:  #iki nokta ust uste unutulursa syntax hatasi verecektir.
    print(name)    #burada bir satir bosluk birakmak gerekiyor aksi halde print fonksiyon loop icinde gorunmeyecektir.
print("###############")

names = ["ali", "hakki", "sefer"]
for name in names:
    print(f"{name.title()}, that was great")



#RANGE Function

for value in range (1,6):
    print(value)


#numaralari liste seklinde yapmak istiyorsak

value = list(range(1,6))
print(value)


even_numbers = list(range(2,11,2))
print(even_numbers)

odd_numbers = list(range(1,11,2))
print(odd_numbers)


squares = []
for value in range(1, 11):
 square = value ** 2
 squares.append(square)
print(squares)

#Simple Statistics with a List of Numbers

digits = list(range(1,11))
print(min(digits))
print(max(digits))
print(sum(digits))


squares = [value**2 for value in range(1, 11)]
print(squares)


odd_numbers = [value for value in range(1,11,2)]
print (odd_numbers)


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) #0-3 arasni almis oluyoruz
print(players[:3]) #basinda numara yoksa yine sifirdan baslamis oluyor.

#bu yapiyi loop yaparkende kullanabiliriz
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
 print(player.title())


my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] #butun listeyi ayni zamanda friends foodsun icine atmis oluyoruz
print("My friend's favorite foods are:")
print(friend_foods)
friend_foods.append("ice cream")
print(friend_foods)

