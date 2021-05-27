#PROYECTO 1 Array.py
### Código utilizado para la clase 'Crear un arreglo'.

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

#PROYECTO 2 

### PROYECTO grid.py COMO INICIALIZARLO

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
