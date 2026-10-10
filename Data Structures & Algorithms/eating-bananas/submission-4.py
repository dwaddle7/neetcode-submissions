import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total = 0
        for pile in piles: total += pile
        left = math.ceil(total/h) #theoretical minimum rate
        # left = 1
        right = max(piles) #theoretical maximum rate
        mid = left + (right - left)//2
        while (left < right):
            time = sum([math.ceil(pile/mid) for pile in piles])
            if time <= h: right = mid
            else: left = mid + 1
            mid = left + (right - left)//2
        return mid