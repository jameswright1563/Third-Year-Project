import numpy as np
import PySimpleGUI as sg

import tkinter as tk
# import src.tkintergui
import numpy.linalg

import src.matrices as mat


def createMatrix(cols, rows):
    inverseLayout = []
    for i in range(0, rows):
        curr = []
        for y in range(0, cols):
            curr.append(sg.InputText("", size=(4, 4)))
        inverseLayout.append(curr)
    return inverseLayout


def createInverseLayout(cols, rows):
    inverseLayout = []
    inverseLayout.append(createMatrix(cols, rows))
    inverseLayout.append([sg.Button("Solve", key="-insub-")])
    inverseLayout.append([sg.Output(size=(50, 20))])
    return inverseLayout


def createDetLayout(dim):
    det = [[sg.Text("Matrix")], createMatrix(dim, dim), [sg.Button("Find Determinant", key="-detmat")],
           [sg.Output(size=(50, 50))]]
    return det


def createMultLayout(col1, row1, col2, row2):
    mult = [[sg.Frame("Matrix 1", createMatrix(col1, row1), key="mat1"),
            sg.Frame("Matrix 2: ", createMatrix(col2, row2))],
            [sg.Button("Solve", key="-multmat-")], [sg.Output()]]
    return mult


def createAdditionLayout(cols, rows):
    column1 = createMatrix(cols, rows)
    # column1.insert()
    addLayout = [[sg.Frame("Matrix 1", createMatrix(cols, rows), key="mat1"),
                 sg.Frame("Matrix 2: ", createMatrix(cols, rows))],
                 [sg.Button("Solve", key="-addmat-")], [sg.Output()]]
    return addLayout

def createSubtractionLayout(cols, rows):
    subLayout = [[sg.Frame("Matrix 1", createMatrix(cols, rows), key="mat1"),
                 sg.Frame("Matrix 2: ", createMatrix(cols, rows))],
                 [sg.Button("Solve", key="-submat-")], [sg.Output()]]
    return subLayout


def gui():
    layout = [
        [sg.Text("Math Solver, please click your category")],
        [sg.Button("Matrices", key="-MATRIX-", enable_events=True)],
        [sg.Button("Vectors", key="vector")]
    ]

    matrixLayout = [
        [sg.Text("Please Select What operation you would like to carry out")],
        [sg.Button("Matrix Multiplication", key="-matrixMUL")],
        [sg.Frame("Single 2-Dimension Calculations", [[sg.Button("Transpose/Cofactor Matrix", key="mattran"),
                                                       sg.Text("Columns"), sg.Combo([2, 3, 4, 5], key="trancol"),
                                                       sg.Text("Rows"),
                                                       sg.Combo([2, 3, 4, 5], key="tranrow")],
                                                      [sg.Button("Matrix Addition", key="matrixadd"),
                                                       sg.Text("Columns"),
                                                       sg.Combo([2, 3, 4, 5], key="adddimcol"),sg.Text("Rows"),
                                                       sg.Combo([2, 3, 4, 5], key="adddimrow")],

        [sg.Button("Matrix Subtraction", key="-matrixSUB"),sg.Text("Columns"), sg.Combo([2, 3, 4, 5], key="subdimcol"),sg.Text("Rows"),
                                                       sg.Combo([2, 3, 4, 5], key="subdimrow")]
                  ])],
        [sg.Button("Scalar Multiplication", key="matrixscalar"),
         sg.Text("Scalar Value"), sg.InputText(default_text=0.5, key="scalarmult")
         sg.Text("Columns"),
         sg.Combo([2, 3, 4, 5], key="adddimcol"), sg.Text("Rows"),
         sg.Combo([2, 3, 4, 5], key="adddimrow")]

        [sg.Frame("Single 1-dimension calculations: ", [[sg.Combo([2, 3, 4, 5], default_value=2, key="singledim")],
                                                        [sg.Button("Determinant", key="-matdet")
                                                         ], [sg.Button("Matrix Inverse", key="-INVERSE-")]])]
    ]
    additiondimLayout = [
        [sg.Text("Please select  the dimension of the matrix, First Box is the column, second is the row")],
        [[sg.Combo([2, 3, 4, 5], key="adddimcol")], [sg.Combo([2, 3, 4, 5], key="adddimrow")]],
        [sg.Button("OK", key="-okadddim")]
    ]
    subdimLayout = [
        [sg.Text("Please select  the dimensions of the matrix, First Box is the column, second is the row")],
        [[sg.Combo([2, 3, 4, 5], default_value=2, key="subdimcol")], [sg.Combo([2, 3, 4, 5], default_value=2,
                                                                               key="subdimrow")]],
        [sg.Button("OK", key="-oksubdim")]
    ]
    multdimLayout = [
        [sg.Frame("Matrix 1",
                  [[sg.Text("Please select  the dimensions of the matrix, First Box is the column, second is the row")],
                   [sg.Combo([2, 3, 4, 5], default_value=2, key="matdimcol1")], [sg.Combo([2, 3, 4, 5], default_value=2,
                                                                                          key="matdimrow1")]])],
        [sg.Frame("Matrix 2",
                  [[sg.Text("Please select  the dimensions of the matrix, First Box is the column, second is the row")],
                   [sg.Combo([2, 3, 4, 5], default_value=2, key="matdimcol2")],
                   [sg.Combo([2, 3, 4, 5], default_value=2, key="matdimrow2")]])],
        [sg.Button("OK", key="-okmultdim")]
    ]
    window = sg.Window("Math Solver", layout, size=(200, 200))
    dim = 0
    cols = 0
    rows = 0
    col1 = 0
    col2 = 0,
    row1 = 0
    row2 = 0
    while True:
        event, values = window.read()

        if event == "-MATRIX-":
            # src.tkintergui.root()
            window = sg.Window("Matrix Operations", matrixLayout)
        if event == "-INVERSE-":
            dim = values["singledim"]
            inverseLayout = createInverseLayout(dim, dim)
            window = sg.Window("Matrix Inverse", inverseLayout)
        if event == "-insub-":
            arr = mat.Matrices().singleSplit(values.items(), dim, dim)
            try:
                result = mat.Matrices().manualInverse(np.array(arr))
                print("The result is:")
                print(result)
            except numpy.linalg.LinAlgError:
                print("Matrix is inversible")
        if event == "matrixadd":
            cols = values["adddimcol"]
            rows = values["adddimrow"]
            additionLayout = createAdditionLayout(cols, rows)
            window = sg.Window("Matrix Addition", additionLayout)
        if event == "-addmat-":
            matrices = mat.Matrices().matrixSplit(values.items(), cols, rows)
            result = mat.Matrices().matrixAddition(matrices[0], matrices[1])
            print(result)
        if event == "-matrixSUB":
            cols = values["subdimcol"]
            rows = values["subdimrow"]
            subtractionLayout = createSubtractionLayout(cols, rows)
            window = sg.Window("Matrix Addition", subtractionLayout)
        if event == "-submat-":
            matrices = mat.Matrices().matrixSplit(values.items(), cols, rows)
            result = mat.Matrices().matrixSubtraction(matrices[0], matrices[1])
            sg.Popup(result)
            print(result)
        if event == "-matrixMUL":
            window = sg.Window("Select your dimensions", multdimLayout)
        if event == "-okmultdim":
            col1 = values["matdimcol1"]
            col2 = values["matdimcol2"]
            row1 = values["matdimrow1"]
            row2 = values["matdimrow2"]
            if not mat.Matrices().check_mult_dimension(col1, row2):
                sg.Popup("Try Again! Columns of first Matrix must be equal to rows of second Matrix")
            else:
                window = sg.Window("Matrix multiplication", createMultLayout(col1, row1, col2, row2))
        if event == "-multmat-":
            matrices = mat.Matrices().matrixSplitMult(values.items(), col1, row1, col2, row2)
            result = mat.Matrices().matrixmultiplication(matrices[0], matrices[1])
            print(result)

        if event == "-matdet":
            dim = int(values["singledim"])
            window = sg.Window("Matrix Determinant", createDetLayout(values["singledim"]))
        if event == "-detmat":
            matrix = mat.Matrices().singleSplit(values.items(), dim, dim)
            result = mat.Matrices().matrixDeterminant(matrix)
            print(result)
        if event=="mattran":
            cols = values["trancol"]
            rows=values["tranrow"]
            window=sg.Window("Transpose Matrix",[[sg.Frame("Matrix Input", createMatrix(values["trancol"], values["tranrow"]))], sg.Button("Solve", key="tranok")])
        if event == "tranok":
            matrix = mat.Matrices().singleSplit(values.items(), cols, rows)
            cofactor = mat.Matrices().matrixCofactors(matrix)
            print("Cofactor Matrix")
            print(cofactor)
            print("Transposed matrix")
            print(cofactor.transpose())
        if event == "matrixscalar":
            cols = values
        if event == "OK" or event == sg.WINDOW_CLOSED:
            break

    # window.close()


gui()
