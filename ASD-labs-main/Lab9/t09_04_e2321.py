# Завдання 9.4 by  Янголь Ярослав / Комп. мех / 2 курс
def QuickSort(arr, a, b):
    if a >= b:
        return

    pivot = arr[a + (b - a) // 2]
    l = a
    r = b

    while True:
        while arr[l] < pivot:
            l += 1
        while arr[r] > pivot:
            r -= 1
        if l >= r:
            break

        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

    QuickSort(arr, a, r)
    QuickSort(arr, r + 1, b)


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    QuickSort(nums, 0, n - 1)
    for i in range(n):
        print(nums[i], end=' ')
    print()
