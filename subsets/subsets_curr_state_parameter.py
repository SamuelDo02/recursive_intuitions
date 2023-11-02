class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.subsets_rec(nums, [])

    def subsets_rec(self, nums, curr):
        if not nums:
            return [curr]

        include = self.subsets_rec(nums[1:], curr + [nums[0]])
        exclude = self.subsets_rec(nums[1:], curr)

        return include + exclude
