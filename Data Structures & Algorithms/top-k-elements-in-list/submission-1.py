class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        reverse_sorted_keys = sorted(counts, key=lambda k: counts[k], reverse=True)
        result = list()
        for i in range(k):
            result.append(reverse_sorted_keys[i])
        return result