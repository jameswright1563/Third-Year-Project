import math

import numpy as np
from hamcrest import *

from unittest import TestCase
import src.vectors as vec

items = {
    "v1p1i": "",
    "v1p1j": "1.0",
    "v1p1k": "3",
    "v1p2i": "4",
    "v1p2j": "5",
    "v1p2k": "6",
    "v2p1i": "7",
    "v2p1k": "8",
    "v2p1j": "9",
    "v2p2i": "10",
    "v2p2j": "11",
    "v2p2k": "12",

}
items2 = {
    "v1p1i": "",
    "v1p1j": "a",
    "v1p1k": "3",
    "v1p2i": "4",
    "v1p2j": "5",
    "v1p2k": "6",
    "v2p1i": "7",
    "v2p1k": "8",
    "v2p1j": "9",
    "v2p2i": "10",
    "v2p2j": "11",
    "v2p2k": "12",
}


class TestVectors(TestCase):

    # Testing extreme and normal values
    def test_getPointSplit(self):
        assert_that(calling(vec.getPointSplit).with_args(items2), raises(KeyError))
        vector1p1, vector1p2, vector2p1, vector2p2 = vec.getPointSplit(items)
        expectedv1p1 = [0.0, 2.0, 3.0]
        assert_that(vector1p1[0], equal_to(expectedv1p1[0]))
        return vector1p1, vector1p2, vector2p1, vector2p2

    def test_getPointIntersection(self):
        vector1p1, vector1p2, vector2p1, vector2p2 = self.test_getPointSplit()
        x, y, z = vec.Vector().getPointIntersection(vector1p1, vector1p2, vector2p1, vector2p2)

    def test_getLineIntersection(self):
        items3 = {
            "v1p1i": "-2",
            "v1p1j": "8",
            "v1p1k": "8",
            "v2p1i": "1",
            "v2p1j": "0",
            "v2p1k": "7",
            "v2d1i":"1",
            "v2d1j": "-2",
            "v2d1k": "3"
        }
        items3["v1d1i"]="1"
        items3["v1d1j"]="-3"
        items3["v1d1k"]="-2"

        print(vec.getLineSplit(items3))


    def test_vector_distance(self):
        vec1 = np.array([-5,-2,0])
        vec2 = np.array([6,0,3])
        vector = vec.Vector(vector1=vec1, vector2=vec2)
        result = vector.vectorDistance()
        print(result)
        assert_that(result, equal_to(math.sqrt(134)))

    def test_vector_distance2(self):
        vec1 = np.array([5,3,0])
        vec2 = np.array([2,-2,math.sqrt(2)])
        vector = vec.Vector(vector1=vec1, vector2=vec2)
        result = vector.vectorDistance()
        print(result)
        assert_that(result, equal_to(6))