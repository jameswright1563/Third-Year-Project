import io
import urllib

import numpy as np
import wolframalpha
from PIL import Image, ImageTk

import src.matrices as mat
import src.vectors as vec
import PySimpleGUI as sg
import layouts as layout
import requests
from io import BytesIO
import src.calculus as calc

lay = layout.Layout()
mat = mat.Matrices()
calc = calc.Calculus()


class GUI:

    def step_results(self, result, steps):
        try:
            sg.Popup("Result:\n" + result + "\nStep-By-Steps:" + steps)
        except Exception:
            sg.Popup("No results!")

    def gui(self):
        sg.theme("Bright Colors")
        window = lay.createSGLayout("Bright Colors")
        theme = "Bright Colors"
        dim = 0
        cols = 0
        rows = 0
        col1 = 0
        col2 = 0,
        row1 = 0
        row2 = 0
        unknowns = 0
        scalar = 0
        appid = "W7YJ9Q-85R328TAWQ"
        client = wolframalpha.Client(appid)
        while True:
            event, values = window.read()
            if event == "help":
                sg.Popup("Welcome to Student Solver, a place where you can check your mathematical answers!"
                         "\n\nPress Matrices/Calculus/Vector buttons to choose a category, or enter your problem in the box."
                         "\n\nAn example is \n\nSolve 2x+4=5\n\nor\n\nDifferentiate 2x\n\nand then press solve."
                         "\n\nYou can see more about the syntax at www.wolframalpha.com"
                         "\n\nThe simultaneous equations buttton has a number of unknowns selector. "
                         "\nTwo unknowns will give 2 equations with x and y selectors, 3 unknowns will give 3 equations with x,y,z selectors."
                         "\n\nAt the bottom of the page is a theme selector. Choose your theme and press OK! "
                         "\n\nTo close this popup press the OK button.")
            if event == "helpmat":
                sg.Popup("On this page you can choose different matrix operations. "
                         "\The frame for 2 matrices operations means you will need to input 2 matrices, "
                         "and the single matrix operations frame only requires you to input one matrix."
                         "\n\nFor Matrix Multiplication, the dimensions can be selected on the next page. To note: the 1st dimension of the first matrix must equal the 2nd dimension of the 2nd matrix e.g. 2x3 and 3x2 is compatible."
                         "\n\nFurther operations for 2 matrices involve transposing a matrix, addition and subtraction."
                         "\n\nThe scalar button will multiply the entire matrix by the scalar value."
                         "\n\nSingle Matrix operations include finding the determinant or the inverse of a matrix. Only 1 dimension is to be selected as the matrix has to be square."
                         "\n\nTo exit this window press OK, and to go back to the home page simply exit the window")
            try:
                if event == "theme":
                    try:
                        theme = values['-LIST-']
                        sg.theme(theme)
                        window.close()
                        window = lay.createSGLayout(values['-LIST-'])
                        sg.theme(values['-LIST-'])
                    except IndexError:
                        sg.Popup("Please select a theme")
                if event == "eqsolve":
                    eq = values["eq"]
                    res = client.query(eq)

                    query = urllib.parse.quote_plus(f"{eq}")
                    query_url = f"http://api.wolframalpha.com/v2/query?" \
                                f"appid={appid}" \
                                f"&input={query}" \
                                f"&scanner=Solve" \
                                f"&podstate=Result__Step-by-step+solution" \
                                "&format=plaintext" \
                                f"&output=json"

                    r = requests.get(query_url).json()

                    """Window with plot created"""
                    if eq.find("plot") >= 0 or eq.find("Plot") >= 0:
                        img_link = res["pod"][1]["subpod"]["img"].src
                        print(img_link)
                        response = requests.get(img_link)
                        im = Image.open(BytesIO(response.content))
                        output = io.BytesIO()
                        im.save(output, format="gif")
                        sg.PopupAnimated(output.getvalue(), title="Plotted Data", message="Data plotted ",
                                         no_titlebar=False,
                                         alpha_channel=0.95, time_between_frames=30)
                    else:
                        try:
                            data = r["queryresult"]["pods"][0]["subpods"]
                            result = data[0]["plaintext"]
                            steps = data[1]["plaintext"]
                            self.step_results(result, steps)
                        except KeyError:
                            sg.Popup("Results: "+ next(res.results).text)
                if event == "-MATRIX-":
                    window.close()
                    window = lay.createMatrixLayout()
                if event == "matrixscalar":
                    window.close()
                    scalar = values["scalarmult"]
                    cols = values["scalardimcol"]
                    rows = values["scalardimrow"]
                    window = lay.createScalarMultLayout(cols, rows)
                if event == "scalarsolve":
                    matrix = mat.singleSplit(values, cols, rows)
                    result = mat.scalarMult(matrix, scalar)
                    sg.Popup(mat.createResultPage(result))
                if event == "-INVERSE-":
                    window.close()
                    dim = values["singledim"]
                    window = lay.createInverseLayout(dim, dim)
                if event == "-insub-":
                    arr = mat.Matrices().singleSplit(values, dim, dim)
                    try:
                        result = mat.manualInverse(np.array(arr))
                        print("The result is:")
                        print(result)
                        self.createResultPage(result)

                    except np.linalg.LinAlgError:
                        det = mat.matrixDeterminant(np.array(arr))
                        print("Matrix cannot be inverted. The determinant is %s, this must not be 0", det)
                        sg.Popup("Matrix cannot be inverted. The determinant is %s, this must not be 0", det)
                if event == "matrixadd":
                    window.close()
                    cols = values["adddimcol"]
                    rows = values["adddimrow"]
                    window = lay.createAdditionLayout(cols, rows)
                if event == "-addmat-":
                    matrices = mat.matrixSplit(values, cols, rows)
                    result = mat.matrixAddition(matrices[0], matrices[1])
                    sg.Popup(mat.createResultPage(result))
                if event == "-matrixSUB":
                    window.close()

                    cols = values["subdimcol"]
                    rows = values["subdimrow"]
                    window = lay.createSubtractionLayout(cols, rows)
                if event == "-submat-":
                    matrices = mat.matrixSplit(values, cols, rows)
                    result = mat.matrixSubtraction(matrices[0], matrices[1])
                    try:
                        sg.Popup(mat.createResultPage(result))
                    except Exception as ex:
                        print(ex)
                if event == "-matrixMUL":
                    window.close()
                    window = lay.createMatrixDimWindow()
                if event == "-okmultdim":
                    col1 = values["matdimcol1"]
                    col2 = values["matdimcol2"]
                    row1 = values["matdimrow1"]
                    row2 = values["matdimrow2"]
                    if not mat.check_mult_dimension(col1, row2):
                        sg.Popup("Try Again! Columns of first Matrix must be equal to rows of second Matrix")
                    else:
                        window.close()
                        window = lay.createMultLayout(col1, row1, col2, row2)
                if event == "-multmat-":
                    matrices = mat.Matrices().matrixSplitMult(values, col1, row1, col2, row2)
                    result = mat.Matrices().matrixmultiplication(matrices[0], matrices[1])
                    print(result)

                if event == "-matdet":
                    window.close()

                    dim = int(values["singledim"])
                    window = lay.createDetLayout(values["singledim"])
                if event == "-detmat":
                    matrix = mat.singleSplit(values, dim, dim)
                    result = mat.matrixDeterminant(matrix)
                    print(result)
                if event == "mattran":
                    window.close()
                    cols = values["trancol"]
                    rows = values["tranrow"]
                    window = lay.createTransposeLayout(cols, rows)
                if event == "tranok":
                    matrix = mat.singleSplit(values, cols, rows)
                    cofactor = mat.matrixCofactors(matrix)
                    print("Cofactor Matrix")
                    print(cofactor)
                    print("Transposed matrix")
                    cofactor = np.transpose(np.array(cofactor))
                    sg.Popup(mat.createResultPage(cofactor))

                if event == "simult":
                    window.close()
                    unknowns = values["unknowns"]
                    newLayout = lay.createSimultaneousLayout(unknowns)
                    window = newLayout
                if event == "simultsolve":

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
                        sg.Popup("Matrix irreversible")
                if event == "vector":
                    window.close()
                    window = lay.createVectorLayout()
                if event == "intersectpoints":
                    window.close()
                    window = lay.createIntersectionPointsLayout()
                if event == "solveintersectpoint":

                    try:
                        a1, b1, a2, b2 = vec.getPointSplit(values)
                        vector = vec.Vector()
                        x, y, z = vector.getPointIntersection(a1, b1, a2, b2)
                    except TypeError as ex:
                        print(ex)
                if event == "intersectequations":
                    window.close()
                    window = lay.createIntersectLineLayout()
                if event == "lineintersectsolve":
                    tup = vec.getLineSplit(values)
                    print("Point of Intersection: " + str(tup))
                if event == "vecadd":
                    dim = values["vecadddim"]
                    window.close()
                    window = lay.createVectorAdditionLayout(dim)
                if event == "vecaddsolve":
                    op = values["vecop"]
                    vect = vec.getVecOpItems(values)
                    if op == "+":
                        result = vect.addition()
                    elif op == "-":
                        result = vect.subtraction()
                    else:
                        result = vect.division()
                    sg.Popup(lay.createStringResult(result))
                if event == "vecdist":
                    dim = values["vecadddim"]
                    window.close()
                    window = lay.createVectorDistLayout(dim)
                if event == "vecdistsolve":
                    vect = vec.getVecOpItems(values)
                    result = round(vect.vectorDistance(), 2)
                    result_str = "Result is " + str(result)
                    sg.Popup(result_str)

                if event == "vecdot":
                    window.close()
                    dim = values["vecadddim"]
                    window = lay.createVectorDotLayout(dim)

                if event == "vecdotsolve":
                    vect = vec.getVecOpItems(values)
                    op = values["vecop"]
                    if op == "Dot":
                        result = vect.dotProduct()
                    elif op == "Cross":
                        result = vect.crossProduct()

                    else:
                        sg.Popup("Invalid Choice. Please choose Cross or Dot")
                    sg.Popup(result)

                if event == "calculus":
                    window.close()
                    window = lay.createCalculusLayout()
                if event == "diff":
                    window.close()
                    window = lay.createDifferentiationLayout()
                if event == "diffsolve":
                    res=calc.differentiation(values)
                    self.displayResult(res)
                if event == "integ":
                    window.close()
                    window = lay.createIntegrationLayout()
                    im = Image.open("integral.png")
                    im = im.resize((100, 100))
                    image = ImageTk.PhotoImage(image=im)
                    window["-IMAGE-"].update(data=image)
                if event == "integsolve":
                    res = calc.integration(values)
                    self.displayResult(res)
            except AttributeError as ex:
                print(ex)
                sg.Popup("Numerical value not entered!")
            if event == "OK":
                continue
            if event == sg.WINDOW_CLOSED or event == sg.WIN_CLOSED:
                window.close()
                window = lay.createSGLayout(theme)
            if event == "EXIT":
                break
        # window.close()

    def displayResult(self, res):
        try:
            result = "Result: " + next(res.results).text
            sg.Popup(result)
        except StopIteration:
            sg.Popup("No results!")

GUI().gui()
