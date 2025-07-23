text = input("text = ")
'''
first = text.find(":", 0)
print(first)
second = text.find(":", first + 1)
print(second)
for i in range(first):
    print(text[i], end="")

print()

for i in range(first + 1, len(text)):
    print(text[i], end="")

print()

for i in range(first + 1, second):
    print(text[i], end="")

if second == -1:
    for i in range(first + 1, len(text)):
        print(text[i], end="")
        
print()
'''


first = text.find(":")
second = text.find(":", first + 1)
punkta = text[0:first]      # cut, vyrizka 0...first-1
punktb = text[first + 1:]   # first+1... end text[first+1: -1]
punktc = text[first + 1:second]

# if second >= 0:
                # dopysaty

print(punkta, "\n", punktb, "\n", punktc)
