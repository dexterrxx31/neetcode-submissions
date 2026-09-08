class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            bucket[count].append(num)

        result = []

        for count in range(len(bucket) - 1, 0, -1):
            for nums in bucket[count]:
                result.append(nums)
                if len(result) == k:
                    return result

        return result
