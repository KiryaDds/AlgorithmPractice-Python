# Завдання 6.4 by  Янголь Ярослав / Комп. мех / 2 курс
# Результат виконання головного файлу 89%
"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""

class Node:
    """ Допоміжний клас: вузол таблиці """
    def __init__(self, key, value):
        self.key = key
        self.value = value 
        self.next = None
        self.valid = True


def init():
    """ Викликається 1 раз на початку виконання програми. """
    global max_size, cells

    max_size = 107
    cells = [None] * max_size


N = 31
def Hash_author(S):
    h = 0
    for i in range(len(S)):
        h = h * N + ord(S[i])
    return h % max_size


def addBook(author, title):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    hash_key = Hash_author(author)
    cell = cells[hash_key]
    while cell != None:
        if cell.key == author:
            cell.value = title
            cell.valid = True
            return 
        cell = cell.next

    cell = Node(author, title)
    cell.next = cells[hash_key]
    cells[hash_key] = cell


def find(author, title):
    """ Перевірає чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    hash_key = Hash_author(author)
    cell = cells[hash_key]
    while cell != None:
        if cell.key == author and cell.value == title:
            return True
        cell = cell.next
        
    return False


def delete(author, title):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    hash_key = Hash_author(author)
    cell = cells[hash_key]
    while cell != None:
        if cell.key == author and cell.value == title:
            cell.key = None
            cell.value = None
            cell.valid = False
            return
        cell = cell.next


def findByAuthor(author):
    """ Повертає список книг заданого автора.
    Якщо бібліотека не міститься книг заданого автора, то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    books_byAuthor = list()
    hash_key = Hash_author(author)
    cell = cells[hash_key]
    while cell != None:
        if cell.key == author:
            books_byAuthor.append(cell.value)
        cell = cell.next
        
    return books_byAuthor
