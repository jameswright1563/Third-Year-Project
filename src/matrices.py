import numpy as np

class Matrices:
    def matrixInverse(self):
        mat = self.matrixInput()
        try:
            np.invert(mat)
        except (np.LinAlgError):
            print("Matrix must be square")
    def matrixmultiplication(self):
        mat1 = self.matrixInput()
        mat2 = self.matrixInput()
        if np.shape(mat1)[1] == np.shape(mat2)[0]:
            result = np.dot(mat1, mat2)
            print("Matrix 1: \n%", result)
        else:
            print("Columns of first matrix must be equal to rows of 2nd matrix")

    def matrixAddition(self):
        mat1 = self.matrixInput()
        mat2 = self.matrixInput()
        result = np.add(mat1, mat2)
        print(result)

    def matrixInput(self):
        R = int(input("Enter the number of rows:"))
        C = int(input("Enter the number of columns:"))

        print("Enter the entries in a single line (separated by space): ")

        # User input of entries in a
        # single line separated by space
        entries = list(map(int, input().split()))

        # For printing the matrix
        matrix = np.array(entries).reshape(R, C)
        print(matrix)
        return matrix


"""Temporary main Method"""

if __name__ == '__main__':
    choice = int(input("Type 1 for matrix muliplication \n2: Matrix Addition"))
    if choice == 1:
        Matrices.matrixmultiplication()
    elif choice == 2:
        Matrices.matrixAddition()
