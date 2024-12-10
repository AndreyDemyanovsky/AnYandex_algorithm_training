n, d = map(int, input().split())
START, END = 1, 2
coordinates = list(map(int, input().split()))

events = []
for i in range(len(coordinates)):
	x = coordinates[i]
	events.append((x, START, i))
	events.append((x + d, END, i))
events.sort()

method_distributing_tickets = [0] * n
free_tickets = []
variants = 0

for i in events:

	if i[1] == START:

		if not free_tickets:
			variants += 1
			n_tic = variants
		else:
			n_tic = free_tickets.pop()

		method_distributing_tickets[i[2]] = n_tic

	elif i[1] == END:
		n_tic = method_distributing_tickets[i[2]]
		free_tickets.append(n_tic)

print(variants)
print(*method_distributing_tickets)