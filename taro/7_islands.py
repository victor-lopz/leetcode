def count_islands(grid: list[list[int]]) -> int:
    """
    Time complexity: O(n*m) - DFS
    Space complexity: O(n*m) - recursion stack
    """
    if not grid or not grid[0]:
        raise ValueError("Input parameter 'grid' cannot by empty.")
    
    def dfs(pos_x: int, pos_y: int) -> None:
        if not grid[pos_x][pos_y]:
            return
        grid[pos_x][pos_y] = 0 # Mark as visited
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        for dx, dy in directions:
            is_neighbour_inbounds = 0 <= pos_x + dx < len(grid) \
                                and 0 <= pos_y + dy < len(grid[0])
            if is_neighbour_inbounds:
                dfs(pos_x + dx, pos_y + dy)
    
    num_islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                num_islands += 1
                dfs(i, j)
    return num_islands

def test_count_two_islands() -> None:
    grid = [
        [0, 1],
        [1, 0]
    ]
    num_islands = count_islands(grid)
    print("islands = ", num_islands)

def test_count_one_island() -> None:
    grid = [
        [0, 1],
        [1, 1]
    ]
    num_islands = count_islands(grid)
    print("islands = ", num_islands)

def test_count_more_islands() -> None:
    grid = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1]
    ]
    num_islands = count_islands(grid)
    print("islands = ", num_islands)

if __name__ == "__main__":
    test_count_two_islands()
    test_count_one_island()
    test_count_more_islands()