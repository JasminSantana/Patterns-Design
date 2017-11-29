""""Author: Santana Mares Jasmin
    gmail: sant.mar.1997@gmail.com
    date: 12/11/2017   """
'''Patron que permite recorrer los elementos de un conjunto sin importar cómo se representen internamente.'''

def count_to(count):
    """Our iterator implementation"""
    """Our list"""
    numbers_in_german = ["eins", "zwei", "drei", "vier", "funf"]

    # Our built in iterator
    # Creates a tuple such as (1, "eins")
    iterator = zip(range(count), numbers_in_german)

    # Iterate through our iterable list
    # Extract the German numbers
    # put them in a generator called number
    for position, number in iterator:
        yield number


for num in count_to(3):
    print("{}".format(num))
