def matrix_input():
    m = int(input("Number of sparse elements: "))
    matr = {}
    for _ in range(m):
        row = int(input("r: "))
        col = int(input("c: "))
        val = float(input("m[{}, {}] = ".format(row, col)))
        matr[(row, col)] = val


    for i in range(max(max(matr.keys()))):
        matr[i] = 0
    return matr


def matrix_output(matr):
    for x, y in matr.items():
        print("m[{}, {}] = {}".format(x[0], x[1], y))


'''
def dense_output(matr):
    m = 0
    for x in matr.keys():
        if x[0] > m:
            m = x[0]
    for i in range(m):
        for j in range(m):
            if (i, j) in matr:
                print(matr[(i, j)])
            else:
                print("0")
'''

'''
def matrix_multiplication(m1, m2):
    mult_result = 0
    for i, j in m1.keys():
        for ii, jj in m2.keys():
            
    return mult_result
'''

matrix1 = matrix_input()
matrix2 = matrix_input()

print(matrix_output(matrix1))
print(matrix_output(matrix1))
print()
# print(dense_output(matrix))
# print(matrix_multiplication(matrix1, matrix2))
