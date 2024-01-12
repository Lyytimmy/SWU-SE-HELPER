import numpy as np
import random

"""
设计思路：棋盘覆盖问题中，有一个特殊方块固定占据一块位置。我们可以通过在特点位置增加三个可以组成一个L形骨牌的特殊方块，这样就得到了四个带有一个特殊
色块的棋盘。先用8*8的棋盘作为演示, 0代表空白棋盘，9代表特殊方块，1-8代表L形状骨牌
"""


def GenerateBoard():
    board = np.zeros((8, 8), dtype=int)
    i = random.randint(0, 7)
    j = random.randint(0, 7)
    board[i, j] = 9
    return board


def DivideStrategy(Board, increment, lastL):
    increment += 1  # 根据递归深度添加不同的L骨牌
    if increment == 1:  # 第一次是9，其余的等于自身
        L = lastL[-1]
    else:
        L = increment
    a = int(len(Board) / 2)  # 棋盘大小的一半，用来切割大棋盘
    board1 = Board[:a, :a]  # 左上
    board2 = Board[:a, a:]  # 右上
    board3 = Board[a:, :a]  # 左下
    board4 = Board[a:, a:]  # 右下

    for i in range(1, 4):
        if np.any(np.isin(board1, lastL)):
            board2[-1][0] = L
            board3[0][-1] = L
            board4[0][0] = L
            break
        if np.any(np.isin(board2, lastL)):
            board1[-1][-1] = L
            board3[0][-1] = L
            board4[0][0] = L
            break
        if np.any(np.isin(board3, lastL)):
            board1[-1][-1] = L
            board2[-1][0] = L
            board4[0][0] = L
            break
        if np.any(np.isin(board4, lastL)):
            board1[-1][-1] = L
            board2[-1][0] = L
            board3[0][-1] = L
            break
    lastL.append(L)
    if len(board1) > 1:
        DivideStrategy(board1, increment, lastL)
        DivideStrategy(board2, increment, lastL)
        DivideStrategy(board3, increment, lastL)
        DivideStrategy(board4, increment, lastL)


def main():
    Board = GenerateBoard()
    increment = 0
    DivideStrategy(Board, increment, [9])
    print(Board)


if __name__ == '__main__':
    main()

"""
def DivideStrategy(Board, increment, lastL):
    increment += 1  # 根据递归深度添加不同的L骨牌
    if increment == 1:  # 第一次是9，其余的等于自身
        L = 9
    else:
        L = increment
    a = int(len(Board) / 2)  # 棋盘大小的一半，用来切割大棋盘
    board1 = Board[:a, :a]  # 左上
    board2 = Board[:a, a:]  # 右上
    board3 = Board[a:, :a]  # 左下
    board4 = Board[a:, a:]  # 右下

    for i in range(1, 4):
        if lastL in board1:
            board2[-1][0] = L
            board3[0][-1] = L
            board4[0][0] = L
            break
        if lastL in board2:
            board1[-1][-1] = L
            board3[0][-1] = L
            board4[0][0] = L
            break
        if lastL in board3:
            board1[-1][-1] = L
            board2[-1][0] = L
            board4[0][0] = L
            break
        if lastL in board4:
            board1[-1][-1] = L
            board2[-1][0] = L
            board3[0][-1] = L
            break
    if len(board1) > 1:
        DivideStrategy(board1, increment, L)
        DivideStrategy(board2, increment, L)
        DivideStrategy(board3, increment, L)
        DivideStrategy(board4, increment, L)
        
输出：
[[3 3 3 3 3 3 3 3]
 [3 2 2 3 3 2 2 3]
 [3 2 0 0 0 0 2 3]
 [3 3 0 9 9 0 3 3]
 [3 3 3 3 9 0 3 3]
 [3 2 2 3 0 0 2 3]
 [3 2 0 0 3 2 2 3]
 [3 3 0 9 3 3 3 3]]

原因以及解决思路：
1. 通过输出结果会发现第一次做递归时添加的9的周围永远是0，这是因为判断lastL在哪时，永远不会处理有lastL的那一块。
2. 按理说，就算你没有处理9周围的空白格子，在接下来递归时也应该会把9周围的空白格子填满，但并没有。这是因为递归到9周围的空白格子时，9已经不是lastL
   因此用一个数组来表示lastL，只要子棋盘有lastL中的任意一个元素在里面都要进行处理
"""
