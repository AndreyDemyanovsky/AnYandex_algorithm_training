import random
N = 0
data = [1, 9, 3, 3, 3,3, 3, 3, 3, 5, 12, 2]
x = 3

def partition(lst, x):
	eq = 0
	large = 0
	for now in range(len(lst)):
		if lst[now] < x:
			save = lst[now]# сохраняяем элемент меньше x
			lst[now] = lst[large]# в первую очередь переносим в настоящий индекс первый элемент >x
			lst[large] = lst[eq]# а где раньше был первый >x ставим первый =x
			lst[eq] = save# в свободное место ставим сохраненный элемент
			eq += 1
			large += 1
		if lst[now] == x:
			lst[large], lst[now] = lst[now], lst[large]
			large += 1
	 		
	return len(lst[:eq]), len(lst[large:])
	

print(*partition(data, x), sep="\n")
