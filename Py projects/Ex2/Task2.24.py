z = float(input('z= '))
y = z + 2
if y < 0:
    f = y**2 - 0.3
elif 0 <= y <= 1:
    f = 0
else:
    f = y**2 + y
# записуєму нашу систему з умовами
x = f - 6.3  # виражаємо "х"
print('\033[33mх =', x)
# \033[33m -- жовтий колір
non_stop = input()
