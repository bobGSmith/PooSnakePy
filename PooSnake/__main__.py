from PooSnake import *


again = ord('y')
h,w =  30,51 
top_boarder = 2
bottom_boarder = 29
l_boarder = 1
r_boarder = 49


while again == ord('y'):  
    
    stdscr = curses.initscr()
    scr = set_up(h,w)
    u = curses.KEY_UP 
    d = curses.KEY_DOWN
    l = curses.KEY_LEFT
    r = curses.KEY_RIGHT
    
    
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
        direction = get_direction(key, direction,u,d,l,r)
        
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
        boarder_setup(scr, h ,w, bottom_boarder, top_boarder, l_boarder, r_boarder)
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

        


    

