from car import Car as CR

my_new_car = CR('Acura', 'mdx', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 5555
my_new_car.read_odometer()