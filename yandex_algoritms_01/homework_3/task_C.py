count_kubs_Any, count_kubs_Bory = map(int, input().split())
set_kubs_Any = set(int(input()) for _ in range(count_kubs_Any)) 
set_kubs_Bory = set(int(input()) for _ in range(count_kubs_Bory)) 

interesec = set_kubs_Any.intersection(set_kubs_Bory)
remainder_Any = set_kubs_Any.difference(set_kubs_Bory)
remainder_Bory = set_kubs_Bory.difference(set_kubs_Any)

print(len(interesec))
print(*sorted(interesec))

print(len(remainder_Any))
print(*sorted(remainder_Any))

print(len(remainder_Bory))
print(*sorted(remainder_Bory))