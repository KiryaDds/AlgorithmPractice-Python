# Завдання 6.3 by  Янголь Ярослав / Комп. мех / 2 курс
# Результат виконання головного файлу 96-97%
"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""


def init():
    """ Викликається 1 раз на початку виконання програми. """
    global max_size, keys, values

    max_size = 100007
    keys = [None] * max_size
    values = [None] * max_size


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
    while keys[hash_key] != None:
        if values[hash_key] == title:
            return
        hash_key = (hash_key + 1) % max_size

    keys[hash_key] = author
    values[hash_key] = title


def find(author, title):
    """ Перевірає чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    hash_key = Hash_author(author)
    while keys[hash_key] != None:
        if values[hash_key] == title:
            return True
        hash_key = (hash_key + 1) % max_size
        
    return False


def delete(author, title):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    hash_key = Hash_author(author)
    while keys[hash_key] != None:
        if values[hash_key] == title:
            keys[hash_key] = None
            values[hash_key] = None
            return
        hash_key = (hash_key + 1) % max_size


def findByAuthor(author):
    """ Повертає список книг заданого автора.
    Якщо бібліотека не міститься книг заданого автора, то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    books_byAuthor = list()
    hash_key = Hash_author(author)
    while keys[hash_key] != None:
        if keys[hash_key] == author:
            books_byAuthor.append(values[hash_key])
        hash_key = (hash_key + 1) % max_size
        
    return books_byAuthor
