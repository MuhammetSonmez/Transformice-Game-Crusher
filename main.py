import time
import pyautogui as pg
import userlist
import pyperclip


def log():
    while True:
        time.sleep(1)
        print(pg.position())

def goto_tribe_room():
    pg.moveTo(1075,820, 1)
    pg.click()
    pg.moveTo(1680, 600, 1)
    pg.click()
    time.sleep(3)


def execute_lua(luadata):
    pg.press("Enter")
    pg.write("/lua")
    pyperclip.copy(luadata)
    pg.press("Enter")
    pg.moveTo(1425,430)
    pg.click()
    time.sleep(0.2)
    pg.hotkey("ctrl", "a")
    pg.press("backspace")
    pg.hotkey("ctrl", "v")
    pg.moveTo(1440, 580)
    pg.click()
    pg.moveTo(1290,820)
    pg.click()
    pg.write("/room 1")
    pg.press("Enter")
    


def inviter(luadata):
    goto_tribe_room()
    with open('userlist.txt', 'r') as f:
        arr = [line.strip() for line in f]
    
    for i in arr:
        pyperclip.copy(i)
        pg.press('enter')
        pg.write("/inv ")
        pg.hotkey("ctrl", "v")
        time.sleep(1)
        pg.press("Enter")

    execute_lua(luadata)
    
def change_room(room_list):
    arr = []
    for i in room_list:
        pg.press("Enter")
        pg.write("/room " + i)
        time.sleep(1)
        pg.press("Enter")
        time.sleep(3)
        arr = arr + ulist()
        pg.press("Enter")
    print(set(arr), len(arr))
    return set(arr)


def silence():
    pg.press("Enter")
    pg.write("/silence Incorrect version, try to reload the game.")
    pg.press("Enter")
    time.sleep(2)


def ulist():
    arr = userlist.getUserlist()
    #print(arr, len(arr))
    return arr


def get_data():
    room_list = ["vanilla2", "vanilla1", "1", "5", "survivor787", "survivor esek", "survivor", "racing1", "racing96846468"]
    arr = change_room(room_list)
    with open('userlist.txt', 'w') as f:
        for i in arr:
            f.write(f"{i}\n")


def clear_userlist():
    with open("userlist.txt", "w") as f:
        f.write("")
        f.close()




def main(luadata):
    
    #log()
    silence()
    get_data()
    inviter(luadata=luadata)
    #clear_userlist()

if __name__ == '__main__':
    luadata = """data = 3
function eventLoop (datA)
    if data == 0 then 
        for i = 0, 9999
        do
            tfm.exec.addShamanObject(4,-100,-200,0,0,0,false)
        end
    else
        print(data) 
        data = data - 1
    end 
end
--Incorrect version, try to reload the game."""
    main(luadata=luadata)
