""""Author: Santana Mares Jasmin
    gmail: sant.mar.1997@gmail.com
    date: 11/11/2017   """

''' Solo permite una unica instancia'''


class Borg:
    """Borg class making class attribute global"""
    _shared_state = {}  # Attribute dictionary

    def __init__(self):
        self.__dict__ = self._shared_state  # Make it an attribute dictionary


class Singleton(Borg):  # Inherits from the Borg class
    """This class now shares all its attributes among its various instances"""

    # This essenstially makes the singleton objects an object-oriented global variable

    def __init__(self, **kwargs):
        Borg.__init__(self)
        # Update the attribute dictionary by inserting a new key-value pair
        self._shared_state.update(kwargs)

    def __str__(self):
        # Returns the attribute dictionary for printing
        return str(self._shared_state)


# Let's cr  eate a singleton objects and add first acronym
x = Singleton(HTTP="Hyper Text Transfer Protocol")
# Print the object
print(x)

# Let's create another singleton object and if it refers to the same attribute dictionary
y = Singleton(SNMP="Sinple Network Management Protocol")
# Print the object
print(y)
