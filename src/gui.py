import numpy as np
import PySimpleGUI as sg
import src.matrices as mat
import src.vectors as vec
import PySimpleGUI as sg
import copy


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
    return sg.Window("Matrix Inverse", inverseLayout)


def createDetLayout(dim):
    det = [[sg.Text("Matrix")], createMatrix(dim, dim), [sg.Button("Find Determinant", key="-detmat")],
           [sg.Output(size=(10, 5))]]
    return det


def createMultLayout(col1, row1, col2, row2):
    mult = [[sg.Frame("Matrix 1", createMatrix(col1, row1), key="mat1"),
             sg.Frame("Matrix 2: ", createMatrix(col2, row2))],
            [sg.Button("Solve", key="-multmat-")], [sg.Output()]]
    return sg.Window("Matrix Multiplication", mult)


def createAdditionLayout(cols, rows):
    addLayout = [[sg.Frame("Matrix 1", createMatrix(cols, rows), key="mat1"),
                  sg.Frame("Matrix 2: ", createMatrix(cols, rows))],
                 [sg.Button("Solve", key="-addmat-")], [sg.Output()]]
    return sg.Window("Matrix Addition", addLayout)


def createSubtractionLayout(cols, rows):
    subLayout = [[sg.Frame("Matrix 1", createMatrix(cols, rows), key="mat1"),
                  sg.Frame("Matrix 2: ", createMatrix(cols, rows))],
                 [sg.Button("Solve", key="-submat-")], [sg.Output()]]
    return sg.Window("Matrix Subtraction", subLayout)


def createIntersectLineLayout():
    lineLayout = [[sg.Frame("Line 1:", [[sg.Text("r = ("), sg.Column([[sg.InputText("", key="v1p1i", size=(5, 10))],
                                                                      [sg.InputText("", key="v1p1j", size=(5, 10))],
                                                                      [sg.InputText("", key="v1p1k", size=(5, 10))]]),
                                         sg.Text(") + t("),
                                         sg.Column([[sg.InputText("", key="v1d1i", size=(5, 10))],
                                                    [sg.InputText("", key="v1d1j", size=(5, 10))],
                                                    [sg.InputText("", key="v1d1k", size=(5, 10))]]), sg.Text(")")]])],
                  [sg.Frame("Line 2:", [[sg.Text("r = ("), sg.Column([[sg.InputText("", key="v2p1i", size=(5, 10))],
                                                                      [sg.InputText("", key="v2p1j", size=(5, 10))],
                                                                      [sg.InputText("", key="v2p1k", size=(5, 10))]]),
                                         sg.Text(") + s("),
                                         sg.Column([[sg.InputText("", key="v2d1i", size=(5, 10))],
                                                    [sg.InputText("", key="v2d1j", size=(5, 10))],
                                                    [sg.InputText("", key="v2d1k", size=(5, 10))]]), sg.Text(")")]])
                   ], [sg.Button("Solve", key="lineintersectsolve")], [sg.Output()]]
    return sg.Window("Intersection of Line", lineLayout)


def createIntersectionPointsLayout():
    layout = [
        [sg.Frame("Line 1: ", [[sg.Frame("Point 1: ", [[sg.InputText("", key="v1p1i", size=(10, 10)), sg.Text("i + "),
                                                        sg.InputText("", key="v1p1j", size=(10, 10)), sg.Text("j + "),
                                                        sg.InputText("", key="v1p1k", size=(10, 10)), sg.Text("k")]])],
                               [sg.Frame("Point 2: ", [[sg.InputText("", key="v1p2i", size=(10, 10)), sg.Text("i + "),
                                                        sg.InputText("", key="v1p2j", size=(10, 10)), sg.Text("j + "),
                                                        sg.InputText("", key="v1p2k", size=(10, 10)),
                                                        sg.Text("k")]])]])],
        [sg.Frame("Line 2: ",
                  [[sg.Frame("Point 1: ", [[sg.InputText("", key="v2p1i", size=(10, 10)), sg.Text("i + "),
                                            sg.InputText("", key="v2p1j", size=(10, 10)), sg.Text("j + "),
                                            sg.InputText("", key="v2p1k", size=(10, 10)), sg.Text("k")]])],
                   [sg.Frame("Point 2: ", [[sg.InputText("", key="v2p2i", size=(10, 10)), sg.Text("i + "),
                                            sg.InputText("", key="v2p2j", size=(10, 10)), sg.Text("j + "),
                                            sg.InputText("", key="v2p2k", size=(10, 10)), sg.Text("k")]])]])],
        [sg.Button("Find Point of Intersection", key="solveintersectpoint")], [sg.Output()]
    ]
    return layout


def createSimultaneousLayout(unknowns):
    layout = []
    for i in range(1, unknowns + 1):
        equ_str = "Equation" + str(i)
        if unknowns == 3:
            layout.append([sg.Frame("Equation " + str(i), [
                [sg.InputText("", key=equ_str + "x", size=(10, 10)), sg.Text("x + "),
                 sg.InputText("", key=equ_str + "y", size=(10, 10)), sg.Text("y + "),
                 sg.InputText("", key=equ_str + "z", size=(10, 10)), sg.Text("z= + "),
                 sg.InputText("", key=equ_str + "ans", size=(10, 10))]])])
        elif unknowns == 2:
            layout.append([sg.Frame("Equation " + str(i), [
                [sg.InputText("", key=equ_str + "x", size=(10, 10)), sg.Text("x + "),
                 sg.InputText("", key=equ_str + "y", size=(10, 10)), sg.Text("y = "),
                 sg.InputText("", key=equ_str + "ans", size=(10, 10))]])])
    layout.append([sg.Button("Solve", key="simultsolve")])
    layout.append([sg.Output(size=(50, 50))])

    return layout


def linAlgError():
    sg.Popup("Matrix is irreversible. This occurs when the determinant is 0")


def createStringResult(result):
    str_result = ""
    for line in result:
        print('  '.join(map(str, line)))
        str_result = " ".join((map(str, line)))
    str_result = "Result: " + str_result
    return str_result


def createLayout():
    layout = []
    layout.append([
        [sg.Text("Math Solver, please click your category")],
        [sg.Button("Matrices", key="-MATRIX-", enable_events=True)],
        [sg.Button("Vectors", key="vector")], [sg.Frame("Simultaneous Equations", [[
            sg.Button("Simultaneous Equations", key="simult"), sg.Text("Number of Unknowns"),
            sg.Combo([2, 3], default_value=2, key="unknowns")]])],
        [sg.Listbox(values=sg.theme_list(),size=(20, 12),
                      key='-LIST-',
                      enable_events=True)],
          [sg.Button('Exit')]
    ])
    return layout


def createVectorLayout():
    vectorLayout = [[sg.Frame("Intersection of lines", [[sg.Button("Given Two Points", key="intersectpoints"),
                                                         sg.Button("Given Two Equations", key="intersectequations")]])],
                    [sg.Frame("",
                    [[sg.Button("Vector Addition / Subtraction", key="vecadd"), sg.Text("Dimension of Vector"),
                     sg.Combo([2, 3], key="vecadddim", default_value=2)],[sg.Button("Distance between two vectors", key="vecdist")],[
                        sg.Button("Dot/Cross Product", key="vecdot")]
                    ])]]
    i = copy.deepcopy(vectorLayout)
    del vectorLayout
    return sg.Window("Vector Operations", i, size=(600, 600))


def createVectorDotLayout(dimension):
    layout = []
    if dimension == 2:
        layout.append([sg.Text("("), sg.Column([[sg.InputText("", size=(5, 10), key="v1i")],
                                                [sg.InputText("", size=(5, 10), key="v1j")]]), sg.Text(")"),
                       sg.Combo(["Cross", "Dot"], key="vecop"), sg.Text("("),
                       sg.Column([[sg.InputText("", size=(5, 10), key="v2i")],
                                  [sg.InputText("", size=(5, 10), key="v2j")]]), sg.Text(")"),
                       [sg.Button("Solve", key="vecdotsolve")]])
    elif dimension == 3:
        layout.append([sg.Text("("), sg.Column([[sg.InputText("", size=(5, 10), key="v1i")],
                                                [sg.InputText("", size=(5, 10), key="v1j")],
                                                [sg.InputText("", size=(5, 10), key="v1k")]]), sg.Text(")"),
                       sg.Combo(["Cross", "Dot"], key="vecop"), sg.Text("("),
                       sg.Column([[sg.InputText("", size=(5, 10), key="v2i")],
                                  [sg.InputText("", size=(5, 10), key="v2j")],
                                  [sg.InputText("", size=(5, 10), key="v2k")]]), sg.Text(")"),
                       sg.Button("Solve", key="vecdotsolve")])
    return sg.Window("Vector Dot/Cross Product", layout)

def createVectorAdditionLayout(dimension):
    layout = []
    if dimension == 2:
        layout.append([sg.Text("("), sg.Column([[sg.InputText("", size=(5, 10), key="v1i")],
                                                [sg.InputText("", size=(5, 10), key="v1j")]]), sg.Text(")"),
                       sg.Combo(["+", "-", "/"], key="vecop"), sg.Text("("),
                       sg.Column([[sg.InputText("", size=(5, 10), key="v2i")],
                                  [sg.InputText("", size=(5, 10), key="v2j")]]), sg.Text(")"),
                       [sg.Button("Solve", key="vecaddsolve")]])
    elif dimension == 3:
        layout.append([sg.Text("("), sg.Column([[sg.InputText("", size=(5, 10), key="v1i")],
                                                [sg.InputText("", size=(5, 10), key="v1j")],
                                                [sg.InputText("", size=(5, 10), key="v1k")]]), sg.Text(")"),
                       sg.Combo(["+", "-", "/"], key="vecop"), sg.Text("("),
                       sg.Column([[sg.InputText("", size=(5, 10), key="v2i")],
                                  [sg.InputText("", size=(5, 10), key="v2j")],
                                  [sg.InputText("", size=(5, 10), key="v2k")]]), sg.Text(")"),
                       [sg.Button("Solve", key="vecaddsolve")]])
    return sg.Window("Vector Operations", layout, size=(300, 300))

def createVectorDistLayout(dimension):
    layout = []
    if dimension == 2:
        layout.append([sg.Text("Vector 1: ("), sg.Column([[sg.InputText("", size=(5, 10), key="v1i")],
                                                [sg.InputText("", size=(5, 10), key="v1j")]]), sg.Text(")"),
                       sg.Text(" Vector 2: ("),
                       sg.Column([[sg.InputText("", size=(5, 10), key="v2i")],
                                  [sg.InputText("", size=(5, 10), key="v2j")]]), sg.Text(")"),
                       [sg.Button("Solve", key="vecdistsolve")]])
    elif dimension == 3:
        layout.append([sg.Text("Vector 1: ("), sg.Column([[sg.InputText("", size=(5, 10), key="v1i")],
                                                [sg.InputText("", size=(5, 10), key="v1j")],
                                                [sg.InputText("", size=(5, 10), key="v1k")]]), sg.Text(")"),
                       sg.Text(" Vector 2: ("),
                       sg.Column([[sg.InputText("", size=(5, 10), key="v2i")],
                                  [sg.InputText("", size=(5, 10), key="v2j")],
                                  [sg.InputText("", size=(5, 10), key="v2k")]]), sg.Text(")"),
                       [sg.Button("Solve", key="vecaddsolve")]])
    return sg.Window("Vector Operations", layout, size=(500, 500))


def createSGLayout():
    layout = []
    layout.append([
        [sg.Text("Math Solver, please click your category")],
        [sg.Button("Matrices", key="-MATRIX-", enable_events=True)],
        [sg.Button("Vectors", key="vector")], [sg.Frame("Simultaneous Equations", [[
            sg.Button("Simultaneous Equations", key="simult"), sg.Text("Number of Unknowns"),
            sg.Combo([2, 3], default_value=2, key="unknowns")]])], [sg.Text("Select Your Theme"),sg.Listbox(values=sg.theme_list(),size=(20, 8),
                      key='-LIST-',
                      enable_events=True),sg.Button("OK", key="theme")],
          [sg.Button('Exit')]
    ])
    return sg.Window("Home", layout)


def createMatrixLayout():
    matrixLayout1 = [
        [sg.Text("Please Select What operation you would like to carry out")],
        [sg.Frame("2 Matrices Operations", [
        [sg.Button("Matrix Multiplication", key="-matrixMUL"), sg.Text("Dimension selections on next page")],[sg.Button("Transposed Matrix", key="mattran"),
                                                       sg.Text("Columns"),
                                                       sg.Combo([2, 3, 4, 5], key="trancol", default_value=2),
                                                       sg.Text("Rows"),
                                                       sg.Combo([2, 3, 4, 5], key="tranrow", default_value=2)],
                                                      [sg.Button("Matrix Addition", key="matrixadd"),
                                                       sg.Text("Columns"),
                                                       sg.Combo([2, 3, 4, 5], key="adddimcol", default_value=2),
                                                       sg.Text("Rows"),
                                                       sg.Combo([2, 3, 4, 5], key="adddimrow", default_value=2)],

                                                      [sg.Button("Matrix Subtraction", key="-matrixSUB"),
                                                       sg.Text("Columns"),
                                                       sg.Combo([2, 3, 4, 5], key="subdimcol", default_value=2),
                                                       sg.Text("Rows"),
                                                       sg.Combo([2, 3, 4, 5], key="subdimrow", default_value=2)]
                                                      ], element_justification='right')],
        [sg.Button("Scalar Multiplication", key="matrixscalar", auto_size_button=True),
         sg.Text("Scalar Value"), sg.InputText(default_text=0.5, key="scalarmult", size=10),
         sg.Text("Columns"),
         sg.Combo([2, 3, 4, 5], key="scalardimcol", default_value=2), sg.Text("Rows"),
         sg.Combo([2, 3, 4, 5], key="scalardimrow", default_value=3)],

        [sg.Frame("Single Matrix operations ", [[sg.Combo([2, 3, 4, 5], default_value=2, key="singledim")],
                                                        [sg.Button("Determinant", key="-matdet")
                                                         ], [sg.Button("Matrix Inverse", key="-INVERSE-")]])],

    ]
    i = copy.deepcopy(matrixLayout1)
    del matrixLayout1
    return sg.Window("", i, size=(600, 600))

def createMatrixDimWindow():
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
    return sg.Window("Select Your Dimensions", multdimLayout)

def popup(message):
    layout = [
        [sg.Text(message)],
        [sg.Push(), sg.Button('OK')],
    ]
    sg.Window('POPUP', layout, modal=True).read(close=True)


def gui():

    window = createSGLayout()
    dim = 0
    cols = 0
    rows = 0
    col1 = 0
    col2 = 0,
    row1 = 0
    row2 = 0
    unknowns = 0
    prev = None
    scalar = 0
    sg.theme("BlueMono")
    while True:
        event, values = window.read()
        if event=="theme":
            sg.theme(values['-LIST-'][0])
            sg.change_look_and_feel(values['-LIST-'][0])
            window.close()
            window = createSGLayout()
            sg.theme(values['-LIST-'][0])

        if event == "-MATRIX-":
            # src.tkintergui.root()
            window.close()
            window = createMatrixLayout()
        if event == "matrixscalar":
            window.close()
            scalar = values["scalarmult"]
            layout1 = []
            cols = values["scalardimcol"]
            rows = values["scalardimrow"]
            layout1.append(createMatrix(cols, rows))
            layout1.append([[sg.Button("Solve", key="scalarsolve")], [sg.Output()]])
            window = sg.Window("Scalar Operations", layout1)
        if event == "scalarsolve":
            matrix = mat.Matrices().singleSplit(values, cols["scalardimcol"], rows)
            result = mat.Matrices().scalarMult(matrix, scalar)
            print(result)
        if event == "-INVERSE-":
            window.close()
            dim = values["singledim"]
            window = createInverseLayout(dim, dim)
        if event == "-insub-":
            arr = mat.Matrices().singleSplit(values, dim, dim)
            try:
                result = mat.Matrices().manualInverse(np.array(arr))
                print("The result is:")
                print(result)
            except np.linalg.LinAlgError:
                det = mat.Matrices().matrixDeterminant(np.array(arr))
                print("Matrix cannot be inverted. The determinant is %s, this must not be 0", det)
        if event == "matrixadd":
            window.close()
            cols = values["adddimcol"]
            rows = values["adddimrow"]
            window = createAdditionLayout((cols, rows))
        if event == "-addmat-":
            matrices = mat.Matrices().matrixSplit(values, cols, rows)
            result = mat.Matrices().matrixAddition(matrices[0], matrices[1])
            print(result)
        if event == "-matrixSUB":
            window.close()

            cols = values["subdimcol"]
            rows = values["subdimrow"]
            window = createSubtractionLayout(cols, rows)
        if event == "-submat-":
            matrices = mat.Matrices().matrixSplit(values, cols, rows)
            result = mat.Matrices().matrixSubtraction(matrices[0], matrices[1])
            try:
                sg.Popup(createStringResult(result))
                print(createStringResult(result))
            except Exception as ex:
                print(ex)
        if event == "-matrixMUL":
            window.close()
            window = createMatrixDimWindow()
        if event == "-okmultdim":
            col1 = values["matdimcol1"]
            col2 = values["matdimcol2"]
            row1 = values["matdimrow1"]
            row2 = values["matdimrow2"]
            if not mat.Matrices().check_mult_dimension(col1, row2):
                sg.Popup("Try Again! Columns of first Matrix must be equal to rows of second Matrix")
            else:
                window.close()
                window = createMultLayout(col1, row1, col2, row2)
        if event == "-multmat-":
            matrices = mat.Matrices().matrixSplitMult(values, col1, row1, col2, row2)
            result = mat.Matrices().matrixmultiplication(matrices[0], matrices[1])
            print(result)

        if event == "-matdet":
            window.close()

            dim = int(values["singledim"])
            window = sg.Window("Matrix Determinant", createDetLayout(values["singledim"]))
        if event == "-detmat":
            matrix = mat.Matrices().singleSplit(values, dim, dim)
            result = mat.Matrices().matrixDeterminant(matrix)
            print(result)
        if event == "mattran":
            window.close()
            cols = values["trancol"]
            rows = values["tranrow"]
            window = sg.Window("Transpose Matrix",
                               [[sg.Frame("Matrix Input", createMatrix(values["trancol"], values["tranrow"]))],
                                [sg.Button("Solve", key="tranok")]])
        if event == "tranok":
            window.close()

            matrix = mat.Matrices().singleSplit(values, cols, rows)
            cofactor = mat.Matrices().matrixCofactors(matrix)
            print("Cofactor Matrix")
            print(cofactor)
            print("Transposed matrix")
            cofactor = np.transpose(np.array(cofactor))
            print(cofactor)
        if event == "matrixscalar":
            cols = values
        if event == "simult":
            window.close()

            unknowns = values["unknowns"]
            newLayout = createSimultaneousLayout(unknowns)
            window = sg.Window("Simultaneous Equations", newLayout, size=(600, 600))
        if event == "simultsolve":
            window.close()

            lmatrix = []
            rmatrix = []
            curr = []
            for i in range(1, unknowns + 1):
                xstr = "Equation" + str(i) + "x"
                ystr = "Equation" + str(i) + "y"
                zstr = "Equation" + str(i) + "z"
                ansstr = "Equation" + str(i) + "ans"
                curr.append(float(values[xstr]))
                curr.append(float(values[ystr]))
                if unknowns == 3:
                    curr.append(float(values[zstr]))
                lmatrix.append(curr)
                curr = []
                rmatrix.append([float(values[ansstr])])
            try:
                result = mat.Matrices().simultaneous_equations(np.array(lmatrix), np.array(rmatrix), unknowns)
                result_str = "x = " + str(result[0]) + "\ny = " + str(result[1])
                if unknowns > 2:
                    result_str = result_str + "\nz = " + str(result[2])
                sg.Popup(result_str)
            except np.linalg.LinAlgError:
                linAlgError()
        if event == "vector":
            window.close()
            window = createVectorLayout()
        if event == "intersectpoints":
            window = sg.Window("Point Intersection", createIntersectionPointsLayout())
        if event == "solveintersectpoint":

            try:
                a1, b1, a2, b2 = vec.getPointSplit(values)
                vector = vec.Vector()
                x, y, z = vector.getPointIntersection(a1, b1, a2, b2)
            except TypeError as ex:
                print(ex)
        if event == "intersectequations":
            window.close()
            window = createIntersectLineLayout()
        if event == "lineintersectsolve":
            tup = vec.getLineSplit(values)
            print("Point of Intersection: " + str(tup))
        if event == "vecadd":
            dim = values["vecadddim"]
            window.close()
            window = createVectorAdditionLayout(dim)
        if event == "vecaddsolve":
            op = values["vecop"]
            vect = vec.getVecOpItems(values)
            if op == "+":
                result = vect.addition()
            elif op == "-":
                result = vect.subtraction()
            else:
                result = vect.division()
            result_str = "Result is " + str(result)
            sg.Popup(createStringResult(result))
        if event == "vecdist":
            dim = values["vecadddim"]
            window.close()
            window = createVectorDistLayout(dim)
        if event == "vecdistsolve":
            vect = vec.getVecOpItems(values)
            result = vect.vectorDistance()
            sg.Popup(result)

        if event =="vecdot":
            window.close()
            dim = values["vecadddim"]
            window = createVectorDotLayout(dim)

        if event == "vecdotsolve":
            vect = vec.getVecOpItems(values)
            op = values["vecop"]
            if op == "Dot":
                result = vect.dotProduct()
            elif op=="Cross":
                result = vect.crossProduct()

            else:
                sg.Popup("Invalid Choice. Please choose Cross or Dot")
            sg.Popup(result)


        if event == "OK":
            continue
        if event == sg.WINDOW_CLOSED or event == sg.WIN_CLOSED:
            window.close()
            window = createSGLayout()

    # window.close()


gui()
