class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0
        
        islands=0

        def dfs(r,c):
            if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]):
                return
            if grid[r][c] != "1":
                return

            grid[r][c]="#"

            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)



        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    islands+=1
                    dfs(r,c)

        return islands
        