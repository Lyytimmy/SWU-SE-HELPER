import math
import random
import time

"""
实现思路：
- 设置x
- 生成一个0-x的数组
- 生成一个范围在0-x的目标值
- 用递归思想写一个查找函数。递归出口为找到了目标值，如果不是则分两种情况:
    大于目标值时，向前切割数组，在新数组中继续使用查找函数；反之，向后切割；
"""


def CreateArray(x):
    array = []
    for i in range(x):
        array.append(random.randint(0, x))
    array.sort()
    return array


def search(array, aim):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == aim:
            return mid
        elif array[mid] < aim:
            left = mid + 1
        else:
            right = mid - 1


def main():
    x = 1000
    array = CreateArray(x)
    aim = random.randint(0, x)
    print(f'我们的目标是{aim}')
    start = time.time()
    search(array, aim)
    end = time.time()
    print('使用分治算法: ', end - start)
    start = time.time()
    for i in range(x):
        if array[i] == aim:
            break
    end = time.time()
    print('不使用分治算法: ', end - start)


if __name__ == '__main__':
    main()

"""
遇到了问题：不使用二分查找算法直接使用循环找更快
修改思路：
1. 优化二分查找算法
2. 不使用0-99这种简单数组
"""

"""
原始版本
def search(array, aim):
    index = math.ceil(len(array) // 2)
    if array[index] == aim:
        print(f'我们找到了{aim}')
    elif array[index] < aim:
        new_array = array[index:]
        search(new_array, aim)
    else:
        new_array = array[:index]
        search(new_array, aim)

全新版本
def search(array, aim):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == aim:
            return mid
        elif array[mid] < aim:
            left = mid + 1
        else:
            right = mid - 1
优化点：
- 使用循环代替迭代，减少函数调用带来的开销
- 使用运算符计算来计算索引，避免使用数组切片减小开销
- mid = left + (right - left) // 2 这种计算方式相比于直接相加可以避免边界相差过大导致的溢出
"""

"""
- 使用分治算法不一定比不使用分治算法快，这个是多方面的因素决定的。
- 分治策略不等于递归，二分法强制要求递归
"""