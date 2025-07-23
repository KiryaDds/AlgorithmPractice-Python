# Завдання 9.5 by  Янголь Ярослав / Комп. мех / 2 курс
def MergeSort(arr):

    if len(arr) > 1:
        mid = len(arr) // 2
        lh = arr[:mid]
        rh = arr[mid:]
        MergeSort(lh)
        MergeSort(rh)

        i = 0
        j = 0
        k = 0
        while i < len(lh) and j < len(rh):
            if lh[i][0] < rh[j][0]:
                arr[k] = lh[i]
                i += 1
            elif lh[i][0] == rh[j][0]:
                i += 1
            else:
                arr[k] = rh[j]
                j += 1
            k += 1

        while i < len(lh):
            arr[k] = lh[i]
            i += 1
            k += 1

        while j < len(rh):
            arr[k] = rh[j]
            j += 1
            k += 1



if __name__ == '__main__':
    n = int(input())
    nums = list()
    for i in range(n):
        nums.append(tuple(map(int, input().split())))
    MergeSort(nums)
    for i in range(n):
        for j in range(2):
            print(nums[i][j], end=' ')
        print()