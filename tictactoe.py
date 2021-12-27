def print_board(field: list) -> None:
    c = 2
    for row in field:
        print(f"{row[0]} | {row[1]} | {row[2]}")
        if c > 0:
            print("-" * 9)
            c -= 1
    print('\n')


def possible_moves(field: list) -> bool:
    for row in field:
        for col in row:
            if col == ' ':
                return True
    return False


# make a move if possible else return false (positions are like on numpad)
def make_move(field: list, symbol: str, pos: int) -> bool:
    positions = [(2, 0), (2, 1), (2, 2), (1, 0), (1, 1),
                 (1, 2), (0, 0), (0, 1), (0, 2)]
    row, column = positions[pos - 1]
    if field[row][column] == ' ':
        field[row][column] = symbol
        return True
    else:
        return False


def check_win(field: list, current_symbol: str) -> bool:
    # vertical
    for i in range(3):
        if field[i][0] == current_symbol:
            if field[i][0] == field[i][1] and field[i][1] == field[i][2]:
                return True
    # horizontal
    for i in range(3):
        if field[0][i] == current_symbol:
            if field[0][i] == field[1][i] and field[1][i] == field[2][i]:
                return True
    # diagonal
    if field[1][1] == current_symbol:
        return (field[0][0] == field[1][1] and field[1][1] == field[2][2]) or (field[0][2] == field[1][1] and field[1][1] == field[2][0])
    return False


# main function for game
def play(field: list, symbol_one: str, symbol_two: str) -> int:
    turn = 0
    symbol = ''
    while True:
        if not possible_moves(field):
            return 0
        if turn % 2 == 0:
            symbol = symbol_one
        else:
            symbol = symbol_two
        while True:
            try:
                pos = int(
                    input(f"Player {(turn % 2) + 1} enter your position: "))
                if make_move(field, symbol, pos):
                    break
            except:
                print("invalid position!")
        print_board(field)
        if check_win(field, symbol):
            return 1 if symbol == symbol_one else 2
        turn = (turn + 1) % 2


if __name__ == '__main__':
    # let users pick a custom symbol
    user_symbols = []
    for i in range(1, 3):
        symbol = input(f"Player {i} choose your symbol (1 character): ")
        assert len(symbol) == 1, "Symbol must be 1 character!"
        user_symbols += symbol
    # loop for game
    while True:
        field = [[' ' for _ in range(3)] for _ in range(3)]
        game = play(field, user_symbols[0], user_symbols[1])
        if game == 0:
            print('\033[93m' + "Tie!" + '\033[0m')
        elif game == 1:
            print('\033[92m' + "Player 1 has won!" + '\033[0m')
        elif game == 2:
            print('\033[92m' + "Player 2 has won!" + '\033[0m')
        else:
            raise Exception

        again = input("Want to play again? (y/n): ")
        if again in ['n', 'N']:
            break
