slovnyk = {}
# slovnyk2 = dict()

slovnyk2 = {"dog": "собака", "cat": "кіт", "rat": ["пацюк"]}

slovnyk2["hen"] = ["курка"]
slovnyk2.update({"bull": ["бик"]})

for k, v in slovnyk2.items():
    print("{} - {}".format(k, v))
    slovnyk[k] = v

print(slovnyk)

slovnyk["dog"] = [slovnyk.get("dog"), "пес"]
slovnyk["cat"] = [slovnyk.get("cat"), "кішка", "котеня"]

print(slovnyk)


def input_dict():
    n = int(input("n = "))
    d = {}
    for i in range(n):
        eng = input("english: ")
        ukr_translate = input("ukrainian words separated by space: ")
        sp = ukr_translate.split()
        # d.update({eng: sp})
        d[eng] = sp
    return d


nd = input_dict()
nd.update(slovnyk)
for k, v in nd.items():
    print("{} -{}".format(k, v))


def reverse_translate(d):
    rev_dict = {}
    for key, value in d.items():
        for ukr in value:
            rev_dict[ukr] = key
    return rev_dict


for k, v in reverse_translate(slovnyk).items():
    print("ukrainian - {}, english - {}".format(k, v))

s = input()
if s in slovnyk2:
    print("english - {}, ukrainian - {} ".format(s, slovnyk2[s]))
else:
    print("No word!")
