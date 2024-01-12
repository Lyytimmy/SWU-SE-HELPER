n = 8  # 8×8的棋盘

chessboard = [[0] * n for _ in range(n)]  # 棋盘初始化
col = [0] * n  # 用于标记每一列是否放置了皇后
dia1 = [0] * (2 * n - 1)  # 正对角线方向
dia2 = [0] * (2 * n - 1)  # 反对角线方向

res = []  # 结果集


def backtrack(row):
    if row == n:  # 终止条件:棋盘放满
        temp = []
        for i in range(n):
            for j in range(n):
                if chessboard[i][j] == 1:
                    temp.append((i, j))
        res.append(temp)
        return True

    for i in range(n):  # 尝试放置每一列
        if col[i] == 0 and dia1[row + i] == 0 and dia2[row - i + n - 1] == 0:
            chessboard[row][i] = 1
            col[i] = 1
            dia1[row + i] = 1
            dia2[row - i + n - 1] = 1
            if backtrack(row + 1):  # 进入下一行放置皇后
                return True

            chessboard[row][i] = 0  # 回溯重置
            col[i] = 0
            dia1[row + i] = 0
            dia2[row - i + n - 1] = 0

    return False


backtrack(0)
print(res)