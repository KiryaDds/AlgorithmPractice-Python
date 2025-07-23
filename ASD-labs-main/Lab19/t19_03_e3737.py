# Завдання 19.3 by  Янголь Ярослав / Комп. мех / 2 курс


def check_if_heap(arr, n):

    for i in range(1, n):
        if 2*i <= n and arr[i-1] > arr[2*i-1]:
            return "NO";
        if 2*i+1 <= n and arr[i-1] > arr[2*i]:
            return "NO";

    return "YES";



if __name__ == "__main__":

    n = int(input())
    t_heap = list(map(int, input().split()))

    print(check_if_heap(t_heap, n))
