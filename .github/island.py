def count_islands(map_grid):
    if not map_grid:
        return 0
    
    rows = len(map_grid)
    cols = len(map_grid[0])
    visited = [[False] * cols for _ in range(rows)]
    
    def dfs(r, c):
        
        if r < 0 or r >= rows or c < 0 or c >= cols or map_grid[r][c] == 'W' or visited[r][c]:
            return
        
        visited[r][c] = True
       
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    island_count = 0
    
    for i in range(rows):
        for j in range(cols):
            if map_grid[i][j] == 'L' and not visited[i][j]:
               
                island_count += 1
                dfs(i, j)  

    return island_count


dispatch_1 = [
    ["L","L","L","L","W"],
    ["L","L","W","L","W"],
    ["L","L","W","W","W"],
    ["W","W","W","W","W"],
]

dispatch_2 = [
    ["L","L","W","W","W"],
    ["L","L","W","W","W"],
    ["W","W","L","W","W"],
    ["W","W","W","L","L"],
]

print(count_islands(dispatch_1))  
print(count_islands(dispatch_2)) 
