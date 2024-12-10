n = int(input())
past_f = float(input())
sequenc = []

minimum = 30.0
maximum = 4000.0

for _ in range(n - 1):
    f, w = input().split()
    sequenc.append((float(f), w))


def get_new_max_or_min(a, b, now_max_or_min, r=None):
    new_max_or_min = (a - b) / 2 + b
    if r == "maximum":
        return new_max_or_min if new_max_or_min < now_max_or_min else now_max_or_min
    elif r == "minimum":
        return new_max_or_min if new_max_or_min > now_max_or_min else now_max_or_min



for i in range(len(sequenc)):
    f, position  = sequenc[i]
    if f == past_f:
        continue
    if f < past_f:
        if position == "closer":
            maximum = get_new_max_or_min(past_f, f, maximum, "maximum")
        
        if position == "further":
            minimum = get_new_max_or_min(past_f, f, minimum, "minimum")
    else:
        if position == "closer":
            minimum = get_new_max_or_min(f, past_f, minimum, "minimum")
        
        if position == "further":
            maximum = get_new_max_or_min(f, past_f, maximum, "maximum")

    past_f = f

print(round(minimum, 6), round(maximum, 6))


