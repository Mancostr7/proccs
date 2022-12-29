import random

def proccs():
    BLACK   = '\033[30m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE    = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'
    WHITE   = '\033[37m'
    list = [BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE]
    color = random.choice(list)
    for i in range(100):
        if(i % 2 == 0):
            print(color + f"--> {i + 1}%", end="\r")
        time.sleep(0.01)
