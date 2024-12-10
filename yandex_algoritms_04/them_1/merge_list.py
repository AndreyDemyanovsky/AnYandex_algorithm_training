N = int(input())
list_n = list(map(int, input()))
M = int(input())
list_m = list(map(int, input()))

# version 1
# def merge_lists(list_1: list[int], list_2: list[int]) -> list[int]:

#     result_list = []
#     while list_1 and list_2:
#         if list_1[0] <= list_2[0]:
#             result_list.append(list_1.pop(0))
#         else:
#             result_list.append(list_2.pop(0))

#     return result_list + (list_1 or list_2)

def merge_lists(list_1, list_2):

    result_list = []
    i = 0
    j = 0
    while i != len(list_1) and j != len(list_2):
        if list_1[i] <= list_2[j]:
            result_list += [list_1[i]]
            i += 1
        else:
            result_list += [list_2[j]]
            j += 1

    return result_list + list_1[i:] + list_2[j:]


print(*merge_lists([23, 44, 56, 124, 323, 542], [2, 5, 734]))