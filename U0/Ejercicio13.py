#Ejercicio 13: Implementa la clase “Matriz” con los atributos int rows, int columns e int[rows][columns] matrix, que contenga 
#los siguientes métodos: 
#                - getNumberRows(): devuelve el número de filas de la matriz.
#                - getNumberColumns(): devuelve el número de columnas de la matriz.
#                - setElement(int x, int j, int element): cambia el valor de la matriz en [x][j] por el valor de [element].
#                - addMatrix(int[][] matrix): suma todos los elementos de la matriz actual a los elementos de [matrix], y 
#el resultado se almacena en la matriz inicial. Si [matrix] no tiene el mismo número de filas y columnas que la matriz 
#inicial, la operación no se puede realizar (notificalo).
#                - multMatrix(int[][] matrix]: multiplica todos los elementos de la matriz actual a los elementos de [matrix], 
#y el resultado se almacena en la matriz inicial. Si [matrix] no tiene el mismo número de filas y columnas que la matriz 
#inicial, la operación no se puede realizar (notificalo).


class Matriz:
    def __init__(self, rows, columns ):
        self.rows = rows
        self.columns = columns
        self.matrix = [[0] * columns for _ in range(rows)]

    def get_rows(self):
        return self.rows
    
    def get_columns(self):
        return self.columns

    def setElement(self, x, j, element):
        if 0 <= x and 0 <= j :
            self.matrix[x][j] = element
        else:
            print("Índices de matriz fuera de rango.")

    def addMatrix(self, other_matrix):
        if len(other_matrix) != self.rows or len(other_matrix[0]) != self.columns:
            print("No se puede sumar. Tamaños de matriz no coinciden.")
            return
        
        for i in range(self.rows):
            for j in range(self.columns):
                self.matrix[i][j] += other_matrix[i][j]

    def multMatrix(self, other_matrix):
        if len(other_matrix) != self.rows or len(other_matrix[0]) != self.columns:
            print("No se puede multiplicar. Tamaños de matriz no coinciden.")
            return
        
        for i in range(self.rows):
            for j in range(self.columns):
                self.matrix[i][j] *= other_matrix[i][j]