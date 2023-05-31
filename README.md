# PooSnakePy
This is the classic snake game except the snake does dumps, which you have to avoid. It runs in the terminal.

## Install 

```
pip install git+https://github.com/bobGSmith/PooSnakePy@master
```

## Play 

resize your terminal so its big enough to play (should happen automatically but doesnt seem to work on some), then run:

```
python3 -m PooSnake 
```

## Gameplay 
The snake speeds up everytime you go up a level. The poos you do are cleared every level, but each level requires you do a greater nubmber of poos than the one before. I have implemented some animations for digesting ( `oooOooo0` ) and eating ( `oooooooC` ) by changing the letter used for the body part where the food is.

## Screenshot 
```shell
 ]_______________________________________________[  
 ]       [POO-SNAKE] [poos 1] [level 1]          [  
 ]===============================================[  
 ]                                               [  
 ]                                               [  
 ]                                               [  
 ]                  *                            [  
 ]                                               [  
 ]                                               [  
 ]                                               [
 ]                                  o o 0        [  
 ]                                               [  
 ]                                               [  
 ]                                               [  
 ]                                               [  
 ]                        ~                      [  
 ]                                               [  
 ]                                               [  
 ]                                               [  
 ]                                               [  
 ]                                               [  
 ]                                               [  
 ]                                               [  
 ]                                               [  
 ]                                               [  
 ]                                               [  
 ]                                               [  
 ]                                               [  
 ]                                               [  
 ]===================================BOBGAME=====[ 
```

where `o` is a body segment, `0` is the head, `*` is food, and `~` is a poo. If you go through a wall you come out the opposite side. If you hit a poo or body segment its game over. 
