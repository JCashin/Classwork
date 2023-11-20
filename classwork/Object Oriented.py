from ipaddress import _BaseNetwork


class Dog():
    def __init__(self, name="no name", age=0, breed="no breed", gender="no gender"):
        self.name = name 
        self.age = age 
        self.breed = breed 
        self.gender = gender 

    def speak(self):
        print("My Dog's name is: ",self.name)

Bobby = Dog("Bobby", 5, "Beagle", "Male")
Pip = Dog("Pip", 7, "Beagle", "Female")
print(Bobby.name)
print(Bobby.age)
print(Bobby.breed)
print(Bobby.gender)
Bobby.speak()
print("\n")
print(Pip.name)
print(Pip.age)
print(Pip.breed)
print(Pip.gender)
Pip.speak()