class Solution:
    def isHappy(self, n: int) -> bool:
        d = {}
        return self.check(d, n)

    def check(self, d, n):
        # Accept dict and number return isHappy as boolean
        if n == 1:
            return True
        if n in d:
            return False
        d[n] = True
        return self.check(d, self.sum(n))

    def sum(self, n):
        # Return sum of squares of n. Where n is an int
        list(str(n))
        val = [int(x) for x in str(n)]
        _sum = 0
        for i in val:
            _sum += i * i

        return _sum
