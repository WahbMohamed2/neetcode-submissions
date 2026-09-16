from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cntr = Counter(nums)
        pairs = cntr.most_common(k)
        return [num for num, _ in pairs]