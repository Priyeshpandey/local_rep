t = int(input())


def print_map(arr, n):
    for i in range(n):
        print(arr[i])


def capture(points, board, x, y, player):
    print_map(board, len(board))
    print('=='*20)
    if (x, y) in points and board[x-1][y-1] == '1':
        board[x-1][y-1] = player
        target = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        sum = 0
        for point in target:
            sum += capture(points, board, point[0], point[1], player)
        return 1 + sum
    else:
        return 0


def uncapture(points, board, x, y, player):
    print_map(board, len(board))
    print('==' * 20)
    if (x, y) in points and board[x-1][y-1] == player:
        board[x-1][y-1] = '1'
        target = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        for point in target:
            uncapture(points, board, point[0], point[1], player)


def explorer(points, board, player):
    max_count = 0
    for point in points:
        count = capture(points, board, point[0], point[1], player)
        if count > max_count:
            max_count = count
        else:
            uncapture(points, board, point[0], point[1], player)
    return max_count


for _ in range(t):
    n, m = map(int, input().split())  # n rows, m columns
    board = []
    for i in range(n):
        x = input()
        x_list = [i for i in x]
        board.append(x_list)
    points = set()
    max_captures = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == '1':
                points.add((i + 1, j + 1))
                max_captures += 1
    play = {
        'Mike': '2',
        'Chef': '3'
    }
    player = play['Chef']
    chef_captures = 0
    mike_captures = 0
    total_capture = 0
    while total_capture < max_captures:
        print_map(board, n)
        print('=='*20)
        player = play['Mike'] if player != play['Mike'] else play['Chef']
        capture_count = explorer(points, board, player)
        total_capture += capture_count
        if player == '3':
            chef_captures += capture_count
    print(chef_captures)
