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