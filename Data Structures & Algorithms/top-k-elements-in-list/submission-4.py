class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]


        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cut in count.items():
            freq[cut].append(num)
            # “把频率作为下标（Index），把出现这个频率的数字放进对应的桶（List）里。”

        res = []
        for i in range(len(freq) - 1, 0, -1):
          for num in freq[i]:
            res.append(num)
            if len(res) == k:
                return res


        
