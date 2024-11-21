class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue = []
        total_min = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    queue.append([i, j, 0])
        m = len(grid)
        n = len(grid[0])
        while(len(queue) != 0):
            r, c, minutes = queue.pop(0)
            for x, y in [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]:
             #for each of the 4 adjacent positions to the orange's position
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                    if grid[x][y] == 1:
                        total_min = minutes + 1
                        grid[x][y] = 2
                        queue.append([x, y, minutes + 1])
        for i in grid:
            if 1 in i:
                return -1
        return total_min