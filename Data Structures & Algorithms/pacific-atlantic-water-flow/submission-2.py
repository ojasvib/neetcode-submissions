class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    
        reachListPacific = set()
        reachListAtlantic = set()
        if not heights: return []
        r = len(heights)
        c = len(heights[0])
        reachListPacific.update((i, 0) for i in range(r))
        reachListPacific.update((0, j) for j in range(c))

        reachListAtlantic.update((i, c - 1) for i in range(r))
        reachListAtlantic.update((r - 1, j) for j in range(c))
        print(reachListAtlantic, reachListPacific)

        dir  = [[0,1],[-1,0],[1,0],[0,-1]]

        def dfs(i, j, oceanSet):
            for x,y  in dir:
                ni = x + i
                nj = y + j
                if ni >= r or nj >=c or ni < 0 or nj < 0 or (ni, nj) in oceanSet:
                    continue
                if heights[ni][nj] >= heights[i][j]:
                    oceanSet.add((ni,nj))
                    dfs(ni,nj, oceanSet)        
                    
        for i, j in list(reachListPacific):
            dfs(i, j, reachListPacific)

        for i, j in list(reachListAtlantic):
            dfs(i, j, reachListAtlantic)
        

        common = reachListPacific & reachListAtlantic
        return list(common)