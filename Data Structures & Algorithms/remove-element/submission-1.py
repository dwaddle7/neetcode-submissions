class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        end = len(nums)
        i = 0
        count = 0
        while (i < end):
            if nums[i] == val:
                tmp = nums[i]
                nums.remove(nums[i])
                nums.append(tmp)
                end = end - 1
                count += 1
                continue
            else:
                i = i + 1
        return len(nums) - count