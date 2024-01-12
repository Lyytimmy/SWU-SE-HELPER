import random
import time

"""
非递归思路：遍历整个随机数组，将所有1序列装入大数组中，在遍历大数组中的1序列进行分析。
递归思路： 递归出口为索引超过数组长度，此时遍历完整个数组。详见代码注释。
"""


def CreateArray(size):
    array = []
    for i in range(size):
        array.append(random.randint(0, 1))
    print(array)
    return array


# 不使用递归
def UnRecursion(array):
    OneArray = []
    size = len(array)
    temp = []
    target_num = 0
    for i in range(size):
        if array[i] == 1:
            temp.append(array[i])
        elif array[i] == 0 and temp:
            OneArray.append(temp)
            temp = []
    if temp:
        OneArray.append(temp)
    for array in OneArray:
        # print(array)
        if len(array) % 2 == 0:
            target_num += 1
    print(f'有{target_num}个连续1序列是偶数大小，有{len(OneArray) - target_num}连续1序列是奇数大小')


# 使用递归
def CountOne(array, index):
    count = 0
    while index < len(array) and array[index] == 1:
        count += 1
        index += 1

    return count


def Recursion(array, index):
    if index >= len(array):
        return True  # 为什么当index大于数组长度时返回True呢，因为如果能正常到数组结尾，要么是全为0，要么都是偶数1序列
    if array[index] == 0:
        Recursion(array, index + 1)  # 如果为0，直接递归到下一个索引
    if array[index] == 1:
        count = CountOne(array, index)  # 如果为1，开始计数，并且index+1
        if count % 2 == 0:
            return Recursion(array, index + count)  # 如果计数为偶数，继续使用递归并跳过被计数的部分
    else:
        return False  # 如果存在count为奇数，返回False


def main():
    size = 50
    array = CreateArray(size)
    start = time.time()
    UnRecursion(array)
    end = time.time()
    print('使用非递归算法：', end - start)
    start = time.time()
    result = Recursion(array, 0)
    print('是否全为偶数序列', result)
    end = time.time()
    print('使用递归算法', end - start)


if __name__ == '__main__':
    main()
