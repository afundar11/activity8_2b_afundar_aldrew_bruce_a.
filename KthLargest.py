
import heapq

def kth_largest(numbers, k):
    if k < 1 or k > len(numbers):
        return None

    heap = []

    for num in numbers:
        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]


numbers = [3, 2, 1, 5, 6, 4]
k = 2

print("Kth Largest:", kth_largest(numbers, k))
print("Sorted Verification:", sorted(numbers, reverse=True)[k - 1])
