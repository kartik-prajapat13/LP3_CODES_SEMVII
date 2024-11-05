class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

class Solution:
    # Function to solve 0-1 Knapsack problem using Dynamic Programming
    def knapsack(self, capacity, items):
        n = len(items)
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for w in range(capacity + 1):
                if items[i - 1].weight <= w:
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - items[i - 1].weight] + items[i - 1].value)
                else:
                    dp[i][w] = dp[i - 1][w]

        return dp[n][capacity]

if __name__ == '__main__':
    # Take user input for the number of items
    n = int(input("Enter the number of items: "))
    
    items = []
    for i in range(n):
        value = int(input(f"Enter the value of item {i + 1}: "))
        weight = int(input(f"Enter the weight of item {i + 1}: "))
        items.append(Item(value, weight))
    
    # Take user input for the capacity of the knapsack
    capacity = int(input("Enter the capacity of the knapsack: "))
    
    obj = Solution()
    max_value = obj.knapsack(capacity, items)
    print("The maximum value that can be obtained is:", max_value)
