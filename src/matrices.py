import numpy as np
import math

class Matrices:


    def matrixInverse(self, matrix1):
        mat=np.asmatrix(matrix1)
        shape = int(math.sqrt(len(matrix1)))
        mat.reshape(matrix1, (shape, shape))

        print(mat)
        try:
            mat=np.invert(mat)
        except (np.LinAlgError):
            print("Matrix must be square")
        return mat
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

    def determinant(arr):
        value = arr[0][0] * (arr[1][1] * arr[2][2] - arr[1][2] * arr[2][1])
        value1 = (arr[0][1] * (arr[1][0] * arr[2][2] - arr[1][2] * arr[2][0]))
        value2 = arr[0][2] * (arr[1][0] * arr[2][1] - arr[2][0] * arr[1][1])
        return value - value1 + value2

    def cofactor(self, arr, determinant=None):
        a = arr[1][1] * arr[2][2] - arr[2][1] * arr[1][2]
        b = arr[1][0] * arr[2][2] - arr[2][0] * arr[1][2]
        c = arr[1][0] * arr[2][1] - arr[2][0] * arr[1][1]
        # x
        d = arr[0][0] * arr[2][2] - arr[2][0] * arr[0][2]
        e = arr[0][1] * arr[2][2] - arr[2][1] * arr[0][2]
        f = arr[0][0] * arr[2][1] - arr[2][0] * arr[0][1]
        #
        g = arr[0][1] * arr[1][2] - arr[1][1] * arr[0][2]
        h = arr[0][0] * arr[1][2] - arr[1][0] * arr[0][2]
        i = arr[0][0] * arr[1][1] - arr[1][0] * arr[0][1]

        # print(a,-b,c,"\n",-d,e,-f,"\n",i,-h,g)
        ans = (a, d, g, -b, -e, -h, c, -f, i)
        det = self.determinant(arr)
        # print_inv(ans,det)
        return det, ans







"""Temporary main Method"""

if __name__ == '__main__':
    choice = int(input("Type 1 for matrix muliplication \n2: Matrix Addition"))
    if choice == 1:
        Matrices.matrixmultiplication()
    elif choice == 2:
        Matrices.matrixAddition()
