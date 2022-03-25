# .py file for doing the main calulations of the matrix


# arr = [[-1,0,1],[2,-1,2],[-1,2,1]]

def determinant(arr):
    value = arr[0][0] * (arr[1][1] * arr[2][2] - arr[1][2] * arr[2][1])
    value1 = (arr[0][1] * (arr[1][0] * arr[2][2] - arr[1][2] * arr[2][0]))
    value2 = arr[0][2] * (arr[1][0] * arr[2][1] - arr[2][0] * arr[1][1])
    return value - value1 + value2


def print_inv(values, d):
    print("    [", values[0], ",", values[4], ",", values[2], "]")
    print(f"1/{d}", "[", values[3], ",", values[1], ",", values[5], "]")
    print("    [", values[6], ",", values[7], ",", values[8], "]")


def cofactor(arr):
    a = arr[1][1] * arr[2][2] - arr[2][1] * arr[1][2]
    b = arr[1][0] * arr[2][2] - arr[2][0] * arr[1][2]
    c = arr[1][0] * arr[2][1] - arr[2][0] * arr[1][1]
    # x
    d = arr[0][0] * arr[2][2] - arr[2][0] * arr[0][2]
    e = arr[0][1] * arr[2][2] - arr[2][1] * arr[0][2]
    f = arr[0][0] * arr[2][1] - arr[2][0] * arr[0][1]
    #
    g = arr[0][1] * arr[1][2] - arr[1][1] * arr[0][2]
    h = arr[0][0] * arr[1][2] - arr[1][0] * arr[0][2]
    i = arr[0][0] * arr[1][1] - arr[1][0] * arr[0][1]

    # print(a,-b,c,"\n",-d,e,-f,"\n",i,-h,g)
    ans = (a, d, g, -b, -e, -h, c, -f, i)
    det = determinant(arr)
    # print_inv(ans,det)
    return det, ans


if __name__ == '__main__':
    cofactor(arr)