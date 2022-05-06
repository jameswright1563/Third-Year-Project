import numpy as np
import PySimpleGUI as sg
import src.matrices as mat
from numpy import dot, array, empty_like
from matplotlib import pyplot as plt
from pyrect import Point


def typeCheck(items):
    newDict = {}
    for x in items:
        if items[x] == "":
            newDict[x] = "0"
        else:
            try:
                newDict[x] = float(items[x])
            except ValueError:
                sg.Popup("Please enter a numerical value")
    items = newDict
    return items


def getLineSplit(items):
    items = typeCheck(items)
    # Cofactor matrices for negative items
    eq1 = [-float(items["v1d1i"]), float(items["v2d1i"])]
    eq2 = [-float(items["v1d1j"]), float(items["v2d1j"])]
    eq3 = [float(items["v1d1k"]), -float(items["v2d1k"])]
    lmatrix = np.array([eq1, eq2])
    rmatrix = np.array([float(items["v1p1i"]) - float(items["v2p1i"]), float(items["v1p1j"]) - float(items["v2p1j"])])
    try:
        np.linalg.inv(lmatrix)
    except np.linalg.LinAlgError:
        lmatrix = np.array([eq1, eq2])
        rmatrix = np.array(
            [float(items["v1p1j"]) - float(items["v2p1j"]), float(items["v1p1k"]) - float(items["v2p1k"])])
    Vector().vecLinePlot([float(items["v1p1i"]), float(items["v1p1j"])], [float(items["v1d1i"]), float(items["v1d1j"])])
    t, s = mat.Matrices().simultaneous_equations(lmatrix, rmatrix, 2)
    print("t = ")
    print(t)
    print("s = ")
    print(s)
    print("Sub into Line 1: ")
    x = float(items["v1p1i"]) + (t * float(items["v1d1i"]))
    y = float(items["v1p1j"]) + (t * float(items["v1d1j"]))
    z = float(items["v1p1k"]) + (t * float(items["v1d1k"]))
    return x, y, z


def getVecOpItems(values):
    try:
        v1i = float(values["v1i"])
        v2i = float(values["v2i"])
        v1j = float(values["v1j"])
        v2j = float(values["v2j"])
        v2k = float(values["v2k"])
        v1k = float(values["v2k"])
        v1 = np.array([v1i, v1j, v1k])
        v2 = np.array([v2i, v2j, v2k])
    except KeyError:
        v1i = float(values["v1i"])
        v2i = float(values["v2i"])
        v1j = float(values["v1j"])
        v2j = float(values["v2j"])
        v1 = np.array([v1i, v1j])
        v2 = np.array([v2i, v2j])
    vect = Vector(vector1=v1, vector2=v2)
    return vect


def getPointSplit(items):
    newDict = {}
    for x in items:
        if items[x] == "":
            newDict[x] = "0"
        else:
            try:
                newDict[x] = float(items[x])
            except ValueError:
                sg.Popup("Please enter a numerical value")
    items = newDict
    vector1p1 = [float(items["v1p1i"]), float(items["v1p1j"]), float(items["v1p1k"])]
    vector1p2 = [float(items["v1p2i"]), float(items["v1p2j"]), float(items["v1p2k"])]
    vector2p1 = [float(items["v2p1i"]), float(items["v2p1j"]), float(items["v2p1k"])]
    vector2p2 = [float(items["v2p2i"]), float(items["v2p2j"]), float(items["v2p2k"])]
    return vector1p1, vector1p2, vector2p1, vector2p2


class Vector:
    def __init__(self, vector1=None, vector2=None, scalar=None):
        self.vector1 = np.array(vector1)
        self.vector2 = np.array(vector2)
        self.vectorChoice = None
        self.scalar = scalar

    def getPointIntersection(self, a1, b1, a2=None, b2=None):
        self.vector1 = np.cross(a1, b1)
        self.vector2 = np.cross(a2, b2)
        x, y, z = self.crossProduct()
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

    def vecLinePlot(self, vec1p, vec1d, vec2p=None, vec2d=None):
        plt.rcParams["figure.figsize"] = [7.00, 3.50]
        plt.rcParams["figure.autolayout"] = True
        data = np.array(vec1d)
        origin = np.array(vec1p)
        plt.quiver(*origin, data[0], color=['black'], scale=15)
        plt.show()

    def vectorDistance(self):
        vector_d = self.vector2 - self.vector1
        return self.getMagnitude(vector_d)
