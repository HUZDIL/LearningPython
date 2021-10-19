class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""

        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""

        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        self.odometer_reading = mileage

    def new_update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can not roll back an odometer")




class ElectricCar(Car):  # inherit
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery_size =75


    def describe_battery(self):
        """Print a statement describing the battery size."""

        print(f"This car has a {self.battery_size}-kWh battery.")





    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""

        print("This car doesn't need a gas tank!")

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


my_car = Car("audi", "a6", 2022)
print(my_car.get_descriptive_name())
my_car.read_odometer()

# Modifying an Attribute’s Value Directly
my_car.odometer_reading = 45
my_car.read_odometer()

# Modifying an Attribute’s Value Through a Method
my_car.update_odometer(333)
my_car.read_odometer()

my_car.new_update_odometer(34)

my_tesla = ElectricCar("tesla", "model s", 2021)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery();
my_tesla.battery_size = 100
my_tesla.describe_battery()

#Overriding Methods from the Parent Class