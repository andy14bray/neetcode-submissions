class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rems = {}
        for idx, num in enumerate(nums):
            rem = target - num
            if num in rems:
                return [rems[num], idx]
            else:
                rems[rem] = idx