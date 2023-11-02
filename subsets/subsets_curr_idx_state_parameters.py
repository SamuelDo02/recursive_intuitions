class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.subsets_rec(nums, [], 0)

    def subsets_rec(self, nums, curr, idx):
        if idx == len(nums):
            return [curr]

        include = self.subsets_rec(nums, curr + [nums[idx]], idx + 1)
        exclude = self.subsets_rec(nums, curr, idx + 1)

        return include + exclude
