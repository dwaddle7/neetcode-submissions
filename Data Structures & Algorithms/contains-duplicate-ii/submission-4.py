class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # the sliding window has to be len(k + 1)
        # write a function that sees if there's a duplicate in an array
        if (k >= len(nums)):
            return self.containsDuplicate(nums)
        for i in range(len(nums)-k+1):
            if self.containsDuplicate(nums[i:i+k+1]):
                return True
        return False

    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False