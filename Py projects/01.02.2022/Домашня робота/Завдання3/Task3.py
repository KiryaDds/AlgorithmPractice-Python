# 3 завдання...

from collections import OrderedDict


def get_lines(filename):
    lines = []
    for i in filename:
        lines.append(i.split())
        lines.sort()

    return lines


def same_name(providers_, h_, names):
    amount = 0
    value = 0
    for i in names:
        if i != h_:
            if names.count('') >= 1:
                names.remove('')
            names.append(h_)
            for i in providers_.keys():
                for j in providers_[i]:
                    for h in j.keys():
                        if h == h_:
                            amount += j[h][0]
                            value += j[h][1]
                        else:
                            amount = 0
                            value = 0
                    break
                break

    return amount, value, names


def report_printing(lines, filename):
    providers = {}
    for line in lines:
        if providers.get(line[0]) is None:
            providers[line[0]] = [{line[1]: [int(line[2]), int(line[3])/100]}]
        else:
            providers[line[0]].append({line[1]: [int(line[2]), int(line[3])/100]})

    providers = OrderedDict(providers)
    names = ['', '']
    last_amount = 0
    last_value = 0
    for i in providers.keys():
        filename.write("=" + i + "=\n")
        amount = 0
        value = 0
        h_p = '_'
        for j in providers[i]:
            s1 = '                '
            s2 = '      '
            s = ''

            for h in j.keys():
                all_amount, all_value, names = same_name(providers, h, names)

                amount += j[h][0]
                value += j[h][1]

                last_amount += j[h][0]
                last_value += j[h][1]

                h_len = len(h)
                h_dif = 16 - h_len
                for _ in range(h_dif):
                    s += " "

            for h in j.keys():
                all_amount_, all_value_, names = same_name(providers, h, names)
                if h == h_p:
                    filename.write(h + s + str(amount) + s2 + str(value) + "\n")
                else:
                    filename.write(h + s + str(j[h][0] + all_amount + all_amount_) + s2 + str(j[h][1] + all_value + all_value_) + "\n")
                    h_p = h
                names = ['', '']

        filename.write(s1 + str(amount) + s2 + str(value) + "\n\n")
    filename.write(s1 + str(last_amount) + s2 + str(last_value))
    filename.close()

    return providers


if __name__ == "__main__":
    f_in = open("provide.txt", "r")
    f_out = open("report.txt", "w")
    f_out.write("З В І Т    за  обліковий  період\n\n")
    print(report_printing(get_lines(f_in), f_out))
