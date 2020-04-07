from collections import Counter
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_dict = defaultdict( list )

        for s in strs:

            ordered_s = ''.join(sorted(s))

            anagram_dict[ordered_s].append( s )

        return anagram_dict.values()
