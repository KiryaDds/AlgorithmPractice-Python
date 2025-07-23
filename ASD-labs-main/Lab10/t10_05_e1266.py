# Завдання 10.5 by  Янголь Ярослав / Комп. мех / 2 курс


def Opti_duration(dur, ind):
    
    global opti_dur, N, s

    if opti_dur == N: return
    
    if opti_dur < dur:
        if dur > N:
            return
        opti_dur = dur

    if ind == s: return


    Opti_duration(dur + tracks[ind], ind + 1)
    Opti_duration(dur, ind + 1)


if __name__ == "__main__":

    while True:
        try:
            line = input()
        except EOFError:
            break

        line = list(map(int, line.split()))
        N = line[0]
        s = line[1]
        tracks = line[2:]
        
        opti_dur = 0
        Opti_duration(0, 0)
        print("sum:",opti_dur,sep='')
