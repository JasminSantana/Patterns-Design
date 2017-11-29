""""Author: Santana Mares Jasmin
    gmail: sant.mar.1997@gmail.com
    date: 11/11/2017   """
'''Permite la construcción de un único proceso capaz de construir distintos objetos complejos,
 abstrayéndonos de los detalles particulares de cada uno.'''

class Director():
    """"Director"""

    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def get_car(self):
        return self._builder.car


class Builder():
    """Abstract Builder"""

    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()


class SkyLarkBuilder(Builder):
    """"Concrete Builder ---> provides and tools to work on the parts"""

    def add_model(self):
        self.car.model = "Skylark"

    def add_tires(self):
        self.car.tires = "Regular tires"

    def add_engine(self):
        self.car.engine = "Turbo engine"


class Car():
    """Product"""

    def __init__(self):
        self.model = None
        self.tires = None
        self.egine = None

    def __str__(self):
        return '{} | {} | {}'.format(self.model, self.tires, self.engine)


builder = SkyLarkBuilder()
director = Director(builder)
director.construct_car()
car = director.get_car()
print(car)
