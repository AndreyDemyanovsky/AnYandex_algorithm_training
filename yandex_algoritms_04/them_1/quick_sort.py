from random import randint, seed


N = int(1)
list_number = list(map(int,"1 1 1 1 0 -2 324 25 -34 5 -356 256 -34 3 3 4 534 3 -23 -6 -3 -2".split()))

def partition(lst, x):
	eq = 0
	large = 0
	for now in range(len(lst)):
		if lst[now] < x:
			save = lst[now]# сохраняяем элемент меньше x
			lst[now] = lst[large]# в первую очередь переносим в настоящий индекс первый элемент >x
			lst[large] = lst[eq]# а где раньше был первый >x ставим первый =x
			lst[eq] = save# в свободное место ставим сохранный элемент
			eq += 1
			large += 1
		elif lst[now] == x:
			lst[large], lst[now] = lst[now], lst[large]
			large += 1
	 		
	return eq, large
	

def quick_sort(list_):
    if list_:
        pivot = list_[randint(0, len(list_) - 1)]
        i, j = partition(list_, pivot)
        return quick_sort(list_[:i]) + list_[i:j] + quick_sort(list_[j:])
    return []

print(*quick_sort(list_number))