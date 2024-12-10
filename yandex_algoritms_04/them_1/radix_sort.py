n = int(input())

list_sting = [str(input()) for i in range(n)]
def redix_sort(lst):
    lenght = len(lst[0])

    for i in range(lenght-1, -1, -1):
        bucket = [[] for i in range(10)]

        print(f"Phase {lenght - i}", sep="\n")
        for j in lst:
            bucket[int(j[i])].append(j)

        for i in range(10):
            print(f"Bucket {i}: {', '.join(bucket[i]) if bucket[i] else 'empty'}")    
        print("*" * 10)

        lst = [j for i in bucket for j in i]
    print(f"Sorted array:\n{', '.join(lst)}")
    

print(f"Initial array:\n{', '.join(list_sting)}\n{'*' * 10}")
redix_sort(list_sting)