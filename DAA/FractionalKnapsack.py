class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

class Solution:
    def fractionalKnapsack(self, capacity, items):
        # Sort items based on value-to-weight ratio in descending order
        items.sort(key=lambda item: item.value / item.weight, reverse=True)
        
        total_value = 0.0
        for item in items:
            if capacity <= 0:  # If the capacity is full, break out of the loop
                break
            
            if item.weight <= capacity:
                capacity -= item.weight
                total_value += item.value
            else:
                total_value += item.value / item.weight * capacity
                capacity = 0  # All capacity is filled

        return total_value

if __name__ == '__main__':
    # Take user input for the number of items
    n = int(input("Enter the number of items: "))
    
    items = []
    for i in range(n):
        value = float(input(f"Enter the value of item {i + 1}: "))
        weight = float(input(f"Enter the weight of item {i + 1}: "))
        items.append(Item(value, weight))
    
    # Take user input for the capacity of the knapsack
    capacity = float(input("Enter the capacity of the knapsack: "))
    
    obj = Solution()
    max_value = obj.fractionalKnapsack(capacity, items)
    print("The maximum value is", max_value)



# Enter the number of items: 3
# Enter the value of item 1: 60
# Enter the weight of item 1: 10
# Enter the value of item 2: 100
# Enter the weight of item 2: 20
# Enter the value of item 3: 120
# Enter the weight of item 3: 30
# Enter the capacity of the knapsack: 50
