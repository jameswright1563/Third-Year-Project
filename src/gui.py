import numpy as np
import PySimpleGUI as sg

import tkinter as tk
# import src.tkintergui
import src.matrices


def gui():
    layout = [
        [sg.Text("Math Solver, please click your category")],
        [sg.Button("Matrices", key="-MATRIX-", enable_events=True)],
        [sg.Button("Vectors", key="vector")]
    ]

    matrixLayout = [
        [sg.Text("Please Select What operation you would like to carry out")],
        [sg.Button("Matrix Inverse", key="-INVERSE-")]
    ]
    dimensionLayout = [
        [sg.InputCombo]
    ]
    inverseLayout = [
        [sg.InputText("", key="-1-", size=(4, 4)), sg.InputText("", key="-2-", size=(4, 4)),
         sg.InputText("", key="-3-", size=(4, 4))],
        [sg.InputText("", key="-4-", size=(4, 4)), sg.InputText("", key="-5-", size=(4, 4)),
         sg.InputText("", key="-6-", size=(4, 4))],
        [sg.InputText("", key="-7-", size=(4, 4)), sg.InputText("", key="-8-", size=(4, 4)),
         sg.InputText("", key="-9-", size=(4, 4))],
        [sg.Button("SOLVE", key="-insub-")]
    ]

    window = sg.Window("Math Solver", layout, size=(1000, 1000))

    while True:
        event, values = window.read()

        if event == "-MATRIX-":
            # src.tkintergui.root()
            window = sg.Window("Matrix Operations", matrixLayout)
        if event == "-INVERSE-":
            # window=sg.Window("Select your dimension")
            window = sg.Window("Matrix Inverser", inverseLayout, size=(1000, 1000))
        if event == "-insub-":
            arr = []
            for x in values.items():
                num = int(x[1])
                arr.append(num)
            print(len(arr))
            result = src.matrices.Matrices().matrixInverse(arr)
            print(result)
            print(arr)

        if event == "OK" or event == sg.WINDOW_CLOSED:
            break

    window.close()


gui()
