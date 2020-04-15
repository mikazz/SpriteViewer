# SpriteViewer
 Sprite Viewer made with Python [Pygame]

![mark](examples/example_1.png)

# Requirements
Installed Python 3.x
Pygame Library


# What is this?
Basic Sprite viewer that animates images, allows to fastly check sprites 


# What it can do?
* [Q/W] - Change Speed of animation (Frames Per Second)
* [SPACE] - Pause
* [V/H] - Mirror sprite Vertically and Horizontally
* [R] - Rewind Animation To Begin [first frame] (better hold the key...)
* [A/S] - Go to Prev/Next Frame of animation
* [L/R ARROWS] - Next Anim Dir 
* [F] - Enter FullScreen Mode
* [ESC] - Exits


# Usage
Put your sprites inside DATA directory
Then run the Script sprite_viewer.py

```bash
>DATA
    >run
        >1.png
        >2.png
        >3.png
    >idle
        >1.png
    >jump
        >1.png
```

# TODO
* Centerize sprites (and adjust resolution automatically to screen size)
* Add sprites scaling at runtime
* Add better directory management, instead of specifying directory with animations inside code
* Add directory manager (view more directories)
* Fix color picker (its broken now)


# Releases
v1.0 - 17.03.2020
