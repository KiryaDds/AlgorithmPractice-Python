# Цей файл виконує 2 завдання

'''
def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

    return nums
'''


def get_sortedfile(fname1, fname2):
    f1 = open(fname1)
    f2 = open(fname2)
    info1 = f1.readlines()
    info2 = f2.readlines()

    if len(info1) < len(info2):
        maxl = len(info2)
        minl = len(info1)
        flag = info2
    else:
        maxl = len(info1)
        minl = len(info2)
        flag = info1

    unsorted_str = []
    for i in range(maxl):
        unsorted_str.append('')

    for i in range(minl):
        unsorted_str[i] = info1[i] + " " + info2[i]

    for i in range(minl, maxl):
        unsorted_str[i] = flag[i]

    fname = "file_merj.txt"
    f = open(fname, "w")
    for i in unsorted_str:
        # s = str(bubble_sort(list(map(int, i.split()))))
        s = str(list(map(int, i.split())))
        s = s[1:len(s)-1] + "\n"
        f.write(s)
    f.close()


print(get_sortedfile("file1.txt", "file2.txt"))
