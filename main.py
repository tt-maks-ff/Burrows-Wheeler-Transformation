def encode(s):
    if len(s) == 0: return s
    board = []
    board.append(s)
    for i in range(1, len(s)):
        board.append(board[i-1][-1] + board[i-1][:len(s) - 1])
    board.sort()
    c, result = 0, ''
    for i in range(len(s)):
        result += board[i][-1]
        if board[i] == s: c = i
    return (result, c)

def decode(s, n):
    board = [char for char in s]
    board.sort()
    for _ in range(len(s) - 1):
        for i in range(len(s)):
            board[i] = s[i] + board[i]
        board.sort()
    return board[n]
