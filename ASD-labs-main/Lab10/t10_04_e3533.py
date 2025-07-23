# Завдання 10.4 by  Янголь Ярослав / Комп. мех / 2 курс

    
def boss_score_time(score, time, num):

    global min_time, K, N
    
    if score >= K:
        if time < min_time:
            min_time = time
        return

    if num >= N:
        return

    boss_score_time(score + a[num][0], time + a[num][1], num + 1)
    boss_score_time(score, time, num + 1)


if __name__ == "__main__":

    N, K = map(int, input().split())
    a = list()
    for i in range(N):
        a.append(tuple(map(int, input().split())))

    min_time = 1e4
    boss_score_time(0, 0, 0)

    if min_time < 1e4:
        print(min_time)
    else:
        print(-1)
