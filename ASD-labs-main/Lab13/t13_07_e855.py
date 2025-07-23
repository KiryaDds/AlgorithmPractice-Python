# Завдання 13.7 by  Янголь Ярослав / Комп. мех / 2 курс


import sys


class Stack:

    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            exit(1)
        else:
            return self.items.pop()
    
    def back(self):
        if len(self.items) == 0:
            exit(1)
        else:
            return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def clear(self):
        self.items.clear()

    def print(self):
        for i in range(self.size()):
            print(self.items[i], end="")


def nice_brackets(n):
    
    def generate_brackets(n, opened=0, closed=0, curr=""):
        if closed == n:
            for c in curr:
                if c in ("(", "["):
                    st.push(c)
                else:
                    if st.empty() or st.back() + c not in ("()", "[]"):
                        break
                    st.pop()
            else:
                sys.stdout.write(curr + "\n")
                st.clear()
                return
            
        if opened < n:
            generate_brackets(n, opened + 1, closed, curr + "(")
            generate_brackets(n, opened + 1, closed, curr + "[")
        if closed < opened:
            generate_brackets(n, opened, closed + 1, curr + ")")
            generate_brackets(n, opened, closed + 1, curr + "]")

    st = Stack()
    generate_brackets(n / 2)


if __name__ == "__main__":

    nice_brackets(int(input()))