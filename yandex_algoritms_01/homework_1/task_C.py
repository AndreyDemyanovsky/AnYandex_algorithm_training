def get_clear_number(number):
    if number.startswith("8"):
        number = number[1:]
    if number[0] == "+":
        number = number[2:]
    if "-" in number:
        number = number.replace("-", "")
    if "(" in number:
        number = number.replace("(", "")
    if ")" in number:
        number = number.replace(")", "")
    if len(number) < 10:
        number = "495" + number

    return int(number)


new_number = get_clear_number(input())
list_saved_numbers = [get_clear_number(input()) for _ in range(3)]

for i in list_saved_numbers:
    if i == new_number:
        print("YES")
    else:
        print("NO")