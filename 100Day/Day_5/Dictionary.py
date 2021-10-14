
alien_0 = {'color': 'green', 'points': 5}  #Key - value seklinde yaziliyor
print(alien_0['color'])
print(alien_0['points'])


alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

alien_0 = {'color': 'green', 'points': 5}
alien_0["color"] = "yellow"   #modifiying the value
print(alien_0)

print("#################################################################")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print(f"Original position: {alien_0['x_position']}")
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
# This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

#Get Metodu
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value) #point icin atanmis bir deger olmadigindan hata almamizi engellemis oluyor.

print("#################################################################")


#loopp  ile key - value degerine ulasmak

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for key,value in favorite_languages.items(): #key ve value yerine baska adlandirma yapilabilir.
    print(f"\nKey = {key}")
    print(f"\nValue = {value}")
for name in favorite_languages.keys():
    print (name.title())


favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
if "haci" not in favorite_languages.keys():
    print("Haci ismi listede yok")
for name in sorted(favorite_languages.keys()): #isimleri siralanmis sekilde aliyoruz
    print(f"{name.title()}, thank you for taking the poll.")

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'c',
'phil': 'python',
}
for language in set(favorite_languages.values()): #set metodu sadece uniqe degerleri gostemis oluyor
    print(language.title()) # result python and C olacaktir











