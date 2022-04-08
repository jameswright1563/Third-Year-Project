import numpy as np
from hamcrest import *

from unittest import TestCase
import src.matrices as mat
class TestMatrices(TestCase):
    def test_matrix_subtraction(self):
        self.fail()

    def test_matrix_split(self):
        test_dict = {0: "1", 1: "1", 2: "1", 3: "1", 4: "1", 5: "1", 6: "1", 7: "1"}
        test_result=mat.Matrices().matrixSplit(test_dict.items(), 2, 2)
        arr=[[0,0],[0,0]]
        assert_that(len(test_result[0]), equal_to(2))
        assert_that(type(test_result[0]), equal_to(type(arr)))
        for x in test_result[0]:
            assert_that(x[0], equal_to(1))
            assert_that(x[1], equal_to(1))
    #Testing a 3x2

    def test_matrix_split2(self):
        test_dict = {0: "3", 1: "3", 2: "3", 3: "3", 4: "3", 5: "1", 6: "2", 7: "2", 8:"2",9:"2",10:"2",11:"2"}
        test_result=mat.Matrices().matrixSplit(test_dict.items(), 3, 2)
        arr=[[3,3,3],[3,3,1]]
        assert_that(len(test_result), equal_to(2))
        assert_that(type(test_result[0]), equal_to(type(arr)))
        assert_that(arr, equal_to(test_result[0]))

    #Testing a 3x2 and 2x3

    def test_matrix_split_mult(self):
        test_dict = {0: "3", 1: "2", 2: "1", 3: "3", 4: "2", 5: "1", 6: "1", 7: "2", 8:"1",9:"2",10:"1",11:"2"}
        test_result = mat.Matrices().matrixSplitMult(test_dict.items(),3,2,2,3)

    def test_matrix_subtraction(self):
        test_dict = {0: "1", 1: "1", 2: "1", 3: "1", 4: "1", 5: "1", 6: "1", 7: "1"}
        matrices=mat.Matrices().matrixSplit(test_dict.items(),2,2)
        test_result = mat.Matrices().matrixSubtraction(matrices[0], matrices[1])
        print(test_result)

    def test_matrix_minors(self):
        test_arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
        test_result = mat.Matrices().matrixMinors(test_arr)
        expected = np.array([[-3.0,-6.0,-3.0],[-6.0, -12.0,-6.0],[-3.0,-6.0,-3.0]])
        for i in range(0,3):
            for j in range(0,3):
                assert_that(test_result[i][j],equal_to(expected[i][j]))
        print(test_result)

    def test_matrix_cofactors(self):
        test_arr = [[1,-2],[-1,2]]
        expected = [[-1,2],[1,-2]]
        test_result = mat.Matrices().matrixCofactors(test_arr)
        assert_that(expected, equal_to(test_arr))

    def test_manual_inverse(self):
        test_arr=np.array([[3,0,2],[2,0,-2],[0,1,1]])
        test_result = mat.Matrices().manualInverse(test_arr)
        print(test_result)