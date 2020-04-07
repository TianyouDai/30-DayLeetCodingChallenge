class Solution:
    def countElements(self, arr: List[int]) -> int:

        lookup = {}
        for i in arr:
            lookup[i] = True

        total = 0
        for n in arr:
            if n + 1 in lookup:
                total += 1

        return total
