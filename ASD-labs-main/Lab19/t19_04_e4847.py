# Завдання 19.4 by  Янголь Ярослав / Комп. мех / 2 курс


class Heap:

    def __init__(self, id, priority):
        self.id = id
        self.priority = priority


class PriorityQueue:

    def __init__(self):
        self.heap = []
        self.heap_by_id = {}
        self.size = 0

    def insert(self, id, priority):
        heap = Heap(id, priority)
        self.heap.append(heap)
        self.heap_by_id[id] = self.size
        self.size += 1
        self.siftUp(self.size - 1)

    def extractMax(self):
        max_heap = self.heap[0]
        max_id, max_priority = max_heap.id, max_heap.priority

        last_heap = self.heap[self.size - 1]
        self.heap[0] = last_heap
        self.heap_by_id[last_heap.id] = 0

        del self.heap[self.size - 1]
        del self.heap_by_id[max_id]

        self.size -= 1
        self.siftDown(0)

        return max_id, max_priority

    def changePriority(self, id, priority):
        ind = self.heap_by_id[id]
        old_priority = self.heap[ind].priority
        self.heap[ind].priority = priority

        if priority > old_priority:
            self.siftUp(ind)
        else:
            self.siftDown(ind)

    def siftUp(self, ind):
        while ind > 0:
            parent_ind = (ind - 1) // 2
            if self.heap[ind].priority <= self.heap[parent_ind].priority:
                break
            self.swap(ind, parent_ind)
            ind = parent_ind

    def siftDown(self, ind):
        while True:
            left_child_ind = 2 * ind + 1
            right_child_ind = 2 * ind + 2

            largest = ind

            if left_child_ind < self.size and self.heap[left_child_ind].priority > self.heap[largest].priority:
                largest = left_child_ind

            if right_child_ind < self.size and self.heap[right_child_ind].priority > self.heap[largest].priority:
                largest = right_child_ind

            if largest == ind:
                break

            self.swap(ind, largest)
            ind = largest

    def swap(self, i, j):
        heap_i = self.heap[i]
        heap_j = self.heap[j]

        self.heap[i] = heap_j
        self.heap[j] = heap_i

        self.heap_by_id[heap_i.id] = j
        self.heap_by_id[heap_j.id] = i



if __name__ == "__main__":

    t_queue = PriorityQueue()

    while True:
        try:
            line = input().split()

            if line[0] == "ADD":
                id = line[1]
                priority = int(line[2])
                t_queue.insert(id, priority)

            elif line[0] == "POP":
                id, priority = t_queue.extractMax()
                print(id, priority)

            elif line[0] == "CHANGE":
                id = line[1]
                new_priority = int(line[2])
                t_queue.changePriority(id, new_priority)

        except EOFError:
            break