n = int(input())
str_data = input()
int_list = [int(x) for x in str_data.split()]
z = dict()
for x in int_list:
    z[x] = 1

print(len(z))

# https://www.eolymp.com/uk/submissions/9981503
