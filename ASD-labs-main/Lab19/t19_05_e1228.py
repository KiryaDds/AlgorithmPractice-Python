# Завдання 19.5 by  Янголь Ярослав / Комп. мех / 2 курс


class MinHeap:

    def __init__(self):
        self.heap = []
        
    def push(self, item):
        self.heap.append(item)
        self._sift_up(len(self.heap) - 1)
        
    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return root
    
    def _sift_up(self, ind):
        parent = (ind - 1) // 2
        while ind > 0 and self.heap[ind] < self.heap[parent]:
            self.heap[ind], self.heap[parent] = self.heap[parent], self.heap[ind]
            ind = parent
            parent = (ind - 1) // 2
            
    def _sift_down(self, ind):
        left_child = 2 * ind + 1
        right_child = 2 * ind + 2
        smallest = ind
        
        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child
            
        if smallest != ind:
            self.heap[ind], self.heap[smallest] = self.heap[smallest], self.heap[ind]
            self._sift_down(smallest)
    

def min_cost(nums):
    min_heap = MinHeap()
    for num in nums:
        min_heap.push(num)
        
    total_cost = 0

    while len(min_heap.heap) > 1:
        num1 = min_heap.pop()
        num2 = min_heap.pop()
        
        cost = num1 + num2
        total_cost += cost
        
        min_heap.push(cost)
        
    return total_cost



if __name__ == "__main__":

    n = int(input())
    nums = list(map(int, input().split()))
    cost = min_cost(nums)
    
    print(cost)
