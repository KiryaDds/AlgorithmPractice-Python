# Завдання 14.8 by  Янголь Ярослав / Комп. мех / 2 курс


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
    
    def front(self):
        if not self.empty():
            return self.items[0]
    
    def size(self):
        return len(self.items)
    
    def clear(self):
        self.items.clear()


def drunkard_game(n, pl1, pl2):
    first = Queue()
    second = Queue()
    for i in range(n//2):
        first.push(pl1[i])
        second.push(pl2[i])

    steps = 0
    draw_final = 2 * 105
    while True:
        if steps == draw_final:
            print("draw")
            break
        if first.empty():
            print("second", steps)
            break
        if second.empty():
            print("first", steps)
            break
        c1 = first.pop()
        c2 = second.pop()
        if c1 == 0 and c2 == n-1:
            first.push(c1)
            first.push(c2)
        elif c1 == n-1 and c2 == 0:
            second.push(c1)
            second.push(c2)
        elif c1 > c2:
            first.push(c1)
            first.push(c2)
        elif c2 > c1:
            second.push(c1)
            second.push(c2)
        steps += 1


if __name__ == "__main__":

    n = int(input())
    player1 = list(map(int, input().split()))
    player2 = list(map(int, input().split()))
    drunkard_game(n, player1, player2)
