def encode(s):
    if len(s) == 0: return s
    board = []
    board.append(s)
    for i in range(1, len(s)):
        board.append(board[i-1][-1] + board[i-1][:len(s) - 1])
    board.sort()
    c, result = 0, ""
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

if __name__ == "__main__":
    a = None
    while a != 3:
        print("""What do you want to do?
        1. Encode
        2. Decode
        3. Exit
        Enter a number you need""")
        a = int(input())
        if a == 1:
            print("Enter a string you want to encode:")
            print(encode(input()))
        elif a == 2:
            print("Enter a encoded string:")
            s = input()
            print("Enter a number of row:")
            r = int(input())
            print(decode(s, r))
