class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        hmap = {}
        for num in nums:
            hmap[num] = 1 + hmap.get(num, 0)
        for key, val in hmap.items():
            heapq.heappush(heap, (-val, key))
        
        result = []
        while len(result) < k:
            result.append(heapq.heappop(heap)[1])
        return result 