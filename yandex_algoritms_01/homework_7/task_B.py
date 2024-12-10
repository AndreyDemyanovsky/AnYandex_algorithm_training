n, m = map(int, input().split())
result = [0] * m

events = []
in_segment = -1
out_segment = 1
is_point = 0

for _ in range(n):
	in_, out = map(int, input().split())
	if in_ > out:
		in_, out = out, in_
		
	events.append((in_, in_segment))
	events.append((out, out_segment))

dots = list(map(int, input().split()))
for index in range(len(dots)):
	events.append((dots[index], is_point, index))
events.sort()

count_segment = 0
for i in events:
	if i[1] == in_segment:
		count_segment += 1
	elif i[1] == is_point:
		result[i[2]] = count_segment
	else:
		count_segment -= 1

print(*result)