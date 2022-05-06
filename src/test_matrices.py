import numpy as np
from hamcrest import *

from unittest import TestCase
import src.matrices as mat


class TestMatrices(TestCase):

    """
    3x3 Test Matrix to inverse: [3,0,2,2,0,-2,0,1,1]
    """

    def test_matrix_inverse(self):
        test_arr = np.array([[3, 0, 2], [2, 0, -2], [0, 1, 1]])
        test_result = mat.Matrices().manualInverse(test_arr)
        expected = np.array([[0.2, 0.2, 0], [-0.2, 0.3, 1], [0.2, -0.3, 0]])
        for i in range(0, 3):
            for j in range(0, 3):
                assert_that(test_result[i][j], equal_to(expected[i][j]))

    """
    Testing for a matrix where the determinant is 0 so it cannot be inversed.
    Output data should raise a numpy linalg error
    """

    def test_matrix_inverse2(self):
        test_arr = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        assert_that(calling(mat.Matrices().manualInverse).with_args(test_arr), raises(np.linalg.LinAlgError))

    def test_matrix_split(self):
        test_dict = {0: "1", 1: "1", 2: "1", 3: "1", 4: "1", 5: "1", 6: "1", 7: "1"}
        test_result = mat.Matrices().matrixSplit(test_dict, 2, 2)
        arr = [[0, 0], [0, 0]]
        assert_that(len(test_result[0]), equal_to(2))
        assert_that(type(test_result[0]), equal_to(type(arr)))
        for x in test_result[0]:
            assert_that(x[0], equal_to(1))
            assert_that(x[1], equal_to(1))

    # Testing a 3x2

    def test_matrix_split2(self):
        test_dict = {0: "3", 1: "3", 2: "3", 3: "3", 4: "3", 5: "1", 6: "2", 7: "2", 8: "2", 9: "2", 10: "2", 11: "2"}
        test_result = mat.Matrices().matrixSplit(test_dict, 3, 2)
        arr = [[3, 3, 3], [3, 3, 1]]
        assert_that(len(test_result), equal_to(2))
        assert_that(type(test_result[0]), equal_to(type(arr)))
        assert_that(arr, equal_to(test_result[0]))

    # Testing a 3x2 and 2x3

    def test_matrix_split_mult(self):
        test_dict = {0: "3", 1: "2", 2: "1", 3: "3", 4: "2", 5: "1", 6: "1", 7: "2", 8: "1", 9: "2", 10: "1", 11: "2"}
        test_result = mat.Matrices().matrixSplitMult(test_dict, 3, 2, 2, 3)

    def test_matrix_subtraction(self):
        test_dict = {0: "1", 1: "1", 2: "1", 3: "1", 4: "1", 5: "1", 6: "1", 7: "1"}
        matrices = mat.Matrices().matrixSplit(test_dict, 2, 2)
        test_result = mat.Matrices().matrixSubtraction(matrices[0], matrices[1])
        print(test_result)

    def test_matrix_minors(self):
        test_arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        test_result = mat.Matrices().matrixMinors(test_arr)
        expected = np.array([[-3.0, -6.0, -3.0], [-6.0, -12.0, -6.0], [-3.0, -6.0, -3.0]])
        for i in range(0, 3):
            for j in range(0, 3):
                assert_that(test_result[i][j], equal_to(expected[i][j]))
        print(test_result)

    def test_matrix_cofactors(self):
        test_arr = [[1, -2], [-1, 2]]
        expected = [[1, 2], [1, 2]]
        test_result = mat.Matrices().matrixCofactors(test_arr)
        print(test_result)
        for i in range(0, 2):
            for j in range(0, 2):
                assert_that(test_result[i][j], equal_to(expected[i][j]))

    def test_matrix_cofactors2(self):
        test_arr = np.array([[2, 2, 2], [-2, 3, 3], [0, -10, 0]])
        expected = np.array([[2, -2, 2], [2, 3, -3], [0, 10, 0]])
        test_result = mat.Matrices().matrixCofactors(test_arr)
        print(test_result)
        for i in range(0, 2):
            for j in range(0, 2):
                assert_that(test_result[i][j], equal_to(expected[i][j]))

    def test_matrix_cofactors3(self):
        test_arr = np.array([[-24, -18, 5], [-20, -15, 4], [-5, -4, 1]])
        expected = np.array([[-24, 18, 5], [20, -15, -4], [-5, 4, 1]])
        test_result = mat.Matrices().matrixCofactors(test_arr)
        print(test_result)
        for i in range(0, 2):
            for j in range(0, 2):
                assert_that(test_result[i][j], equal_to(expected[i][j]))

    # Simultaneous t

    def test_simultaneous_equations(self):
        test_arr_left = np.array([[2, 3], [5, 2]])
        test_arr_right = np.array([[13], [16]])
        expected = mat.Matrices().simultaneous_equations(test_arr_left, test_arr_right, 2)
        assert_that(expected[0], equal_to(2))
        assert_that(expected[1], equal_to(3))
        print(expected)

    """
    Simultaneous Equations - Test Data 2:
    2x + 1y + 4z = 17
    3x - 2y = -3
    x + 4y + 5z = 7
    """

    def test_simultaneous_equations2(self):
        test_arr_left = np.array([[2, 1, 4], [3, -2, 0], [1, 4, 5]])
        test_arr_right = np.array([[17], [-3], [7]])
        expected = mat.Matrices().simultaneous_equations(test_arr_left, test_arr_right, 3)
        assert_that(expected[0], equal_to(-7))
        assert_that(expected[1], equal_to(-9))
        assert_that(expected[2], equal_to(10))
        print(expected)

    """
    Simultaneous Equations -Test Data 3: 
    1x + 2y + 3z = 4
    5x + 6y + 7z = 8
    9x + 10y + 11z = 12
    """

    def test_simultaneous_equations3(self):
        test_arr_left = np.array([[1, 2, 3], [5, 6, 7], [9, 10, 11]])
        test_arr_right = np.array([[4], [8], [12]])
        expected = mat.Matrices().simultaneous_equations(test_arr_left, test_arr_right, 3)
        print(expected)
