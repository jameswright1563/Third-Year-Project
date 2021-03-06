import numpy as np
import PySimpleGUI as sg


class Matrices:

    def __init__(self):
        self.scalar = None

    def truncate(self, n, decimals=0):
        multiplier = 10 ** decimals
        return int(n * multiplier) / multiplier

    def createResultPage(self, result):
        result_str = "Result: \n" + "\n".join(['  '.join(['{:4}'.format(item) for item in row]) for row in result])
        return result_str

    def fillNoneValues(self, items):
        newDict = {}
        try:
            for x in items:
                if items[x] == "":
                    newDict[x] = "0"
                else:
                    newDict[x] = float(items[x])
            return newDict
        except ValueError:
            raise TypeError

    def singleSplit(self, arr, cols, rows):
        arr = self.fillNoneValues(arr)
        result = []
        i = 0
        arrPos = 1
        currentArr = []
        for x in arr.items():
            if i < (cols * rows):
                num = int(x[1])
                currentArr.append(num)
                if arrPos == cols:
                    result.append(currentArr)
                    currentArr = []
                    arrPos = 1
                else:
                    arrPos += 1
        return result

    def matrixSplit(self, items, cols, rows):
        items = self.fillNoneValues(items)

        mat1 = []
        mat2 = []
        i = 0
        mat1pos = 1
        mat2pos = 1
        curr = []
        curr2 = []
        for x in items.items():
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

        return mat1, mat2

    # Splitting matrices for multiple dimensions

    def matrixSplitMult(self, items, col1, row1, col2, row2):
        items = self.fillNoneValues(items)
        mat1 = []
        mat2 = []
        i = 0
        mat1pos = 1
        mat2pos = 1
        curr = []
        curr2 = []
        for x in items.items():
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
        return mat1, mat2

    @staticmethod
    def minor(arr, i, j):
        # ith row, jth column removed
        x = arr
        res = x[np.array(list(range(i)) + list(range(i + 1, x.shape[0])))[:, np.newaxis],
                np.array(list(range(j)) + list(range(j + 1, x.shape[1])))]
        return res

    def matrixMinors(self, arr):
        new_arr = np.zeros((len(arr), len(arr)))
        for i in range(0, arr.shape[0]):
            for j in range(0, arr.shape[0]):
                det = round(np.linalg.det(Matrices().minor(arr, i, j)))
                new_arr[i][j] = det
        return new_arr

    def matrixCofactors(self, arr):
        negative = False
        new_arr = arr
        if not len(arr) == 2:
            for i in range(0, len(arr)):
                for j in range(0, len(arr)):
                    if negative:
                        new_arr[i][j] = -arr[i][j]
                        negative = False
                    else:
                        negative = True
        else:
            new_arr[0][1] = -arr[0][1]
            new_arr[1][0] = -arr[1][0]
        return new_arr

    def simultaneous_equations(self, lmatrix, rmatrix, unknowns):
        x = 0
        y = 0
        z = 0
        print("First we put all elements from the left and right side into seperate matrices")
        print("Left Matrix: ")
        print(lmatrix)
        print("Right Matrix: ")
        print(rmatrix)
        print("Then we inverse the left hand matrix: ")
        if unknowns == 2:
            lmatrixinv = np.linalg.inv(lmatrix)
            print(lmatrixinv)
            print("Then we multiply both sides by the inverse to cancel out the left hand variables: ")
            result = self.matrixmultiplication(lmatrixinv, rmatrix)
            print(result)
            try:
                x = result[0][0]
                y = result[1][0]
            except Exception as e:
                x = result[0]
                y = result[1]
            return x, y
        elif unknowns == 3:
            lmatrixinv = np.linalg.inv(lmatrix)
            print(lmatrixinv)
            print("Then we multiply both sides by the inverse to cancel out the left hand variables: ")
            result = self.matrixmultiplication(lmatrixinv, rmatrix)
            print(result)

            x = round(result[0][0])
            y = round(result[1][0])
            z = round(result[2][0])
            return x, y, z

    def roundArr(self, arr):
        new_arr = arr
        for i in range(0, len(arr[0])):
            for j in range(0, len(arr[1])):
                new_arr[i][j] = self.truncate(arr[i][j], 1)
        return new_arr

    def manualInverse(self, arr):
        det = round(self.matrixDeterminant(arr))
        if det == 0:
            raise np.linalg.LinAlgError
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
        inversed = (1 / det) * transposed
        inversed = self.roundArr(inversed)
        print("Inversed Matrix: ")
        print(inversed)
        return inversed

    def check_inverse(self, matrix):
        if self.matrixDeterminant(matrix) == 0:
            return False
        else:
            return True

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

    def matrixDeterminant(self, mat):
        return np.linalg.det(mat)

    def scalarMult(self, mat, scalar):
        self.scalar = float(scalar)
        return self.scalar * np.array(mat)
