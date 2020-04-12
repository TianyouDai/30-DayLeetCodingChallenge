class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
                return 0
        if len(stones) == 1:
            return stones[0]

        while True:
            stones = sorted(stones)
            num = stones[-1] - stones[-2]
            stones.pop()
            stones.pop()
            stones.append(num)
            if len(stones) == 0:
                return 0
            if len(stones) == 1:
                return stones[0]




        
