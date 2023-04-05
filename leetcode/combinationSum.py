def combinationSum(candidates, target):
    res = []

    def dfs(i, curr, total):
        if total == target:
            res.append(curr.copy())
            return 
        if i >= len(candidates) or total > target:
            return 
        
        #if we include candinate[i]
        curr.append(candidates[i])
        dfs(i, curr, total + candidates[i])
        curr.pop()
        #if we exclude the candiante[i]
        dfs(i+1, curr, total)
    
    dfs(0,[], 0)

    return res

        
        


# Input: candidates = [2,3,6,7], target = 7
#Output: [[2, 2,3],[7]]
candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates, target))
