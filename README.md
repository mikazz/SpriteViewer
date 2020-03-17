# SpriteViewer
 Sprite Viewer made with Python [Pygame]


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
Inside sprite_viewer (open with notepad or something) there is line
DIR_PATH = "player"
Change >player< according to your folder name
Then run the Script

Make sure that your main directory is organized in such way (name convention is not mandatory)

```bash
>main_directory_with_sprites
	>run
		>1.png
		>2.png
        >3.png
	>idle
        >1.png
	>jump
        >1.png
```

You can view only one main_directory_with_sprites at once


# TODO
* Centerize sprites (and adjust resolution automatically to screen size)
* Add sprites scaling at runtime
* Add better directory management, instead of specifying directory with animations inside code
* Add direcotry manager (view more directories)
* Fix color picker (its broken now)


# Releases
v1.0 - 17.03.2020
