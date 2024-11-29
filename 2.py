class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"The {self.name} says {self.sound}")


class Dog(Animal):
    def __init__(self, name, sound, breed):
        super().__init__(name, sound)
        self.breed = breed

    def speak(self):
        print(f"The {self.breed} dog named {self.name} says {self.sound}")


class Cat(Animal):
    def __init__(self, name, sound, color):
        super().__init__(name, sound)
        self.color = color

    def speak(self):
        print(f"The {self.color} cat named {self.name} says {self.sound}")


# Creating instances of Dog and Cat
dog = Dog("Rex", "woof", "Golden Retriever")
cat = Cat("Whiskers", "meow", "black")

# Calling the speak method on both objects
dog.speak()
cat.speak()