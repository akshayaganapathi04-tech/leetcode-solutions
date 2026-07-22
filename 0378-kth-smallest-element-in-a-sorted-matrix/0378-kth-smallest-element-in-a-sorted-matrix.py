import heapq

class Solution:
    def kthSmallest(self, matrix, k):
        heap = []

        for row in matrix:
            for num in row:
                heapq.heappush(heap, num)

        for _ in range(k - 1):
            heapq.heappop(heap)

        return heapq.heappop(heap)
        