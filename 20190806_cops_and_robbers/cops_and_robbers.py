from queue import Queue

def cops_and_robbers(board):
    ROBBERS = "robbers"
    COPS = "cops"
    board_size = len(board)
    if board[0][0] == 1:
        return ROBBERS

    def find_way():
        visited = {}
        my_queue = Queue()
        my_queue.put((0, 0))
        while not my_queue.empty():
            x, y = my_queue.get()
            if visited.get((x, y)):
                continue
            visited[(x, y)] = True
            if x < board_size-1 and board[x+1][y] == 0: # middle_right
                my_queue.put((x+1, y))
            if x > 0 and board[x-1][y] == 0:
                my_queue.put((x-1, y))
            if y > 0 and board[x][y-1] == 0:
                my_queue.put((x, y-1))
            if y < board_size-1 and board[x][y+1] == 0: # bottom_right
                my_queue.put((x, y+1))
        return visited.get((board_size-1, board_size-1))

    return COPS if find_way() else ROBBERS
