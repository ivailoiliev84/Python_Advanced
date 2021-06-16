def create_matrix(n):
    matrix = []

    for i in range(int(n)):
        matrix.append([x for x in input()])
    return matrix


# return list from tuples with(row, column) , horses position
def find_horses_position(horses_index):
    position = []
    for i in range(len(horses_index)):
        for j in range(len(horses_index)):
            if horses_index[i][j] == "K":
                position.append((i, j))
    return position


def are_attacking_each_oder(matrix):
    for i, j in find_horses_position(matrix):
        movies = [
            (i + 1, j + 2),
            (i + 2, j + 1),
            (i + 2, j - 1),
            (i + 1, j - 2),
            (i - 2, j + 1),
            (i - 2, j - 1),
            (i - 1, j - 2),
            (i - 1, j + 2)
        ]

        for el in movies:
            row, cow = el
            if not 0 <= row <= len(matrix) - 1:
                continue
            if not 0 <= cow <= len(matrix) - 1:
                continue

            if matrix[row][cow] == "K":
                return True
    return False


# return dictionary key = tuple from horse position , value = count of horses which  attack
def the_most_aggressive(attacks):
    most_aggressive = {}
    for i, j in find_horses_position(attacks):
        movies = [
            (i + 1, j + 2),
            (i + 2, j + 1),
            (i + 2, j - 1),
            (i + 1, j - 2),
            (i - 2, j + 1),
            (i - 2, j - 1),
            (i - 1, j - 2),
            (i - 1, j + 2)
        ]

        for el in movies:
            row, cow = el
            if not 0 <= row <= len(attacks) - 1:
                continue
            if not 0 <= cow <= len(attacks) - 1:
                continue

            if attacks[row][cow] == "K":

                if (i, j) not in most_aggressive:
                    most_aggressive[(i, j)] = 1
                else:
                    most_aggressive[(i, j)] += 1

    return most_aggressive


def find_the_most_aggressive(dict_aggression):
    max_attacks = None
    pos = None

    for key, value in the_most_aggressive(dict_aggression).items():
        if max_attacks is None or max_attacks < value:
            max_attacks = value
            pos = key

    return pos


def main():
    delete_horses_count = 0
    board = create_matrix(input())
    while are_attacking_each_oder(board):
        most_aggressor = find_the_most_aggressive(board)
        row, cow = most_aggressor
        board[row][cow] = "0"
        delete_horses_count += 1

    print(delete_horses_count)


main()

