# Завдання 13.5 by  Янголь Ярослав / Комп. мех / 2 курс


class Stack:

    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return -1
        else:
            return self.items.pop()
    
    def back(self):
        if len(self.items) == 0:
            return -1
        else:
            return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def clear(self):
        self.items.clear()


def bracketsChecker(brackets_sequence):
    s = Stack()
    br_type = Stack()
    for bracket in brackets_sequence:

        if bracket == "(":
            br_type.push(0)
            s.push(bracket)
        elif bracket == "[":
            br_type.push(1)
            s.push(bracket)
        elif bracket == "{":
            br_type.push(2)
            s.push(bracket)

        elif bracket == ")" and br_type.back() == 0:
            if s.empty():
                return False
            else:
                s.pop()
                br_type.pop()
        elif bracket == "]" and br_type.back() == 1:
            if s.empty():
                return False
            else:
                s.pop()
                br_type.pop()
        elif bracket == "}" and br_type.back() == 2:
            if s.empty():
                return False
            else:
                s.pop()
                br_type.pop()

        else: return False

    return s.empty()


if __name__ == "__main__":

    line = input()
    res = bracketsChecker(line)
    if res: print("yes")
    else: print("no")

