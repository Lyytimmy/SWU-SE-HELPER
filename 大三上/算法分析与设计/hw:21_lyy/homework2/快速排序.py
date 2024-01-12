import random

"""
合并排序详见lab1
快速排序原理：
选取一个基准值，一般选择数组的第一个元素。然后设置两个索引i,j，一个指向数第一个元素，一个指向数组的最后一个元素。
然后i向右移动，找到第一个比基准值大的元素，j向左移动，找到第一个比基准值小的元素，让i,j元素位置交换，
直到i=j。此时，i和j的位置为k，交换k与基准值的位置。此时，基准值左边的值比基准值小，基准值右边的值比基准值大，但顺序不一定是正确的。然后需要对基准值
两边的元素做同样的排序，直到每个部分只有一个值。
详见：
http://data.biancheng.net/view/117.html
https://blog.csdn.net/wthfeng/article/details/78037228
"""


def generateArray():
    array = []
    for i in range(8):
        array.append(random.randint(0, 100))
    print(f'未排序的数组： {array}')
    return array


def QuickSort(arr, i, j):
    if i < j:
        jizhun = arr[i]
        left, right = i, j
        while i < j:
            # j的停止条件：找到第一个比基准值小的元素
            while arr[j]>jizhun and i < j:
                j -= 1
            # i的停止条件：找到第一个比基准值大的元素
            while arr[i]<jizhun and i < j:
                i += 1
            arr[i], arr[j] = arr[j], arr[i]
        k = i
        # 交换基准值与位置为k的值
        arr[k], jizhun = jizhun, arr[k]
        # k左边
        QuickSort(arr, left, k - 1)
        # k右边
        QuickSort(arr, k + 1, right)


def main():
    array = generateArray()
    QuickSort(array, 0, len(array)-1)
    print(f'排序后的数组 {array}')


if __name__ == "__main__":
    main()
