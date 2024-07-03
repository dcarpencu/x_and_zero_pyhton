import numpy as np

arr = np.array(["-", "-", "-", "-", "-", "-", "-", "-", "-"])
new_arr = arr.reshape(3, 3)


def afisare_joc():
    print(arr[0], arr[1], arr[2], sep=" | ", flush=True, end="")
    print('\n=========')
    print(arr[3], arr[4], arr[5], sep=" | ", flush=True, end="")
    print('\n=========')
    print(arr[6], arr[7], arr[8], sep=" | ", flush=True, end="")


afisare_joc()

player = 'X'

isFinished = False


def check_game(index1, index2, index3):
    if arr[index1] == arr[index2] and arr[index2] == arr[index3] and arr[index1] != '-':
        return True
    else:
        return False


while (not isFinished):
    print()
    pozitia = int(input(f'E randul lui {player}, alege un numar intre 1-9:'))
    print()
    arr[pozitia - 1] = player;

    afisare_joc()
    print()

    if check_game(0, 1, 2) or check_game(3, 4, 5) or check_game(6, 7, 8) or check_game(0, 3, 6) or check_game(1, 4,
                                                                                                              7) or check_game(
            2, 5, 8) or check_game(0, 4, 8) or check_game(2, 4, 6):
        isFinished = True

    if (isFinished == True):
        print(f'{player} a castigat!')

    if (player == 'X'):
        player = '0'
    else:
        player = 'X'