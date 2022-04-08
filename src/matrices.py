import numpy as np
import math


class Matrices:

    def __init__(self):
        self.scalar = None

    def singleSplit(self, items, cols, rows):
        mat1 = []
        i = 0
        mat1pos = 1
        curr = []
        for x in items:
            if i < (cols * rows):
                num = int(x[1])
                curr.append(num)
                if mat1pos == cols:
                    # curr.append(num)
                    mat1.append(curr)
                    curr = []
                    mat1pos = 1
                else:
                    mat1pos += 1
        return mat1

    def matrixSplit(self, items, cols, rows):
        mat1 = []
        mat2 = []
        i = 0
        mat1pos = 1
        mat2pos = 1
        curr = []
        curr2 = []
        for x in items:
            if i < (cols * rows):
                num = int(x[1])
                curr.append(num)
                if mat1pos == cols:
                    # curr.append(num)
                    mat1.append(curr)
                    curr = []
                    mat1pos = 1
                else:
                    mat1pos += 1
            else:
                num = int(x[1])
                curr2.append(num)
                if mat2pos == cols:
                    # curr.append(num)
                    mat2.append(curr2)
                    curr2 = []
                    mat2pos = 1
                else:
                    mat2pos += 1
            i += 1
        print(len(mat1))
        print(mat1)
        print(mat2)
        return mat1, mat2

    # Splitting matrices for multiple dimensions

    def matrixSplitMult(self, items, col1, row1, col2, row2):
        mat1 = []
        mat2 = []
        i = 0
        mat1pos = 1
        mat2pos = 1
        curr = []
        curr2 = []
        for x in items:
            if i < (col1 * row1):
                num = int(x[1])
                curr.append(num)
                if mat1pos == col1:
                    # curr.append(num)
                    mat1.append(curr)
                    curr = []
                    mat1pos = 1
                else:
                    mat1pos += 1
            else:
                num = int(x[1])
                curr2.append(num)
                if mat2pos == col2:
                    # curr.append(num)
                    mat2.append(curr2)
                    curr2 = []
                    mat2pos = 1
                else:
                    mat2pos += 1
            i += 1
        print(len(mat1))
        print(mat1)
        print(mat2)
        return mat1, mat2

    def matrixInverse(self, matrix1):
        mat = np.asmatrix(matrix1)
        shape = int(math.sqrt(len(matrix1)))
        #   mat.reshape(mat,(shape, shape))
        mat = np.linalg.inv(mat)
        return mat

    def matrixDeterminant(self, mat):
        return np.linalg.det(mat)

    @staticmethod
    def minor(arr, i, j):
        # ith row, jth column removed
        x=arr
        res= x[np.array(list(range(i)) + list(range(i + 1, x.shape[0])))[:, np.newaxis],
                   np.array(list(range(j)) + list(range(j + 1, x.shape[1])))]
        return res

    def matrixMinors(self, arr):
        new_arr=np.zeros((len(arr),len(arr)))
        for i in range(0,arr.shape[0]):
            for j in range(0,arr.shape[0]):
                det=round(np.linalg.det(Matrices().minor(arr, i, j)))
                new_arr[i][j] = det
        return new_arr

    def matrixCofactors(self,arr):
        negative=False
        new_arr=arr
        for i in range(0,len(arr)):
            for j in range(0,len(arr)):
                if negative:
                    new_arr[i][j]=-arr[i][j]
                    negative =False
                else:
                    if arr[i][j]>=0:
                        negative=True
                    else:
                        new_arr[i][j] = -arr[i][j]
                        negative = True
        return new_arr
    def manualInverse(self, arr):
        det = self.matrixDeterminant(arr)
        print("Determinant: ")
        print(det)
        minors = self.matrixMinors(arr)
        print("Matrix of minors(determinant for each element):")
        print(minors)
        cofactors = self.matrixCofactors(minors)
        print("Apply cofactors:")
        print(cofactors)
        transposed = cofactors.transpose()
        print("Transpose the matrix: ")
        print(transposed)
        print("Now we multiply each element by 1 over the determinant")
        inversed = (1/det)*transposed
        print("Inversed Matrix: ")
        print(inversed)
        return inversed



    def check_mult_dimension(self, col1, row2):
        if col1 == row2:
            return True
        else:
            return False

    def matrixmultiplication(self, mat1, mat2):
        result = np.dot(mat1, mat2)
        return result

    def matrixAddition(self, mat1, mat2):
        result = np.add(mat1, mat2)
        return result

    def matrixSubtraction(self, mat1, mat2):
        result = np.subtract(mat1, mat2)
        return result

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
