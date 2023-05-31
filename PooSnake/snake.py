                        #############
                        # POO-SNAKE #
                        #############


import curses
import time 
import random

#=================# GAME FUNCTIONS #=================#

def mv_hed(head, direction, rows, cols, top_boarder):
    if direction =='e':
        head[1] += 2 
    if direction == 'w':
        head[1] -= 2
    if direction == 's':
        head[0] += 1
    if direction == 'n':
        head[0] -= 1
       
    if head [0] == rows-1:
        head[0] = top_boarder + 1
    elif head[1] >= cols-2:
        head[1] = 2
    elif head[0] == top_boarder:
        head[0] = rows - 2
    elif head[1] <= 1:
        head[1] = cols - 3
    return head
  
def eat(food, head, body, food_state, poos, h ,w, top_boarder, direction):
    score_add = False; dead = 'not'
    if food == head and food_state == 'uneaten':
        food_state = 'digesting'
        score_add = True 
        if direction == 'n': prey = 'U'; 
        elif direction == 's': prey = 'n';
        elif direction == 'e': prey = 'C'; 
        elif direction == 'w': prey = '3'
        
    elif food_state == 'digesting' and food in body:
        prey = 'O'
    elif food_state == 'digesting' and food not in body:
        poos.append(food)
        body.insert(0,food)
        prey = '*'
        food = [random.randint(top_boarder+1,h-2), random.choice([x for x in range(2,47,2)])]
        food_state = 'uneaten'
    elif head in body:
        dead = 'body'; prey = '*'
    elif head in poos:
        dead = 'poo'; prey = '*'
    else:
        prey = '*'
    return food, food_state, poos, prey, score_add, dead, body
    
def set_up(h,w, key_pad = True, no_delay = True, cursor = False):    
    curses.resize_term(h,w)
    scr = curses.newwin(h,w,0,0)
    scr.keypad(key_pad)
    curses.noecho()
    scr.nodelay(no_delay)
    curses.cbreak()
    curses.curs_set(cursor)
    return scr

def get_direction(key, direction,u = curses.KEY_UP, d = curses.KEY_DOWN, l = curses.KEY_LEFT,  r = curses.KEY_RIGHT):
    if key == l and direction != 'e':
        direction = 'w'
    elif key == r and direction != 'w':
        direction = 'e'
    elif key == u and direction != 's':
        direction = 'n'
    elif key == d and direction != 'n':
        direction = 's'
    else: 
        pass 
    return direction

def boarder_setup(scr,h ,w, bottom_boarder, top_boarder, l_boarder, r_boarder, score,level,logo = 'BOBGAME', left = ']', right = '['):
    scr.clear()
    scr.addstr(1, (w//2)-16, '[POO-SNAKE] [poos {}] [level {}]'.format(score,level))
    scr.addstr(top_boarder,1,'='*(w-2))
    scr.addstr(0,1,'_'*(w-2))
    scr.addstr(bottom_boarder,1,'='*(w-2))
    scr.addstr(bottom_boarder, w//2 + w//4, logo)
    for i in range(h):
        scr.addstr(i,r_boarder,'[')
        scr.addstr(i,l_boarder,']') 

def levelup_screen(scr, top_boarder, h, level):
    for i in range(top_boarder+1, h -2):
        scr.addstr(i,6,'NXT LVL ! ' * 4)
        scr.refresh()
        time.sleep(0.05)
    scr.clear()
    scr.addstr((h//2)-5,19,'[=========]')
    scr.addstr((h//2)-3, 19,'[=========]')
    scr.addstr((h//2) -4,19, '[ LEVEL {:6<} ]'.format(level))
    scr.refresh()
    time.sleep(1.5)

def display_snake(scr, head, body, head_symbol = '0', body_symbol = 'o'):
    scr.addstr(head[0],head[1], head_symbol)
    for b in body:
        scr.addstr(b[0],b[1],body_symbol)

def display_food(scr,food,prey):
    scr.addstr(food[0],food[1],prey)
    
def display_poos(scr, poos, poo_symbol = '~'):
    for p in poos:
        scr.addstr(p[0],p[1], '~')
        
def mv_body(body, head):
    body.append(head.copy())
    body.pop(0)
    return body     
    
#=================# GAME SETUP #=================#

if __name__ == '__main__': 
        
    again = ord('y')
    h,w =  30,51 
    top_boarder = 2
    bottom_boarder = 29
    l_boarder = 1
    r_boarder = 49


    while again == ord('y'):  
        
        stdscr = curses.initscr()
        scr = set_up(h,w)
        u = curses.KEY_UP; d = curses.KEY_DOWN; l = curses.KEY_LEFT;  r = curses.KEY_RIGHT
        
        
        head = [10,12]
        body = [[10,11]]
        food = [h//2, (w//2) + 1]
        direction = 'e'
        prey = '*' 
        food_state = 'uneaten' 
        poos = []
        score = 0
        speed = 0.22
        level = 1
        
        #=================# GAME LOGIC #=================#
        
        while True:
            scr.refresh()
            time.sleep(speed)
            
            # user input
            key = scr.getch()
            direction = get_direction(key, direction)
            
            # eating
            food, food_state, poos, prey, score_add, dead, body = eat(food, head, body,
                                                                food_state, poos, 
                                                                h, w, top_boarder, direction)
            
            # update score, check if dead
            if score_add:
                score += 1 
            if dead != 'not':
                break
            
            # display snake, food, boarder etc.. 
            boarder_setup(scr, h ,w, bottom_boarder, top_boarder, l_boarder, r_boarder,score, level)
            display_snake(scr,head,body)
            display_food(scr,food,prey)
            display_poos(scr,poos)

            # move the snake    
            body = mv_body(body,head)
            head = mv_hed(head, direction, h, w, top_boarder)
            
            if len(poos) == 2 * (level + 1):
                poos = []
                level += 1
                speed *= 0.75
                levelup_screen(scr, top_boarder, h, level)
                
            
            if key == ord('q'):
                break
        
        scr.refresh()
        scr.clear()
        scr.addstr(1, (w//2)-17, '[POO-SNAKE] [poos {}] [level {}]'.format(score,level))
        scr.addstr(top_boarder,1,'='*(w-2))
        scr.addstr(0,1,'='*(w-2))
        scr.addstr(bottom_boarder,1,'='*(w-2))
        for i in range(h):
            scr.addstr(i,r_boarder,'[')
            scr.addstr(i,l_boarder,']')
        scr.addstr(head[0], head[1], 'X')
        for b in body:
            scr.addstr(b[0],b[1], 'x' )
            
        scr.refresh()
        time.sleep(2)
        scr.clear()
        
        scr.nodelay(False)
        scr.addstr((h//2)-5,18,'[============]')
        scr.addstr((h//2)-3, 18,'[============]')
        scr.addstr((h//2) -4,18, '[ GAME OVER! ]')
        
        if dead == 'poo':
            scr.addstr((h//2)-1,7,'Snake died frome eating his own dump')

        elif dead == 'body':
            scr.addstr((h//2)-1,16,'Snake ate himself...')
        else:
            scr.addstr((h//2)-1,12,'Snake lost the will to live')
            
        scr.addstr((h//2)+1, 14, 'Poos done: {}, level: {}'.format(score,level))
        scr.addstr((h//2)+3,16,'Play again?  (y/n)')
        scr.refresh()
        again = scr.getch()
        if again != ord('y') and again != ord('n'):
            scr.addstr((h//2)+3,12,'invalid input, enter y or n')
            scr.addstr((h//2)+4,16,'Play again?  (y/n)')
            again = scr.getch()
            scr.refresh()
            if again != ord('y') and again != ord('n'):
                scr.clear()
                scr.addstr((h//2),16,'OH FORGET IT !!')
                scr.refresh()
                time.sleep(2)
                curses.endwin()
            
    curses.endwin()

        

