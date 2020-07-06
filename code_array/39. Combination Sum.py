class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        self.DFS(candidates, target, 0, [], res)
        return res
    
    def DFS(self, candidates, target, index, path, res):
        length = len(candidates)

        for i in range(index, length):
            remain = target - candidates[i]
            if remain < 0 :
                break
            # 目標達成 回傳res
            if remain == 0:
                res.append(path + [candidates[i]])
                break
            self.DFS(candidates, remain, i, path+ [candidates[i]], res)