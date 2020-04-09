class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        ss = []
        ts = []

        for c in S:
            if c == "#":
                if len(ss) != 0:
                    ss.pop()
            else:
                ss.append(c)

        for c in T:
            if c == "#":
                if len(ts) != 0:
                    ts.pop()
            else:
                ts.append(c)

        if ss == ts:
            return True
