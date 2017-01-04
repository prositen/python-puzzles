def done_or_not(board):
    transposed = [[board[y][x] for y in range(9)] for x in range(9)]
    regions = [[board[x][y] for x in range(3*i, 3*(i+1)) for y in range(3*j, 3*(j+1))] for i in range(3) for j in range(3)]

    all_nums = list(range(1, 10))
    rows_done = all([sorted(board[x]) == all_nums for x in range(9)])
    cols_done = all([sorted(transposed[x]) == all_nums for x in range(9)])
    regions_done = all([sorted(regions[x]) == all_nums for x in range(9)])

    done = rows_done and cols_done and regions_done

    return "Finished!" if done else "Try again!"