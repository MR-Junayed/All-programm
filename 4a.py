class Car:
    def __init__(self, make, model):
        """Initialize the Car instance with make and model."""
        self.make = make
        self.model = model

    def display_info(self):
        """Prints the car's make and model."""
        print(f"Car Make: {self.make}, Model: {self.model}")

# Create an instance of the Car class
my_car = Car("Toyota", "Corolla")

# Access the attributes
print("Make:", my_car.make)  # Output: Toyota
print("Model:", my_car.model)  # Output: Corolla

# Call the display_info method
my_car.display_info()  # Output: Car Make: Toyota, Model: Corolla