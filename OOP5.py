class Car:
    def __init__(self, brand, model, year):
        # Instance variables
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        # Accessing instance variables
        print(f"Car Info: {self.brand} {self.model}, Year: {self.year}")

# Creating an object of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Accessing the instance method
my_car.display_info()

