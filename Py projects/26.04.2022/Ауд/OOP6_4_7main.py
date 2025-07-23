from OOP6_4_7CSet import *
from OOP6_4_7Iter import *


def put(M):
    """Друк M - змінної класу CustomSet за допомогою ітератора.

    """
    Lc = IterIFS(M.lstSet)  # Створюємо об'єкт-ітератор
    for c in Lc:  # Цикл по колекції
        print(c, "", end='')
    print()


M1 = CustomSet([4, 3, 1, 4, 102])
print("Множина M1 з кількістью елементів %d\n" % len(M1), M1)
put(M1)
M2 = CustomSet([3, 4, 1.23, "ass", 4, 3])
print("Множина M2 з кількістью елементів %d\n" % len(M2), M2)
put(M2)
M3 = CustomSet([102, -10.5, 102.8, 1, "fff", "abnb", -8])
print("Множина M3 з кількістью елементів %d\n" % len(M3), M3)
put(M3)
# Приклади використання перевантажених операторів
MP = M1 + M2;
print("MP (об'єднання М1,М2):\n", MP);
put(MP)
MM = M2 - M1;
print("MM (різниця М2,М1):\n", MM);
put(MM)
MQ = M2 * M1;
print("MQ (перетин М2,М1):\n", MQ);
put(MQ)
MR = M2 / M3;
print("MR (симетрична різниця М2,М3):\n", MR);
put(MR)