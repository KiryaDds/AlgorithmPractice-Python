from collections import namedtuple

Students = namedtuple("Students", ["Surname", "Group_Number", "Mark_1", "Mark_2", "Mark_3"])

print("Якщо студент має заборгованість, його оцінка -- 0")
n = int(input("n = "))
A = []
for i in range(n):
    surname = input("Surname: ")
    group = int(input("Group number: "))
    mark_1 = int(input("First mark: "))
    mark_2 = int(input("Second mark: "))
    mark_3 = int(input("Third mark: "))
    A.append(Students(surname, group, mark_1, mark_2, mark_3))

print(A)

bad_students = []
for x in A:
    if x.Mark_1 == 0 or x.Mark_2 == 0 or x.Mark_3 == 0:
        bad_students.append(x.Surname)

bad = ""
for x in range(len(bad_students)):
    bad += bad_students[x] + ", "
bad = bad[0:len(bad) - 2]
print("Студентами, які мають заборгованості, є: ", bad)


best = ""
avg1 = 0
avg2 = 0
avg3 = 0
for x in A:
    avg1 += x.Mark_1
    avg2 += x.Mark_2
    avg3 += x.Mark_3
avg1 /= len(A)
avg2 /= len(A)
avg3 /= len(A)
if max(avg1, avg2, avg3) == avg1:
    best = "перший"
if max(avg1, avg2, avg3) == avg2:
    best = "другий"
if max(avg1, avg2, avg3) == avg3:
    best = "третій"
print("Найкраще було здано \033[33m{}\033[38m предмет.".format(best))


nice_students = []
for x in A:
    if (x.Mark_1 == 4 or x.Mark_1 == 5) and (x.Mark_2 == 4 or x.Mark_2 == 5) and (x.Mark_3 == 4 or x.Mark_3 == 5):
        nice_students.append(x.Surname)

nice = ""
for x in range(len(nice_students)):
    nice += nice_students[x] + ", "
nice = nice[0:len(nice) - 2]
print("На 4 та 5 іспити здали: ", nice)
