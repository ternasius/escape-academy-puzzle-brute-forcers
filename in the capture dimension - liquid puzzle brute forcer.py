import math
import random
# obj: get [3, 3, 3, 3, 3] in rightmost column

desired_right_list = [3, 3, 3, 3, 3]


def M_to_L():
    zero_count = 0
    for i in liquid_list[0]:
        if i == 0:
            zero_count += 1

    move_list = liquid_list[1][:zero_count]

    for _ in range(zero_count):
        liquid_list[0].pop()
        liquid_list[1].pop(0)
        liquid_list[1].append(0)

    for i in range(zero_count):
        liquid_list[0].append(move_list[i])

    liquid_list[0].sort(reverse=True)


def L_to_M():
    max_zeroes = 7
    zero_count = 0
    for i in liquid_list[1]:
        if i == 0:
            zero_count += 1

    if zero_count > max_zeroes:
        zero_count = 7

    move_list = liquid_list[0][:zero_count]

    for _ in range(zero_count):
        liquid_list[1].pop()
        liquid_list[0].pop(0)
        liquid_list[0].append(0)

    for i in range(zero_count):
        liquid_list[1].append(move_list[i])

    liquid_list[1].sort(reverse=True)


def M_to_R():
    zero_count = 0
    for i in liquid_list[2]:
        if i == 0:
            zero_count += 1

    move_list = liquid_list[1][:zero_count]

    for _ in range(zero_count):
        liquid_list[2].pop()
        liquid_list[1].pop(0)
        liquid_list[1].append(0)

    for i in range(zero_count):
        liquid_list[2].append(move_list[i])

    liquid_list[2].sort(reverse=True)


def R_to_M():
    max_zeroes = 5
    zero_count = 0
    for i in liquid_list[1]:
        if i == 0:
            zero_count += 1

    if zero_count > max_zeroes:
        zero_count = 5

    move_list = liquid_list[2][:zero_count]

    for _ in range(zero_count):
        liquid_list[1].pop()
        liquid_list[2].pop(0)
        liquid_list[2].append(0)

    for i in range(zero_count):
        liquid_list[1].append(move_list[i])

    liquid_list[1].sort(reverse=True)


def R_to_L():
    max_zeroes = 5
    zero_count = 0
    for i in liquid_list[0]:
        if i == 0:
            zero_count += 1

    if zero_count > max_zeroes:
        zero_count = 5

    move_list = liquid_list[2][:zero_count]

    for _ in range(zero_count):
        liquid_list[0].pop()
        liquid_list[2].pop(0)
        liquid_list[2].append(0)

    for i in range(zero_count):
        liquid_list[0].append(move_list[i])

    liquid_list[0].sort(reverse=True)


def L_to_R():
    max_zeroes = 5
    zero_count = 0
    for i in liquid_list[2]:
        if i == 0:
            zero_count += 1

    if zero_count > max_zeroes:
        zero_count = 5

    move_list = liquid_list[0][:zero_count]

    for _ in range(zero_count):
        liquid_list[2].pop()
        liquid_list[0].pop(0)
        liquid_list[0].append(0)

    for i in range(zero_count):
        liquid_list[2].append(move_list[i])

    liquid_list[2].sort(reverse=True)


f_in = open("liquid puzzle_output.txt", "w")

lowest = math.inf

for x in range(1000000):
    sequence = ""
    moves = 0

    liquid_list = [[3, 2, 2, 1, 0, 0, 0],
                   [3, 3, 3, 2, 2, 1, 1, 0, 0],
                   [3, 2, 1, 1, 0]]

    while liquid_list[2] != desired_right_list:
        num = random.randint(0, 5)

        moves += 1

        # region cases
        match num:
            case 0:
                L_to_M()
                sequence += "LM "
            case 1:
                M_to_L()
                sequence += "ML "
            case 2:
                R_to_M()
                sequence += "RM "
            case 3:
                M_to_R()
                sequence += "MR "
            case 4:
                L_to_R()
                sequence += "LR "
            case 5:
                R_to_L()
                sequence += "RL "
        # endregion

    if moves < lowest:
        lowest = moves

    if moves < 11:
        f_in.write(sequence + "\n")
        f_in.write(str(moves) + "\n")

f_in.write(str(lowest) + "\n")
f_in.close()
