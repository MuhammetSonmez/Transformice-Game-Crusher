import pyautogui as pg
import clipboard

def generate_combinations_3():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    combinations = []

    for first_char in alphabet:
        for second_char in alphabet:
            for third_char in alphabet:
                combination = first_char + second_char + third_char
                combinations.append(combination)
                if combination == 'zzz':
                    return combinations

    return combinations

def generate_combinations():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    combinations = []

    for first_char in alphabet:
        for second_char in alphabet:
            combination = first_char + second_char
            combinations.append(combination)
            if combination == 'zz':
                return combinations

    return combinations


def write_to_file(data):
    with open("check.txt", "+a", encoding= "utf-8") as f:
        f.write(data)
        f.close()

def read_to_file():
    userlist = []
    with open("check.txt", "r", encoding="utf-8") as f:
        for line in f:
            if "#" in line:
                userlist.append(line)
        f.close()
    return userlist

def clear_file():
    with open("check.txt", "w", encoding="utf-8") as f:
        f.write("")
        f.close()


def getUserlist():
    pg.PAUSE = 0.001
    charlist = generate_combinations()
    userlist = []
    pg.press("Enter")
    clear_file()
    for char in charlist:
        pg.write(char)
        pg.press('tab')
        pg.hotkey("ctrl", "a")
        pg.hotkey("ctrl", "x")
        pg.keyUp("ctrl")
        copied_text = clipboard.paste()
        write_to_file(copied_text + "\n")
    
    for i in read_to_file():
        if i not in userlist or i + "\n" not in userlist:
            userlist.append(i.replace("\n", ""))
        else:
            print(i)

    return userlist

"""
u = getUserlist()
print(u, len(u))

"""