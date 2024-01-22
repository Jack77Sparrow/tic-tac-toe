import random
import os
import time
import datetime
pol = [' ',' ',' ',
       ' ',' ',' ',
       ' ',' ',' ', " "]
Game = 0

startgame = time.time()

win = 1
lose = -1
Draw = 2
rungame = 0
list_of_numbers = [1,2,3,4,5,6,7,8,9]
#quadr = int(input("input from 1-9: "))
def DrawBoard():
    print(" %c | %c | %c " % (pol[1], pol[2], pol[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (pol[4], pol[5], pol[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (pol[7], pol[8], pol[9]))
    print("   |   | ")
def check_position(x):
    if pol[x] == ' ':
        return True
    else:
        return False

def check_win():
    global Game
    if pol[1] == pol[2] and pol[2] == pol[3] and pol[1] !=' ':
        Game = win  
        
    elif pol[4] == pol[5] and pol[5] == pol[6] and pol[4] !=' ':
        Game = win   
    elif pol[7] == pol[8] and pol[8] == pol[9] and pol[7] !=' ':
        Game = win   
    elif pol[1] == pol[4] and pol[4] == pol[7] and pol[1] !=' ':
        Game = win   
    elif pol[2] == pol[5] and pol[5] == pol[8] and pol[2] !=' ':
        Game = win  
    elif pol[3] == pol[6] and pol[6] == pol[9] and pol[3] !=' ':
        Game = win  
    elif pol[1] == pol[5] and pol[5] == pol[9] and pol[5] !=' ':
        Game = win 
    elif pol[3] == pol[5] and pol[5] == pol[7] and pol[5] !=' ':
        Game = win   
    elif pol[1] != ' ' and pol[2] != ' ' and pol[3] != ' ' and \
            pol[4] != ' ' and pol[5] != ' ' and pol[6] != ' ' and \
            pol[7] != ' ' and pol[8] != ' ' and pol[9] != ' ':
        Game = Draw
    else:
        Game = rungame
        


def run_game():       
    while Game == rungame:
        quadr = int(input("input from 1-9: "))
        pchod = random.choice(list_of_numbers)
        if check_position(quadr):

            #pol[quadr] = 'x'
            list_of_numbers.remove(quadr)
            #pchod = random.choice(list_of_numbers)
            # if quadr == pchod:
            #     time.sleep(1)
            #     pol[pchod] = 'o'
            
            time.sleep(1)
            pol[quadr] = 'x'    
            #pol[pchod] = 'o'
            check_win()
        if check_position(pchod):
            list_of_numbers.remove(pchod)
            time.sleep(1)
            pol[pchod] = 'o'
                
            check_win()
        DrawBoard()
        
def start_game():
    print("if you wana start game write [start]")
    start = input()
    
    if start == "start":
        
        print("game is running: good luck)😃🤞")
        run_game()
    else:
        print("please write [start] if you wana start game: ")
        
start_game()


#run_game()
#check_win()
endgame= time.time()

print(f"game is over on time {endgame-startgame:.2f}")