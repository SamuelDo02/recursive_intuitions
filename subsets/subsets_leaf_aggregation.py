class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.subsets_rec(nums, [], 0, res)
        return res

    def subsets_rec(self, nums, curr, idx, res):
        if idx == len(nums):
            res.append(curr)
            return

        self.subsets_rec(nums, curr + [nums[idx]], idx + 1, res) # include
        self.subsets_rec(nums, curr, idx + 1, res) # exclude
