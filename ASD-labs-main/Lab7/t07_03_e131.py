# Завдання 7.3 by  Янголь Ярослав / Комп. мех / 2 курс


class HashTable:

    def __init__(self):

        self.max_size = 100007
        self.keys = [None] * self.max_size
        self.values = [None] * self.max_size


    def Hash_word(self, S):
        N = 31
        h = 0
        for i in range(len(S)):
            h = h * N + ord(S[i])
        return h % self.max_size


    def add(self, word):

        hash_key = self.Hash_word(word)
        while self.keys[hash_key] != None:
            if self.values[hash_key] == word:
                return
            hash_key = (hash_key + 1) % self.max_size

        self.keys[hash_key] = hash_key
        self.values[hash_key] = word


    def find(self, word):

        hash_key = self.Hash_word(word)
        while self.keys[hash_key] != None:
            if self.values[hash_key] == word:
                return True
            hash_key = (hash_key + 1) % self.max_size
            
        return False


    def delete(self, word):

        hash_key = self.Hash_word(word)
        while self.keys[hash_key] != None:
            if self.values[hash_key] == word:
                self.keys[hash_key] = None
                self.values[hash_key] = None
                return
            hash_key = (hash_key + 1) % self.max_size


if __name__ == "__main__":

    word = HashTable()

    line0 = input()
    for i in range(len(line0)):
        word.add(line0[i])

    n = int(input())
    res = n

    for i in range(n):
        line = input()
        if len(line) > len(line0):
            res -= 1
            continue
        for j in range(len(line)):
            if not word.find(line[j]):
                res -= 1
                break

    print(res)