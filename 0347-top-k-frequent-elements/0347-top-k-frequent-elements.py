class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies
        a = Counter(nums)
        # Get the k most common elements as a list of (element, count) pairs
        most_common = a.most_common(k)
        # Extract just the elements (keys), ignoring counts
        return [item[0] for item in most_common]