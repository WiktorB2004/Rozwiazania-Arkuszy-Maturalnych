import os
import re

# Check if there is and count empty columns on the board, also return highest amount of empty columns on one board
def check_empty_columns(boards):
    at_least_one_empty_column = 0
    most_empty_columns = 0

    for board in boards:
        empty_count = 0
        for i in range(0,8):
            column = []
            for l in range(0,8):
                column.append(board[l][i])
            if column.count('.') == 8:
                empty_count += 1
        if empty_count > 0:
            at_least_one_empty_column += 1

        most_empty_columns = max(empty_count, most_empty_columns)
        
    return [at_least_one_empty_column, most_empty_columns]

# Checks if the number of white and black pawns are equal
def same_white_and_black(boards):
    result = 0
    lowest_at_board = 100
    for board in boards:
        board_string = ''.join(board)
        black = re.findall('[a-z]', board_string)
        white = re.findall('[A-Z]', board_string)
        if sorted(black) == sorted(map(lambda x: x.lower(), white)):
            result += 1
            lowest_at_board = min(lowest_at_board, len(black)+len(white))
    
    return [result, lowest_at_board]

# Count white checks by tower and black checks by tower
def count_checks_by_tower(boards):
    white_check = 0
    black_check = 0
    
    for board in boards:
        #Check rows
        for row in board:
            if len(re.findall('[K]\W*[w]', row)):
                black_check += 1
            if len(re.findall('[w]\W*[K]', row)):
                black_check += 1
            if len(re.findall('[W]\W*[k]', row)):
                white_check += 1
            if len(re.findall('[k]\W*[W]', row)):
                white_check += 1
        # Check columns
        for i in range(0,8):
            column = []
            for l in range(0,8):
                column.append(board[l][i])
            column = ''.join(column)
            if len(re.findall('[K]\W*[w]', column)):
                black_check += 1
            if len(re.findall('[w]\W*[K]', column)):
                black_check += 1
            if len(re.findall('[W]\W*[k]', column)):
                white_check += 1
            if len(re.findall('[k]\W*[W]', column)):
                white_check += 1   
            
    return [white_check, black_check]

# Main function
def main():
    with open(os.path.join(os.path.dirname(__file__), './zalaczniki/szachy.txt'), 'r') as f:
        # Read data
        data = f.read().split()
        # Boards Array
        boards = []
        # Extract boards from dataset
        for i in range(0, len(data), 8):
            boards.append(data[i:i+8])

        # Solutions
        solution_1 = check_empty_columns(boards)
        solution_2 = same_white_and_black(boards)
        solution_3 = count_checks_by_tower(boards)

    # Write solutions to files
    with open(os.path.join(os.path.dirname(__file__), './zadanie1.1.txt'), 'w') as f:
        f.write(' '.join(map(str,solution_1)))
    with open(os.path.join(os.path.dirname(__file__), './zadanie1.2.txt'), 'w') as f:
        f.write(' '.join(map(str,solution_2)))
    with open(os.path.join(os.path.dirname(__file__), './zadanie1.3.txt'), 'w') as f:
        f.write(' '.join(map(str,solution_3)))
        
if __name__ == '__main__':
    main()