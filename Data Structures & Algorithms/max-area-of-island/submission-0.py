class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        maxArea=0
        visit=set()

        rows,cols= len(grid),len(grid[0])

        def dfs(r,c):
            if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c] != 1 or (r,c) in visit :
                return 0

            visit.add((r,c))

            return(1 + dfs(r-1,c) +
                        dfs(r+1,c)+
                        dfs(r,c-1)+
                        dfs(r,c+1))




        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea =max(maxArea, dfs(r,c))

        return maxArea
        