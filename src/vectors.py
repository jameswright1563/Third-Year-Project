import numpy as np
import PySimpleGUI as sg
import src.matrices as mat


class Vector:

    """
    Class responsible for all vector operations
    """

    def __init__(self, vector1=None, vector2=None, scalar=None):
        self.vector1 = np.array(vector1)
        self.vector2 = np.array(vector2)
        self.vectorChoice = None
        self.scalar = scalar

    # Splits values manually by key checking - Returns vector object

    def getVecOpItems(self, values):
        values = self.typeCheck(values)
        v1i = float(values["v1i"])
        v2i = float(values["v2i"])
        v1j = float(values["v1j"])
        v2j = float(values["v2j"])
        try:
            v2k = float(values["v2k"])
            v1k = float(values["v1k"])
            v1 = np.array([v1i, v1j, v1k])
            v2 = np.array([v2i, v2j, v2k])
        except KeyError:
            v1 = np.array([v1i, v1j])
            v2 = np.array([v2i, v2j])
        vect = Vector(vector1=v1, vector2=v2)
        return vect

    def getPointSplit(self, items):
        unknowns = 0
        try:
            items = self.typeCheck(items)
        except TypeError as ex:
            print(ex)
            sg.Popup("Please enter a numerical value")
        vector1p1 = [float(items["v1p1i"]), float(items["v1p1j"])]
        vector1p2 = [float(items["v1p2i"]), float(items["v1p2j"])]
        vector2p1 = [float(items["v2p1i"]), float(items["v2p1j"])]
        vector2p2 = [float(items["v2p2i"]), float(items["v2p2j"])]
        if items["v1p1k"] + items["v1p2k"] + items["v2p1k"] + items["v2p2k"] == "":
            unknowns = 2
        if unknowns != 2:
            vector1p1.append(float(items["v1p1k"]))
            vector1p2.append(float(items["v1p2k"]))
            vector2p1.append(float(items["v2p1k"]))
            vector2p2.append(float(items["v2p2k"]))
        return vector1p1, vector1p2, vector2p1, vector2p2

    def typeCheck(self, items):
        newDict = {}
        for x in items:
            if items[x] == "":
                newDict[x] = 0
            else:
                try:
                    newDict[x] = float(items[x])
                except ValueError:
                    raise TypeError
        items = newDict
        return items

    def getLineIntersection(self, items):
        items = self.typeCheck(items)

        print("We must organise our variables into matrices and rearrange unknowns to the left hand side.")
        eq1 = [float(items["v1d1i"]), -float(items["v2d1i"])]
        eq2 = [float(items["v1d1j"]), -float(items["v2d1j"])]
        print("eq1=", eq1)
        print("eq2=", eq2)

        if items["v1d1k"] + items["v2d1k"] == "":
            lmatrix = np.array([eq1, eq2])
            rmatrix = np.array(
                [-float(items["v1p1i"]) + float(items["v2p1i"]), float(items["v1p1j"]) + float(items["v2p1j"])])
            try:
                np.linalg.inv(lmatrix)
            except np.linalg.LinAlgError:
                print("No intersections at all, matrix is irreversible, or vectors are parallel.")
                return ""
        else:
            try:
                lmatrix = np.array([eq1, eq2])
                rmatrix = np.array(
                    [-float(items["v1p1i"]) + float(items["v2p1i"]),
                     -float(items["v1p1j"]) + float(items["v2p1j"])])

                np.linalg.inv(lmatrix)
            except np.linalg.LinAlgError:
                print("No intersection for eq1 and eq2, attempting 2 and 3.")
                eq3 = [float(items["v1d1k"]), -float(items["v2d1k"])]
                lmatrix = np.array([eq2, eq3])
                rmatrix = np.array(
                    [-float(items["v1p1j"]) + float(items["v2p1j"]),
                     -float(items["v1p1k"]) + float(items["v2p1k"])])
                try:
                    print("No intersection for eq2 and eq3, attempting 1 and 3.")
                    eq3 = [float(items["v1d1k"]), -float(items["v2d1k"])]
                    lmatrix = np.array([eq1, eq3])
                    rmatrix = np.array(
                        [-float(items["v1p1i"]) + float(items["v2p1i"]),
                         -float(items["v1p1k"]) + float(items["v2p1k"])])
                    np.linalg.inv(lmatrix)
                except np.linalg.LinAlgError:
                    print("No intersections at all, or vectors are parallel.")
                    return ""

        t, s = mat.Matrices().simultaneous_equations(lmatrix, rmatrix, 2)
        print("t = ")
        print(t)
        print("s = ")
        print(s)
        print("Sub into Line 1: ")
        x = round(float(items["v1p1i"]) + (t * float(items["v1d1i"])), 2)
        y = round(float(items["v1p1j"]) + (t * float(items["v1d1j"])), 2)
        z = round(float(items["v1p1k"]) + (t * float(items["v1d1k"])), 2)
        return x, y, z

    def getPointIntersectionForTwo(self, x1, y1, x2, y2, x3, y3, x4, y4):
        D = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if D == 0:
            print(
                "As (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4) is equal to zero, the lines are paralell and do not intersect")
            return "No intersect"

        else:
            px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / (
                    (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
            py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / (
                    (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
            print("""Formulas used:
                    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / (
                                (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
                    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / (
                                (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))""")
            print("px = " + str(px))
            print("py = " + str(py))
            return [px, py]

    def getPointIntersectionForThree(self, a1, b1, a2, b2):
        self.vector1 = np.cross(a1, b1)
        self.vector2 = np.cross(a2, b2)
        print("Vector 1: " + str(self.vector1))
        print("Vector 2: " + str(self.vector2))
        arr = self.crossProduct()
        x = arr[0]
        y = arr[1]
        z = arr[2]
        print("x = ", x)
        print(x)
        print("y = ")
        print(y)
        print("z = ")
        print(z)
        return x, y, z

    # def getLineIntersection(self):

    def addition(self):
        return self.vector1 + self.vector2

    def multiplication(self):
        return self.vector1 * self.vector2

    def subtraction(self):
        return self.vector1 - self.vector2

    def division(self):
        return self.vector1 / self.vector2

    def dotProduct(self):
        return self.vector1.dot(self.vector2)

    def crossProduct(self):
        return np.cross(self.vector1, self.vector2)

    def scalarMult(self, vectorchoice):
        return self.scalar * vectorchoice

    def getMagnitude(self, vector):
        return np.linalg.norm(vector)

    def vectorDistance(self):
        vector_d = self.vector2 - self.vector1
        return round(self.getMagnitude(vector_d), 2)
