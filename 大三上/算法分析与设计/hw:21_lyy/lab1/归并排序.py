import random
import time

"""
设计思路：题目要求取消栈空间的需要，其实是要求不能使用递归，因为递归会需要调用栈来保存中间信息。自底而上就是二二归并、四四归并
        所以就是从最底层而二归并，两个元素两个元素排序，然后四个四个排序，最后排序一次即可
"""


def GenerateArray(size):
    array = []
    for i in range(size):
        array.append(random.randint(0, 20))
    print(f'未排序前：', array)
    return array


def Sort_bottom_up(arr):
    size = 2
    while size <= len(arr):
        left, right = 0, size - 1
        while right <= len(arr) - 1:
            merge(arr, left, right)
            left += size
            right += size
        size *= 2


def merge(arr, left, right):
    n1 = []
    n2 = []
    if right - left == 1:
        n1.append(arr[left])
        n2.append(arr[right])
    else:
        mid = (left + right - 1) // 2
        n1 = arr[left:mid + 1]
        n2 = arr[mid + 1:right + 1]
    i, j, k = 0, 0, left
    while i < len(n1) and j < len(n2):
        if n1[i] <= n2[j]:
            arr[k] = n1[i]
            i += 1
        else:
            arr[k] = n2[j]
            j += 1
        k += 1
    while i < len(n1):
        arr[k] = n1[i]
        i += 1
        k += 1
    while j < len(n2):
        arr[k] = n2[j]
        j += 1
        k += 1


def main():
    size = 8
    array = GenerateArray(size)
    array2 = array
    start = time.time()
    Sort_bottom_up(array)
    print("排序好了：", array)
    end = time.time()
    print("所需时间", end - start)
    start = time.time()
    array2.sort()
    end = time.time()
    print("不使用算法进行排序时间", end - start)


if __name__ == '__main__':
    main()
