import math
import random

# obj: get to this pattern
# [[1, 2, 3],
#  [1, 2, 3],
#  [1, 2, 3]]

desired_list = [[1, 2, 3],
                [1, 2, 3],
                [1, 2, 3]]


# region functions
def top_left():
    num_list[0] = num_list[0][1:] + num_list[0][:1]


def top_right():
    num_list[0] = num_list[0][2:] + num_list[0][:2]


def middle_left():
    num_list[1] = num_list[1][1:] + num_list[1][:1]


def middle_right():
    num_list[1] = num_list[1][2:] + num_list[1][:2]


def bottom_left():
    num_list[2] = num_list[2][1:] + num_list[2][:1]


def bottom_right():
    num_list[2] = num_list[2][2:] + num_list[2][:2]


def left_up():
    temp = [num_list[i][0] for i in range(3)]
    temp = temp[1:] + temp[:1]

    for i in range(3):
        num_list[i][0] = temp[i]


def left_down():
    temp = [num_list[i][0] for i in range(3)]
    temp = temp[2:] + temp[:2]

    for i in range(3):
        num_list[i][0] = temp[i]


def middle_up():
    temp = [num_list[i][1] for i in range(3)]
    temp = temp[1:] + temp[:1]

    for i in range(3):
        num_list[i][1] = temp[i]


def middle_down():
    temp = [num_list[i][1] for i in range(3)]
    temp = temp[2:] + temp[:2]

    for i in range(3):
        num_list[i][1] = temp[i]


def right_up():
    temp = [num_list[i][2] for i in range(3)]
    temp = temp[1:] + temp[:1]

    for i in range(3):
        num_list[i][2] = temp[i]


def right_down():
    temp = [num_list[i][2] for i in range(3)]
    temp = temp[2:] + temp[:2]

    for i in range(3):
        num_list[i][2] = temp[i]
# endregion


f_in = open("colour_puzzle_output.txt", "w")

lowest = math.inf

for x in range(100000):
    sequence = ""
    moves = 0

    num_list = [[3, 2, 2],
                [3, 1, 1],
                [3, 2, 1]]

    while num_list != desired_list:
        num = random.randrange(0, 11)

        moves += 1

        # region cases
        match num:
            case 0:
                top_left()
                sequence += "TL "
            case 1:
                top_right()
                sequence += "TR "
            case 2:
                middle_left()
                sequence += "ML "
            case 3:
                middle_right()
                sequence += "MR "
            case 4:
                bottom_left()
                sequence += "BL "
            case 5:
                bottom_right()
                sequence += "BR "
            case 6:
                left_up()
                sequence += "LU "
            case 7:
                left_down()
                sequence += "LD "
            case 8:
                middle_up()
                sequence += "MU "
            case 9:
                middle_down()
                sequence += "MD "
            case 10:
                right_up()
                sequence += "RU "
            case 11:
                right_down()
                sequence += "RD "
        # endregion

    if moves < lowest:
        lowest = moves

    if moves < 8:
        f_in.write(sequence + "\n")
        f_in.write(str(moves) + "\n")

f_in.write(str(lowest) + "\n")
f_in.close()
