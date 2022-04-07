import numpy as np
import PySimpleGUI as sg

import tkinter as tk
# import src.tkintergui
import numpy.linalg

import src.matrices

[sg.InputText("", key="-1-", size=(4, 4)), sg.InputText("", key="-2-", size=(4, 4)),
 sg.InputText("", key="-3-", size=(4, 4))],
[sg.InputText("", key="-4-", size=(4, 4)), sg.InputText("", key="-5-", size=(4, 4)),
 sg.InputText("", key="-6-", size=(4, 4))],
[sg.InputText("", key="-7-", size=(4, 4)), sg.InputText("", key="-8-", size=(4, 4)),
 sg.InputText("", key="-9-", size=(4, 4))],

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
    for i in range(0, rows):
        curr = []
        for y in range(0, cols):
            curr.append(sg.InputText("", size=(4, 4)))
        inverseLayout.append(curr)
    inverseLayout.append([sg.Button("Solve", key="-insub-")])
    inverseLayout.append([sg.Output()])
    return inverseLayout


def createAdditionLayout(cols, rows):
    column1=createMatrix(cols, rows)
    #column1.insert()
    addLayout = [[sg.Frame("Matrix 1", createMatrix(cols, rows), key="mat1")],[sg.Frame("Matrix 2: ",createMatrix(cols, rows))],
                 [sg.Button("Solve", key="-addmat-")], [sg.Output()]]
    return addLayout

def gui():
    layout = [
        [sg.Text("Math Solver, please click your category")],
        [sg.Button("Matrices", key="-MATRIX-", enable_events=True)],
        [sg.Button("Vectors", key="vector")]
    ]

    matrixLayout = [
        [sg.Text("Please Select What operation you would like to carry out")],
        [sg.Button("Matrix Inverse", key="-INVERSE-")], [sg.Button("Matrix Addition", key="matrixadd")]
    ]
    dimensionLayout = [
        [sg.Text("Please select how many the dimension of the matrix")],
        [sg.Combo([2, 3, 4, 5], key="invdim")], [sg.Button("OK", key="-okinvdim")]
    ]
    additiondimLayout = [
        [sg.Text("Please select  the dimension of the matrix, First Box is the column, second is the row")],
        [[sg.Combo([2, 3, 4, 5], key="adddimcol")], [sg.Combo([2, 3, 4, 5], key="adddimrow")]],
        [sg.Button("OK", key="-okadddim")]
    ]
    resultLayout = [[sg.Text("Result"), sg.Output()]]
    inverseLayout = None
    additionLayout = None
    window = sg.Window("Math Solver", layout, size=(1000, 1000))
    dim = 0
    cols = 0
    rows = 0
    ad=None
    while True:
        event, values = window.read()

        if event == "-MATRIX-":
            # src.tkintergui.root()
            window = sg.Window("Matrix Operations", matrixLayout)
        if event == "-INVERSE-":
            window = sg.Window("Select your dimension", dimensionLayout)
        if event == "-okinvdim":
            dim = values["invdim"]
            inverseLayout = createInverseLayout(dim, dim)
            window.close()
            window = sg.Window("Matrix Inverser", inverseLayout, size=(1000, 1000))
        if event == "-insub-":
            arr = []
            i = 0
            curr = []
            for x in values.items():
                num = int(x[1])
                if i == dim:
                    arr.append(curr)
                    curr = []
                curr.append(num)
                i += 1
            arr.append(curr)
            try:
                result = src.matrices.Matrices().matrixInverse(arr)
                print("The result is:")
                print(result)
            except numpy.linalg.LinAlgError:
                print("Matrix is inversible")

        if event == "matrixadd":
            window = sg.Window("Select your dimension", additiondimLayout)
        if event == "-okadddim":
            cols = values["adddimcol"]
            rows = values["adddimrow"]
            additionLayout = createAdditionLayout(cols, rows)
            window = sg.Window("Matrix Addition", additionLayout)

        if event =="-addmat-":
            length = 0
            mat1 = []
            mat2=[]
            i = 0
            i2=0
            curr = []
            curr2=[]
            for x in values.items():
                if i<=cols*rows:
                    num = int(x[1])
                    try:
                        if i % cols==0 and i!=0:
                            mat1.append(curr)
                            curr = []
                        curr.append(num)
                    except ZeroDivisionError:
                        curr.append(num)
                else:
                    num = int(x[1])
                    try:
                        if i2 % cols == 0 and i2 != 0:
                            mat2.append(curr)
                            curr2 = []
                        curr2.append(num)
                    except ZeroDivisionError:
                        curr2.append(num)
                    i2+=1
                length+=1
                i += 1
            result = src.matrices.Matrices().matrixAddition(mat1, mat2)
            print(result)


        if event == "OK" or event == sg.WINDOW_CLOSED:
            break

    # window.close()


gui()
