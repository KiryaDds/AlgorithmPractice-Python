# Task e1065 by  Янголь Ярослав / Комп. мех. / 2 курс
# https://www.eolymp.com/uk/submissions/13889474
# https://www.eolymp.com/uk/submissions/13890630 -- 50%

def field_count(st_n, st_m, depth):

    counter = 0
    for i in range(st_n, n):
        for j in range(st_m, m):
            
            if squares[i][j] == "#":
                squares[i][j] = "."
                counter += 1
                if j+1 != m:
                    if squares[i][j+1] == "#":
                        field_count(i, j+1, depth+1)
                if i+1 != n:
                    if squares[i+1][j] == "#":
                        field_count(i+1, j, depth+1)
                if j-1 != -1:
                    if squares[i][j-1] == "#":
                        field_count(i, j-1, depth+1)
                
                #squares[i][j] = "."
                if depth != 0:
                    return counter
    
    return counter


if __name__ == "__main__":

    squares = []
    n, m = map(int, (input().split()))
    for _ in range(n):                                  # тут було 5 замість n
        line = input()
        squares.append(list(line))

    print(field_count(0, 0, 0))
