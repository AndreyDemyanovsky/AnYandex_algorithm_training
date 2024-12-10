number_of_tasks, k = map(int, input().split())
task_direction = list(map(int, input().split()))
task_direction.sort()

result = 1
l = 1
r = 0
save_list = [task_direction[0] + k +1]

while l < len(task_direction):

    if task_direction[l] >= save_list[r]:
        save_list.append(task_direction[l] + k + 1)
        r += 1
    else:
        result += 1
        save_list.append(task_direction[l] + k + 1)

    l += 1

print(result)