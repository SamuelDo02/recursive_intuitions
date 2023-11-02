class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        first = nums[0]
        smaller_subsets = self.subsets(nums[1:])

        res = []
        for subset in smaller_subsets:
            res.append(subset + [first]) # include
            res.append(subset) # exclude

        return res
