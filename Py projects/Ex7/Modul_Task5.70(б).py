'''
text = input("Text = ")
flag = "No!"
if text[0].isdigit() is False or text[0] == "0":
    print(flag)
else:
    for i in range(1, len(text)):
        if text[i].isdigit() is True:
            print(flag)
            break
        else:
            flag = "Yes!"
    if flag == "Yes!":
        if len(text) - 1 == int(text[0]):
            print(flag)
        else:
            flag = "No!"
            print(flag)
'''

text=input("")
n=int(input("Скільки знищити?"))
k=int(input("починаючи з якого?"))
text2 = text[0:k-1] + text[k+n-1:len(text)]
print(text2)
