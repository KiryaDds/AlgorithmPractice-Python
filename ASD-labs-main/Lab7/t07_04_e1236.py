# Завдання 7.4 by  Янголь Ярослав / Комп. мех / 2 курс


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

    n = int(input())
    words = []
    for i in range(n):
        words.append(input())

    text = HashTable()
    line_t = input()
    for i in range(len(line_t)):
        text.add(line_t[i])

    for i in range(n):
        line = words[i]
        if line[-1] in line_t:
            prefix = line_t.index(line[-1])
        for j in range(len(line)):
            if not text.find(line[j]):
                prefix = 0
                break
            else:
                text.delete(line[j])

    if prefix == 0:
        print("NO")
    else:
        print("YES", prefix + 1)
