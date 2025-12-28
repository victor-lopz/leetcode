import unittest

class IrregularShapeError(Exception):
    pass

def count_islands(grid: list[list[int]]) -> int:
    """
    Counts how many islands are on the grid.
    An island is a contiguous (horizontally or vertically, but not diagonally)
    collection of land cells, which are marked with the integer 1.
    Other cells are water and are marked with the integer 0.
    
    Time complexity: O(n*m) - Traverse all the grid in O(n*m) time + DFS, which
                              has O(n*m) complexity in the worst case.
    Space complexity: O(n*m) - for the visited array. The stack could also need n*m space
                                in the worst case, when all cells are land.
    """
    if not grid or not grid[0]:
        return 0
    n = len(grid)
    m = len(grid[0])
    for i in range(1, n):
        if m != len(grid[i]):
            raise IrregularShapeError("All rows of 'grid' must be of the same length.")
        
    num_islands = 0
    stack = []
    visited = [[False] * m for i in range(n)]
    directions = ((1,0), (-1,0), (0,1), (0,-1))
    
    def can_visit(row: int, col: int) -> bool:
        return 0 <= row < n and 0 <= col < m and not visited[row][col] and grid[row][col] == 1
    
    def dfs(pos_x: int, pos_y: int) -> None:
        visited[pos_x][pos_y] = True
        stack.append((pos_x, pos_y))
        while stack:
            pos_x, pos_y = stack.pop()
            for dx, dy in directions:
                new_x = pos_x + dx
                new_y = pos_y + dy
                if can_visit(new_x, new_y):
                    visited[new_x][new_y] = True
                    stack.append((new_x, new_y))
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] == 1:
                num_islands += 1
                dfs(i, j)
    return num_islands

class CountIslandsTestCase(unittest.TestCase):
    
    def test_one_big_island(self) -> None:
        grid = [
            [1,1,1,1,0],
            [1,1,0,1,0],
            [1,1,0,0,0],
            [0,0,0,0,0]
        ]
        self.assertEqual(1, count_islands(grid))
    
    def test_count_two_small_islands(self) -> None:
        grid = [
            [0, 1],
            [1, 0]
        ]
        self.assertEqual(2, count_islands(grid))

    def test_count_one_small_island(self) -> None:
        grid = [
            [0, 1],
            [1, 1]
        ]
        self.assertEqual(1, count_islands(grid))

    def test_dont_count_diagonal_land(self) -> None:
        grid = [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1]
        ]
        self.assertEqual(3, count_islands(grid))
    
    def test_empty_grid(self) -> None:
        self.assertEqual(0, count_islands([]))
        self.assertEqual(0, count_islands([[]]))
    
    def test_all_water(self) -> None:
        grid = [
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(0, count_islands(grid))
        self.assertEqual(0, count_islands([[0]]))
    
    def test_all_land(self) -> None:
        grid = [
            [1, 1, 1],
            [1, 1, 1]
        ]
        self.assertEqual(1, count_islands(grid))
        self.assertEqual(1, count_islands([[1]]))
    
    def test_row(self) -> None:
        self.assertEqual(2, count_islands([[1, 0, 1]]))
    
    def test_column(self) -> None:
        self.assertEqual(2, count_islands([[1], [0], [1]]))

    def test_performance(self) -> None:
        n, m = 300, 300
        land_grid = [[1 for i in range(n)] for j in range(m)]
        self.assertEqual(1, count_islands(land_grid))
        water_grid = [[0 for i in range(n)] for j in range(m)]
        self.assertEqual(0, count_islands(water_grid))
    
    def test_big_diagonal_grid(self) -> None:
        n = 300
        diag_grid = [[0 if i != j else 1 for j in range(n)] for i in range(n)]
        self.assertEqual(n, count_islands(diag_grid))
    
    def test_throws_error_irregular_shape(self) -> None:
        grid = [
            [1, 1],
            [0]
        ]
        self.assertRaises(IrregularShapeError, count_islands, grid)

if __name__ == "__main__":
    unittest.main()