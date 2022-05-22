import math

import numpy as np
from hamcrest import *
from unittest.mock import MagicMock, Mock, patch
from unittest import TestCase
import src.vectors as vec

"""Test data: 4 dictionaries of values expected to"""

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

items3 = {
    "v1p1i": "",
    "v1p1j": "1",
    "v1p1k": "",
    "v1p2i": "4",
    "v1p2j": "5",
    "v1p2k": "",
    "v2p1i": "7",
    "v2p1k": "",
    "v2p1j": "9",
    "v2p2i": "10",
    "v2p2j": "11",
    "v2p2k": "",
}

items4 = {
    "v1p1i": "-2",
    "v1p1j": "8",
    "v1p1k": "8",
    "v2p1i": "1",
    "v2p1j": "0",
    "v2p1k": "7",
    "v2d1i": "1",
    "v2d1j": "-2",
    "v2d1k": "3"
}


class TestVectors(TestCase):
    """
    Test getPointSplit checks an error is raised which produces a popup by using extreme values such as letters.
    It then checks normal values to check the correct vector has been outputted.
    """

    def test_getPointSplit(self):
        with patch('PySimpleGUI.Popup') as mock:
            assert_that(calling(vec.getPointSplit).with_args(items2), raises(TypeError))
            instance = mock.return_value
            instance.return_value = "ok"
        vector1p1, vector1p2, vector2p1, vector2p2 = vec.getPointSplit(items3)
        assert_that(len(vector1p1), equal_to(3))
        vector1p1, vector1p2, vector2p1, vector2p2 = vec.getPointSplit(items)
        expectedv1p1 = [0.0, 1.0, 3.0]
        print(vector1p1)
        assert_that(vector1p1[0], equal_to(expectedv1p1[0]))
        assert_that(vector1p1[1], equal_to(expectedv1p1[1]))
        assert_that(vector1p1[2], equal_to(expectedv1p1[2]))

        return vector1p1, vector1p2, vector2p1, vector2p2

    def test_getPointIntersectionforThree(self):
        vector1p1, vector1p2, vector2p1, vector2p2 = self.test_getPointSplit()
        x, y, z = vec.Vector().getPointIntersectionForThree(vector1p1, vector1p2, vector2p1, vector2p2)
        assert_that(x, equal_to(-172.0))

    def test_getPointIntersectionforTwo(self):
        vector1p1, vector1p2, vector2p1, vector2p2 = vec.getPointSplit(items3)
        px, py = vec.Vector().getPointIntersectionForTwo(vector1p1[0], vector1p1[1], vector1p2[0], vector1p2[1],
                                                         vector2p1[0], vector2p1[1], vector2p2[0], vector2p2[1])
        assert_that(px, equal_to(10.0))
        assert_that(py, equal_to(11.0))
        assert_that(vec.Vector().getPointIntersectionForTwo(0, 0, 0, 0, 0, 0, 0, 0), equal_to("No intersect"))

    def test_getLineIntersection(self):
        with patch('PySimpleGUI.Popup') as mock:
            assert_that(calling(vec.Vector().getLineIntersection).with_args(items2), raises(AttributeError))
            instance = mock.return_value
            instance.return_value = "ok"

        items4["v1d1i"] = "1"
        items4["v1d1j"] = "-3"
        items4["v1d1k"] = "-2"
        x, y, z = vec.Vector().getLineIntersection(items4)
        assert_that(x, equal_to(0.0))
        assert_that(y, equal_to(2.0))
        assert_that(z, equal_to(4.0))
        items4["v1d1i"] = "0"
        items4["v1d1j"] = "0"
        items4["v1d1k"] = ""
        items4["v2d1k"] = ""
        x = vec.Vector().getLineIntersection(items4)
        assert_that(x, equal_to(""))

    def test_vector_distance(self):
        vec1 = np.array([-5, -2, 0])
        vec2 = np.array([6, 0, 3])
        vector = vec.Vector(vector1=vec1, vector2=vec2)
        result = vector.vectorDistance()
        print(result)
        assert_that(result, equal_to(round(math.sqrt(134), 2)))

    def test_vector_distance2(self):
        vec1 = np.array([5, 3, 0])
        vec2 = np.array([2, -2, math.sqrt(2)])
        vector = vec.Vector(vector1=vec1, vector2=vec2)
        result = vector.vectorDistance()
        print(result)
        assert_that(result, equal_to(6))
