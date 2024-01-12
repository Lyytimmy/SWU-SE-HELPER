# 物品类
class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value
        self.cost = value / weight


# 贪心算法求解0-1背包
def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x.cost, reverse=True)
    total_value = 0

    for item in items:
        if capacity <= 0:
            return total_value

        amount = min(item.weight, capacity)
        total_value += amount * item.cost
        capacity -= amount

    return total_value


# 测试
item1 = Item('A', 2, 3)
item2 = Item('B', 3, 4)
item3 = Item('C', 4, 5)
items = [item1, item2, item3]
capacity = 5

max_value = fractional_knapsack(items, capacity)
print(max_value)