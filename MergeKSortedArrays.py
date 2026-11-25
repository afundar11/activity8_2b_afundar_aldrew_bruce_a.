
import heapq

def merge_arrays(arrays):
    heap = []
    result = []

    for i in range(len(arrays)):
        if arrays[i]:
            heapq.heappush(heap, (arrays[i][0], i, 0))

    while heap:
        value, array_index, element_index = heapq.heappop(heap)
        result.append(value)

        next_index = element_index + 1

        if next_index < len(arrays[array_index]):
            next_value = arrays[array_index][next_index]

            heapq.heappush(
                heap,
                (next_value, array_index, next_index)
            )

    return result


arrays = [
    [1, 4, 7],
    [2, 5, 8, 10],
    [3, 6, 9]
]

print("Merged Array:", merge_arrays(arrays))
