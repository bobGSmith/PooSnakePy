# PooSnakePy
This is the classic snake game except the snake does dumps, which you have to avoid. It runs in the terminal.

## Install
From this project folder:

```bash
pip install .
```

Then launch the game from any terminal:

```bash
poosnake
```

For editable development installs, use:

```bash
pip install -e .
```

## Install From GitHub
Run this command:

```bash
python3 -m pip install --upgrade --force-reinstall git+https://github.com/ovrhuman/PooSnakePy.git
```

Then start the game with:

```bash
poosnake
```

If your terminal says `poosnake: command not found`, run it this way instead:

```bash
python3 -m poosnake
```

On macOS, `pip` sometimes installs commands into a folder that is not on your terminal `PATH`, but `python3 -m poosnake` should still work.

## Dependencies
You need Python 3.8 or newer. On Windows, the `windows-curses` package is installed automatically.

## Gameplay
The snake speeds up every time you go up a level. The poos you do are cleared every level, but each level requires you to do a greater number of poos than the one before.

The game uses little terminal animations for digesting (`oooOooo0`) and eating (`oooooooC`) by changing the character used for the body part where the food is.

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

`o` is a body segment, `0` is the head, `*` is food, and `~` is a poo. If you go through a wall, you come out the opposite side. If you hit a poo or body segment, it is game over.
