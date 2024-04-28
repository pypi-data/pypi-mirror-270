from bashinpy import system

def draft(x, y):
    system.call(f"tput cup {x} {y}")

def draftprint(x, y, text):
    draft(x, y)
    print(text)

def draftinput(x, y, text):
    draft(x, y)
    input(text)

def clear():
    system.call("clear")

def reset():
    system.call("tput reset")
