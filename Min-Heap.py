
class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1

        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]

    def extract(self):
        if not self.heap:
            return None

        smallest = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            i = 0

            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                smallest_child = i

                if left < len(self.heap) and self.heap[left] < self.heap[smallest_child]:
                    smallest_child = left

                if right < len(self.heap) and self.heap[right] < self.heap[smallest_child]:
                    smallest_child = right

                if smallest_child == i:
                    break

                self.heap[i], self.heap[smallest_child] = self.heap[smallest_child], self.heap[i]
                i = smallest_child

        return smallest

    def size(self):
        return len(self.heap)


h = MinHeap()
numbers = [5, 9, 11, 14, 19, 17, 18, 13]

for n in numbers:
    h.insert(n)

print("Peek:", h.peek())
print("Size:", h.size())

while h.size() > 0:
    print(h.extract(), end=" ")
