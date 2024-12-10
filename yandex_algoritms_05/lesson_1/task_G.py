my_units = int(input())  # кол наших саолдат 
hp = int(input())  # здоровье казармы 
enemy_units = int(input())  # кол солдат врага за раунд
min_number_rounds = 10 ** 9 + 7


def battle_simulation(t, my_units, enemy_units):
    hp_barracks = hp
    cou_r = 0
    enemy_warriors = 0

    while hp_barracks > t:
        if enemy_warriors >= my_units:
            return 10 ** 9 + 7
        hp_barracks -= (my_units - enemy_warriors)  # убиваем всех солдат и атакуем остатком казарму
        enemy_warriors = 0

        if hp_barracks > 0:  # если казарма жива создаем солдат противника
            enemy_warriors += enemy_units
        cou_r += 1  # прибавляем количество раундов

    while hp_barracks > 0:
        if my_units <= 0:
            return 10 ** 9 + 7
        if hp_barracks >= my_units:  # если у нас солдат больше или равно здоровью казармы то бьем всеми силами по казарме
            hp_barracks -= my_units
        else:  # иначе, убиваем казарму и оставшимися войнами бьем по вражеским
            enemy_warriors -= my_units - hp_barracks
            hp_barracks = 0
        my_units -= enemy_warriors

        if hp_barracks > 0:  # если казарма жива создаем солдат противника
            enemy_warriors += enemy_units
        cou_r += 1

    while enemy_warriors > 0:
        if my_units <= 0:
            return 10 ** 9 + 7
        enemy_warriors -= my_units
        if enemy_warriors > 0:
            my_units -= enemy_warriors
        cou_r += 1

    return cou_r


for i in range(hp + 1):
    ans_for_i = battle_simulation(i, my_units, enemy_units)
    if ans_for_i < min_number_rounds:
        min_number_rounds = ans_for_i

print(min_number_rounds if min_number_rounds != 10 ** 9 + 7 else -1)
