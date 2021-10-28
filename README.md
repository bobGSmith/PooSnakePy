# PooSnakePy
This is the classic snake game except the snake does dumps, which you have to avoid. It runs in the terminal.

## Dependencies 
You need python and the windows curses package for python. 
```shell
pip install windows-curses
```

## Gameplay 
The snake speeds up everytime you go up a level. The poos you do are cleared every level, but each level requires you do a greater nubmber of poos than the one before. I have implemented some animations for digesting ( `oooOooo0` ) and eating ( `oooooooC` ) by changing the letter used for the body part where the food is.
