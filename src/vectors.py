import numpy as np


class Vector:
    def __init__(self, vector1, vector2, scalar=None):
        self.vector1 = np.array(vector1)
        self.vector2 = np.array(vector2)
        self.scalar = scalar

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

    def scalarMult(self, vectorchoice):
        return self.scalar * vectorchoice
