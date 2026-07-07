import unittest

def max_profit(prices: list[int]) -> int:
    """Computes the maximum profit of buying the stock on a single day 
    and selling in on a different day in the future.
    Time complexity: O(n), where n=len(prices).
    Space complexity: O(1).
    Args:
        prices: array containing the prices of a stock (prices[i] >= 0)
    Returns:
        The maximum profit or 0 if there is no profit.
    Example:
        >>> max_profit([7,1,5,3,6,4])
        5
    """
    if len(prices) < 2:
        return 0
    profit = 0
    min_price = prices[0]
    for price in prices[1:]:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)
    return profit

class MaxProfitTestCase(unittest.TestCase):
    
    def test_empty_array(self) -> None:
        self.assertEqual(0, max_profit([]))
    
    def test_one_price(self) -> None:
        self.assertEqual(0, max_profit([5]))
    
    def test_positive_profit(self) -> None:
        self.assertEqual(6, max_profit([5,1,7,3,5,6]))
    
    def test_zero_profit(self) -> None:
        self.assertEqual(0, max_profit([5,4,3,2,1]))
    
    def test_example1(self) -> None:
        self.assertEqual(5, max_profit([7,1,5,3,6,4]))
    
    def test_example2(self) -> None:
        self.assertEqual(0, max_profit([7,6,4,3,1]))    

if __name__ == "__main__":
    unittest.main()