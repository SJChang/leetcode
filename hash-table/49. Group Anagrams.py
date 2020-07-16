class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
           
        res = collections.defaultdict(list)
        for word in strs:
            sorted_str = ''.join(sorted(word))
            res[sorted_str].append(word)
        return res.values()