s = str(input())
n = len(s)
if n % 4:
i = n
while i >= 4:
    s = '000' + s
