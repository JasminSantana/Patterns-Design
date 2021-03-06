""""Author: Santana Mares Jasmin
    gmail: sant.mar.1997@gmail.com
    date: 11/11/2017   """
'''El patrón Abstract Factory permite crear mediante una interfaz un 
 conjuntos de objetos  que dependen mutuamuente, en este caso se extraen 
 las acciones que pertenecen exclusivamente de cada uno de los animales'''

class Dog:
    """"One of the objects to be returned"""

    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"


class DogFactory:
    """"Concrete Factory"""

    def get_pet(self):
        """"Returnes a Dog object"""
        return Dog()

    def get_food(self):
        """"Returned a Dog Food object"""
        return "Dog Food!"


class PetStore:
    """PetStore houses our Abstract Factory"""

    def __init__(self, pet_factory=None):
        """"pet_factory is our Abstract Factory"""
        self._pet_factory = pet_factory

    def show_pet(self):
        """"Utility method to display the details of the objects returned by the DogFactory"""

        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print("Our pet is '{}!'".format(pet))
        print("Our pet says hello by '{}'".format(pet.speak()))
        print("Its food is '{}'".format(pet_food))


# Create a Concrete Factory
factory = DogFactory()

# Create a pet store housing our Abstract Factory
shop = PetStore(factory)

# Invoke the utility method to show the details of  our pet
shop.show_pet()
