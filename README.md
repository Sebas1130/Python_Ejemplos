# PROYECTO 1 Array.py

## Código utilizado para la clase 'Crear un arreglo'.

#### Clase de tipo de matriz
##### Métodos:

    Longitud
    Representación de cadenas
    Membresía
    Índice.
    Reemplazo

##### Código utilizado en el shell para crear una matriz.

	$ python3 
##### instancia y métodos

	from array import Array
	menu = Array(5)
	len(menu)
	print(menu)
	for i in range(len(menu)):
    menu[i] = i + 1
	menu[0]
	menu[2]
	for item in menu:
    print(menu)
##### Comandos para ver la longitud y altura de objecto matrix

	menu.__len__()
	menu.__str__()
	menu.__iter__()
	menu.__getitem__(2)
	menu.__setitem__(2, 100)
	menu.__getitem__(2)

# PROYECTO 2 

## PROYECTO grid.py COMO INICIALIZARLO

##### Código utilizado para la clase 'Crear un arreglo de dos dimensiones'Código utilizado para la clase 'Crear un arreglo de dos dimensiones'
### Clase de tipo de cuadrícula
#### Métodos:

      Inicializar
      Obtener altura
      Obtener ancho
      Elemento de acceso
      Representación de cadenas
##### Código utilizado en el shell de Python  para instanciar una cuadrícula
Para inicializar el shell de python se ejecuta el siguiente comando 

	$ python3

##### primero importmos Grid del archivo grid
	from grid import Grid

##### despues le damos valor de 3 ,3  y lo guardamos en una varibale llamada matrix
	matrix = Grid(3, 3)

##### Imprimos aver que contiene la varibale matrix
        print(matrix)
##### despues creamos un ciclo  que crea el rando de el contenido de la avaribale matrix.get_height() osea la altura y con matrix.get_width el  ancho  y que multiplique row * column

        for row in range(matrix.get_height()):
            for column in range(matrix.get_width()):
                matrix[row][column] = row * column

##### por ultimo podemos verificar que contiene el objecto por dentro con los siguientes comandos

        print(matrix) 
        matrix.get_height()
        matrix.get_width()
        matrix.__getitem__()
        matrix.__getitem__(1)
        matrix.__getitem__(2)[0]
        matrix.__str__()
	
# PROYECTO 3

## Lista enlazada lineal simple (singly linked list) – Implementación en Python

![](https://programacionycacharreo.files.wordpress.com/2018/10/singly_linked_list.jpeg)

Una lista enlazada (linked list en inglés), es un tipo de estructura de datos compuesta de nodos. Cada nodo contiene los datos de ese nodo y enlaces a otros nodos.

Se pueden implementar distintos tipos de listas enlazadas. En este post vamos a implementar una lista enlazada lineal simple (singly linked list). En este tipo de listas, cada nodo contiene sus datos y un enlace al siguiente nodo. Además la lista tendrá un método para contar el número de elementos de la lista,un método para insertar un elemento en la lista y un método para eliminar un elemento de la lista.

##### En primer lugar, definimos una clase que va a ser la clase Node. Los objetos de esta contendrán sus propios datos y un enlace al siguiente elemento de la lista:

```javascript
	class Node:
    		def __init__(self, data):
        		self.data = data
        		self.next = None
```
##### A continuación definimos la clase de la lista SinglyLinkedList, que contiene el primer elemento de la lista:
```javascript
	class SinglyLinkedList:
    		def __init__(self, head):
        		self.head = head
```
##### El método que cuenta los elementos de la lista, length(), primero comprueba que la lista no esté vacía, y luego recorre todos los elementos de la lista incrementando un contador por cada elemento. Al final devuelve el contador:
```javascript
	 def length(self):
        	current = self.head
        	if current is not None:
            		count = 1
	
            		while current.next is not None:
                		count += 1
                		current = current.next
            		return count
        	else:
            		return 0
```
##### El siguiente método, insert(datos, posición), inserta un elemento tras la posición indicada. Si se indica la posición 0, el nuevo elemento pasa a ser la cabecera de la lista. En esta implementación, si la posición que se pasa como argumento excede el tamaño de la lista, el elemento se inserta al final:

	    def insert(self, data, position):
        	new_node = Node(data)

        	if position == 0:
            		new_node.next = linked_list.head
            		linked_list.head = new_node
        	else:
            		current = linked_list.head
            		k = 1
            		while current.next is not None and k < position:
                		current = current.next
                		k += 1
            		new_node.next = current.next
            		current.next = new_node

##### El método delete(posición) borra el elemento en la posición pasada como parámetro. Si es el primer elemento la lista de la cabeza pasa a ser el segundo elemento. Si se encuentra el elemento en la lista y se borra devolvemos True, en caso contrario devolvemos False:

```javascript
	def delete(self, position):
        	if position != 1:
            		current = self.head
            		k = 1
            		while current.next is not None and k < position - 1:
                		current = current.next
                		k += 1
            		if current.next is not None:
                		current.next = current.next.next
                		return True
            		else:
                		return False
        	else:
            		self.head = self.head.next
            		return True
```


##### con este código podemos comprobar el funcionamiento de la lista:

### creamos la lista
linked_list = SinglyLinkedList(Node(1))

### rellenamos la lista
for i in range(2,10):
    linked_list.insert(i, i-1)

### insertamos un elemento
linked_list.insert(999,3)

### eliminamos un elemento
linked_list.delete(6)

### mostramos la lista
```javascript
current = linked_list.head
	while current is not None:
    	print(current.data)
    	current = current.next
```

##### Dándonos esta salida por la consola:

1
2
3
999
4
6
7
8
9

