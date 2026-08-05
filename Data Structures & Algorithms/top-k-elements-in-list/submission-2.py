class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}

        for number in nums:
            if number not in frequency_map:
                frequency_map[number] = 1
            else:
                frequency_map[number] += 1

        buckets = [[] for i in range(len(nums) + 1)]

        for number, count in frequency_map.items():
            buckets[count].append(number)

        result = []

        for i in range(len(buckets) - 1, -1, -1):
            for number in buckets[i]:
                result.append(number)
                
                if len(result) == k:
                    return result