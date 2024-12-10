STOP_INPUT = -2 * 10**9
data = None
tp = ""

while True:
    if data is None:
        data = int(input())
        if data == STOP_INPUT:
            break

    new_number = int(input())

    if new_number == STOP_INPUT:
        tp = "CONSTANT" if tp == "" else tp
        break

    if tp == "RANDOM":
        continue

    if new_number > data and tp not in ("WEAKLY DESCENDING", "DESCENDING") :
        if tp in ("ASCENDING", ""):
            tp =  "ASCENDING"
        else:
            tp = "WEAKLY ASCENDING"

    elif new_number < data and tp not in ("ASCENDING", "WEAKLY ASCENDING"):
        if tp in ("DESCENDING", ""):
            tp = "DESCENDING"
        else:
            tp = "WEAKLY DESCENDING"

    elif new_number == data:
        if tp =="ASCENDING":
            tp = "WEAKLY ASCENDING"
        elif tp =="DESCENDING":
            tp = "WEAKLY DESCENDING"
        elif tp == "":
            tp = "CONSTANT"
    else:
        tp = "RANDOM"

    data = new_number
        
print(tp)