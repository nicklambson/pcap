def get_blocks(board):
    blocks = list()
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            block = list()
            for r in range(row, row + 3):
                for c in range(col, col + 3):
                    block.append(board[r][c])
            blocks.append(block)
    return blocks

def get_cols(board):
    columns = list()
    for i in range(0, 9):
        column = [row[i] for row in board]
        columns.append(column)
    return columns

def validate(to_check):
    for sub in to_check:
        if len(sub) != len(set(sub)):
            return "invalid"
        else:
            return "valid"
            
        
def print_board(board):
    print()
    for row in board:
        to_print = " ".join([str(x) for x in row])
        print(to_print)
    print()

test = """195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671"""

board = [[int(x) for x in row] for row in test.splitlines()]
rows = board.copy()
cols = get_cols(board)
blocks = get_blocks(board)

print_board(board)

print(f"rows are {validate(rows)}.")
print(f"columns are {validate(cols)}.")
print(f"blocks are {validate(blocks)}.")