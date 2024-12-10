
def get_all_possible_permutations(n, count_dino,
                                   dino_positions=None,
                                  lst_diagonal_difference=None, lst_diagonal_sum=None,
                                  number_ways=0):
    if not lst_diagonal_difference:
        lst_diagonal_difference = []
    if not lst_diagonal_sum:
        lst_diagonal_sum = []
    if not dino_positions:
        dino_positions = []

    if count_dino == 0:
        return number_ways + 1

    for i in range(n):
        diagonal_difference = i - len(dino_positions)
        diagonal_sum = len(dino_positions) + i
        if i not in dino_positions and \
                diagonal_difference not in lst_diagonal_difference and diagonal_sum not in lst_diagonal_sum:

            count_dino -= 1
            dino_positions.append(i)
            lst_diagonal_difference.append(diagonal_difference)
            lst_diagonal_sum.append(diagonal_sum)
            number_ways = get_all_possible_permutations(n, count_dino, dino_positions,
                                                        lst_diagonal_difference, lst_diagonal_sum, number_ways)
            dino_positions.pop()
            lst_diagonal_difference.pop()
            lst_diagonal_sum.pop()
            count_dino += 1

    return number_ways


N = int(input())
print(get_all_possible_permutations(N, N))


# def check(n, row, col, matrix):
#
#     for i in range(n):
#         for j in range(n):
#             if i - j == row - col or i + j == row + col or i == row or j == col:
#                 if matrix[i][j] == "Q":
#                     return False
#     return True
#
#
# def get_all_possible_permutations(n, count_dino, matrix, dino_positions=None, number_ways=0):
#     if not dino_positions:
#         dino_positions = []
#     if count_dino == 0:
#         return number_ways + 1
#
#     for i in range(n):
#         if i not in dino_positions:
#             if check(n, len(dino_positions), i, matrix):
#                 matrix[len(dino_positions)][i] = "Q"
#                 count_dino -= 1
#                 dino_positions.append(i)
#                 number_ways = get_all_possible_permutations(n, count_dino, matrix, dino_positions, number_ways)
#                 dino_positions.pop()
#                 count_dino += 1
#                 matrix[len(dino_positions)][i] = "_"
#
#     return number_ways
#
#
# N = int(input())
# matrix_out = [["-" for _ in range(N)] for _ in range(N)]
# print(get_all_possible_permutations(N, N, matrix_out))