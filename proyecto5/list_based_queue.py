

class ListQueue:
    def __init__(self) -> None:
        self.items = []
        self.size = len(self.items)
    
    def enqueue(self,data):
        self.items.insert(0,data)
        self.size += 1

    def dequeue(self):
        data = self.items.pop()
        self.size -= 1
        return data

    def traverse(self):
        total_item = self.size

        for item in range(total_item):
            print(self.items[item])


"""
importamos en el shell de python el archivo list_based_queue  instanciamos la clase ListQueue
y lo guardamos en lavariable food , despues insertamos datos con la funcion enqueue que definimos
dentro de la clase ListQueue , despueslistamos los datos con la tercera funcion definida dentro 
de la clase, Osea traverse y listamos los elemento , si queremos eliminar un elemento usamos la
funcion definida en la clase valga la redundancia elminamos el primer elemento insertado en lista
osea  'eggs' esto corresponde al modelo FIFO (primero en entrar primero en salir, en inglés 
«First In First Out»): el primer ítem que es añadido a la lista es el primero en ser retornado.


from list_based_queue import ListQueue
food = ListQueue()

food.enqueue('eggs')
food.enqueue('ham')
food.enqueue('spam')

food.traverse()
spam
ham
eggs

food.dequeue()
'eggs'

food.traverse()
spam
ham
 

"""