
"""
A = str(input())
B = str(input())
A_10 = 0
B_10 = 0

k = len(A) - 1
for i in range(len(A)):
    A_10 += int(A[i]) * 2**k
    k -= 1

k = len(B) - 1
for i in range(len(B)):
    B_10 += int(B[i]) * 2**k
    k -= 1

print("A_10=", A_10)
print("B_10=", B_10)
sum_10 = A_10 + B_10
print("sum_10", sum_10)
sum_bin = ""
while sum_10 != 0:
    sum_bin += str(sum_10 % 2)
    sum_10 //= 2

print(sum_bin)
"""

# https://www.eolymp.com/uk/submissions/9964798 - 45%
'''
A = str(input())
B = str(input())

while len(A) < len(B) or len(B) < len(A):
    if min(len(A), len(B)) == len(A):
        A = "0" + A
    else:
        B = "0" + B


def digit(bin_sum, seed):
    zeros = 0
    if seed == 1:
        if len(bin_sum) != 1:
            bin_sum = bin_sum[0:len(bin_sum) - 1] + "10" + "0" * zeros
        else:
            bin_sum = bin_sum[0:len(bin_sum) - 1]
            zeros += 1
            digit(bin_sum, 1)

    return bin_sum


sum_b = ""
for i in range(len(A)):
    if A[i] == "0" and B[i] == "0":
        sum_b += "0"
    elif (A[i] == "0" and B[i] == "1") or (A[i] == "1" and B[i] == "0"):
        sum_b += "1"
    elif A[i] == "1" and B[i] == "1":
        sum_b = digit(sum_b, 1)

print(sum_b.lstrip("0"))
'''

# https://www.eolymp.com/uk/submissions/9964829 - 75%


def to_int(x):
    return int(x, 2)


def to_bin(x):
    res = ""
    while x > 0:
        d = x % 2
        x //= 2
        res += str(d)
    return res[::-1]


def sumn(x, y):
    return x + y


A = input()
B = input()
z = str(to_bin(sumn(to_int(A), to_int(B))))
print(z)

# https://www.eolymp.com/uk/submissions/9980147 - 95%
