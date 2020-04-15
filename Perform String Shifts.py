class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        ml = 0
        length = len(s)
        for direction, step in shift:
            if direction == 0:
                ml += step
            else:
                ml -= step
        ml = ml % length
        return s[ml:] + s[:ml]
                
