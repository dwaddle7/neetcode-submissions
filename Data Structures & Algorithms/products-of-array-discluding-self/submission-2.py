class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        numZeroes = 0
        totalProdWithoutZeros = 1
        for num in nums:
            if num == 0:
                numZeroes += 1
            else:
                totalProdWithoutZeros *= num
        for num in nums:
            if numZeroes > 1:
                result.append(0)
            elif numZeroes == 1:
                if num != 0:
                    result.append(0)
                else:
                    result.append(totalProdWithoutZeros)
            else:
                result.append(totalProdWithoutZeros//num)
        return result