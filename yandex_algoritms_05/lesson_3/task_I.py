import sys
import re


class Player:
    def __init__(self, name, command):
        self.name = name
        self.count_goals = 0
        self.he_command = command
        self.goals_on_minutes = {i: 0 for i in range(1, 91)}
        self.opened_scoring = 0

    def goal(self, minute):
        self.count_goals += 1
        self.goals_on_minutes[minute] += 1

    def get_count_goal_on_minute(self, minute, start=1):
        summa = 0
        for i in range(start, minute + 1):
            summa += self.goals_on_minutes[i]
        return summa


players = {}
commands = {}

score_com1 = 0
com1 = None

score_com2 = 0
com2 = None

first_goal = None


def create_command(com, scores, dct):
    if com not in dct:
        dct[com] = [0, 0, 0]  # количество голов, количество матчей, открывала счет первой
    dct[com][0] += scores
    dct[com][1] += 1


def get_string(lst):
    return " ".join(lst)


for line in sys.stdin:

    if "-" in line:
        pattern_team = r"\".+\""
        pattern_score = r"\d+:\d+"
        teams = re.findall(pattern_team, line)
        com1, com2 = map(str.strip, teams[0].split("-"))
        score_com1, score_com2 = map(int, re.findall(pattern_score, line)[0].split(":"))

        create_command(com1, score_com1, commands)
        create_command(com2, score_com2, commands)

    elif score_com1 or score_com2:
        player = line.split()
        player[-1] = player[-1].replace("'", "")
        minutes = int(player.pop(-1))
        name = " ".join(player)

        if not first_goal:
            first_goal = [minutes, name]
        elif first_goal[0] > minutes:
            first_goal = [minutes, name]

        if score_com1:
            command = com1
            score_com1 -= 1
        elif score_com2:
            command = com2
            score_com2 -= 1

        if name not in players:
            players[name] = Player(name, command)

        players[name].goal(minutes)
        if not score_com1 and not score_com2:
            players[first_goal[1]].opened_scoring += 1
            command_player = players[first_goal[1]].he_command
            commands[command_player][2] = commands[command_player][2] + 1
            first_goal = None
    else:
        res = 0
        line = line.split()
        match line:
            case "Total", "goals", "for", *command:
                command = get_string(command)
                if command in commands:
                    res = commands[command][0]

            case "Total", "goals", "by", *name:
                name = get_string(name)
                if name in players:
                    res = players[name].count_goals

            case "Mean", "goals", "per", "game", "for", *command:
                command = get_string(command)
                if command in commands:
                    res = commands[command][0] / commands[command][1]

            case "Mean", "goals", "per", "game", "by", *name:
                name = get_string(name)
                if name in players:
                    p = players[name]
                    res = p.count_goals / commands[p.he_command][1]

            case "Score", "opens", "by", *name_or_command:
                name_or_command = get_string(name_or_command)
                if name_or_command in commands:
                    res = commands[name_or_command][2]
                elif name_or_command in players:
                    res = players[name_or_command].opened_scoring

            case "Goals", "on", "minute", m, "by", *name:
                name = get_string(name)
                if name in players:
                    res = players[name].goals_on_minutes[int(m)]

            case "Goals", "on", "first", t, "minutes", "by", *name:
                name = get_string(name)
                if name in players:
                    res = players[name].get_count_goal_on_minute(int(t))

            case "Goals", "on", "last", t, "minutes", "by", *name:
                name = get_string(name)
                if name in players:
                    res = players[name].get_count_goal_on_minute(90, start=91 - int(t))

        print(res)

