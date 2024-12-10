# n, l = map(int, input().split())

# seq = []
# for _ in range(n):
#     seq.append(list(map(int, input().split())))


# def merged(list1, list2):
#     merged_list = []
#     pl1 = 0
#     pl2 = 0
#     while len(merged_list) < l:
#         if list1[pl1] <= list2[pl2]:
#             merged_list.append(list1[pl1])
#             pl1 += 1
#         else:
#             merged_list.append(list2[pl2])
#             pl2 += 1
#     return merged_list[-1]


# for i in range(n):
#     for j in range(i + 1, n):
#         print(merged(seq[i], seq[j]))
