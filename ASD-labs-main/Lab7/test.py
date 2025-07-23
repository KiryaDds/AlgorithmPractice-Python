class Node:

    def __init__(self, key: int, value):
        self.key = key
        self.value = value
        self.next = None
        self.valid = True

class HashTable:

    MAX_SIZE = 1000
    def __init__(self):
        self.slots = [None] * HashTable.MAX_SIZE
        
    @staticmethod
    def hash(key: int) -> int:
        return key % HashTable.MAX_SIZE

    def put(self, key, value):
        hash_key = HashTable.hash(key)
        slot = self.slots[hash_key]
        while slot != None:
            if slot.key == key:
                slot.value = value
                slot.valid = True
                return
            slot = slot.next
        slot = Node(key, value)
        slot.next = self.slots[hash_key]
        self.slots[hash_key] = slot
        
    def get(self, key):
        hash_key = HashTable.hash(key)
        slot = self.slots[hash_key]
        while slot != None:
            if slot.key == key:
                return slot.value
            slot = slot.next
        return None

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __len__(self):
        return self.current_size

    def __contains__(self, key):
        return not (self[key] is None)

    def __str__(self):
        return str(self.keys) + '\n' + str(self.values) + '\n'


if __name__ == "__main__":

    n = int(input())

    words = []
    for i in range(n):
        words.append(input())

    text = HashTable()
    line_t = input()
    for i in range(len(line_t)):
        text.put(line_t.count(line_t[i]), line_t[i])

    for i in range(n):
        prefix = 0
        for j in range(len(words[i])):
            if words[i] in text:
                


    if prefix == 0:
        print("NO")
    else:
        print("YES", prefix + 1)
