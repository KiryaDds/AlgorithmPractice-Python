# Завдання 14.12 by  Янголь Ярослав / Комп. мех / 2 курс


class Queue:

    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.empty():
            return self.items.pop(0)
        
    def min_item(self):
        if not self.empty():
            return min(self.items)


if __name__ == "__main__":

    n, a, b, c, x_i = input().split()
    n = int(n); a = int(a); b = int(b); c = int(c); x_i = int(x_i)
    sum_min = 0
    qe = Queue()

    for i in range(n):
        x_i = ((a * x_i * x_i + b * x_i + c) // 100) % 1000000
        if x_i % 5 < 2:
            qe.pop()
            if not qe.empty():
                sum_min += qe.min_item()
        else:
            qe.push(x_i)
            sum_min += qe.min_item()
            
    print(sum_min)