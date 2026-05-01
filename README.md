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
Replace `YOUR_USERNAME` with the GitHub account that owns the repo:

```bash
python3 -m pip install --upgrade --force-reinstall git+https://github.com/YOUR_USERNAME/PooSnakePy.git
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
