import types  # Import the types module

""""Author: Santana Mares Jasmin
    gmail: sant.mar.1997@gmail.com
    date: 12/11/2017   """

'''Determina cómo se debe realizar el intercambio de mensajes entre 
diferentes objetos para resolver una tarea.'''
class Strategy:
    """The Strategy Pattern class"""

    def __init__(self, fuction=None):
        self.name = "Default Strategy"

    def execute(self):
        """The default method that prints the name of the strategy being used"""
        print("{} is used!".format(self.name))


# Replacement method 1
def strategy_one(self):
    print("{} is used to execute method 1".format(self.name))


def strategy_two(self):
    print("{} is used to execute method 2".format(self.name))


s0 = Strategy()
s0.execute()

s1 = Strategy(strategy_one)
s1.name = "Strategy one"
s1.execute()

s2 = Strategy(strategy_two)
s2.name = "Strategy two"
s2.execute()
