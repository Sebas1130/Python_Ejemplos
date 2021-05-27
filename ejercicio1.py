from random import randint
from functools import reduce


# Reto 1
class Array:
    def __init__(self, capacity, fill_value=None):
        self.capacity = capacity
        self.items = [fill_value for i in range(self.capacity)]


    # Reto 2
    def __random_fill__(self):
        self.aleatorios = [randint(0, 100) for i in range(self.capacity)]
        
        for i in range(self.capacity):
            self.items[i] = self.aleatorios[i]
        return self.items


    # Reto 3
    def __summation__(self):
        all_sum = reduce(lambda a, b: a + b, self.items)
        return all_sum


if __name__ == '__main__':
    menu = Array(10)
    print(menu.__random_fill__())
    print(menu.__summation__())