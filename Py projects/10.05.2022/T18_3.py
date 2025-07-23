import pickle
import datetime


class Genre:
    def __init__(self):
        self.name = None
        self.characteristic = None

    def inputG(self):
        self.name = input('Імя жанру=')
        self.characteristic = input('Характерні особливості=')

    def printG(self):
        print(self.name, self.characteristic, end=' ')


class Carrier:
    def __init__(self):
        self.nosiy = None
        self.colors = None
        self.time = None

    def inputC(self):
        self.nosiy = input('Тип носія=')
        self.colors = input('Кольорова гама=')
        self.time = int(input('Тривалість зберігання='))

    def printC(self):
        print(self.nosiy, self.colors, self.time, end=' ')


class Film(Genre, Carrier):
    def __init__(self):
        Genre.__init__(self)
        Carrier.__init__(self)
        self.title = None
        self.writer = None
        self.director = None
        self.duration = None

    def inputF(self):
        self.title = input('Назва фільму=')
        self.writer = input('Автор сценарію=')
        self.director = input('Режисер=')
        self.duration = input('Тривалість=')
        self.year = int(input('Рік запису='))
        Genre.inputG(self)
        Carrier.inputC(self)

    def printF(self):
        print(self.title, self.writer, self.director, self.duration, end=' ')
        Genre.printG(self)
        Carrier.printC(self)
        print(' ')


class FilmoTeka(Film):
    def __init__(self, nfile=None):
        Film.__init__(self)
        self._teka = []
        d = datetime.datetime.now()
        self.y = d.year
        self.nfile = nfile

    def addF(self):
        f = Film()
        f.inputF()
        self._teka.append(f)

    def printTeka(self):
        for f in self._teka:
            f.printF()

    def filterTeka(self):
        filtr = 0
        print('МОЖЛИВІ ВАРІАНТИ:\n1 - усі фільми,\n2 - носій,\n3 - автор,\n4 - режесер,\n5 - час зберігання')
        filtr = int(input('Ваш вибір := '))
        if filtr == 1:
            self.printTeka()
        elif filtr == 2:
            nosiy = input('Введіть носій=')
            for f in self._teka:
                if nosiy == f.nosiy:
                    f.printF()
        elif filtr == 3:
            writer = input('Введіть автора=')
            for f in self._teka:
                if writer == f.writer:
                    f.printF()
        elif filtr == 4:
            director = input('Введіть режесера=')
            for f in self._teka:
                if director == f.director:
                    f.printF()
        elif filtr == 5:
            time = int(input('Введіть час зберігання='))
            for f in self._teka:
                if time <= f.time - (self.y - f.year):
                    f.printF()

    def saveTeka(self):
        if self.nfile:
            file = open(self.nfile, 'wb')
            pickle.dump(self._teka, file)  # записуємо сховище фільмів  у файл
            file.close()
        else:
            print('''Ім'я файлу для збереження не обрано!''')

    def loadTeka(self, nfile):
        try:
            self.nfile = nfile
            self._teka = []
            file = open(self.nfile, 'rb')
            self._teka = pickle.load(file)  # завантажуємо сховище фільмів з файлу у список self.teka
            file.close()
        except FileNotFoundError as fn:
            print("Файл не знайдено", fn.filename,
                  "\nСтворено пусту фільмотеку з вказаним ім'ям")
            file = open(self.nfile, 'wb')
            pickle.dump(self._teka, file)
            file.close()


def Filmoteka_user_processing(teka):
    diya = 0
    while diya != 4:
        print('\nВАРІАНТИ РОБОТИ:\n1 - додати фільм,\n2 - вивести фільми,\n3 - зберегти на диск,\n4 - вихід з програми')
        diya = int(input('Виберіть дію := '))
        if diya == 1:
            teka.addF()
        elif diya == 2:
            teka.filterTeka()
        elif diya == 3:
            teka.saveTeka()


fn = input("Ім'я файлу з фільмотекою=")
myteka = FilmoTeka()
myteka.loadTeka(fn)
Filmoteka_user_processing(myteka)
