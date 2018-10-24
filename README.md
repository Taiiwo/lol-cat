## lol-cat
This is a fork of [osu!cat](https://github.com/ZeCryptic/osu-cat/releases/tag/v1.2.0) for use with League of Legends. Keys pressed with the middle and ring finger of the left hand trigger a left press, and every other key triggers a right press. Mouse is tracked as normal. Command line options are removed for convenience. Green screen mode is used by default. To turn it off, make a file called "nogreenscreen.txt" with the contents "1" for a white background. I had to change the way the original detected keys to allow detection inside of the game window, so it detects keys a little bit differently, but I think its more efficient overall. Feel free to use it on your stream. You can put a link to this repo in your stream description if you want.

Random video of it in action:
![gif of it in action](https://sr.ht/-coq.gif)
Better video examples welcome

## Download
I've compiled my version into a windows binary so you don't have to compile it yourself:
### [Download Windows Binaries here](https://github.com/Taiiwo/lol-cat/releases)

Here's the rest of the original readme:

This is a python application that tracks the cursor position and key inputs to create a Bongo Cat window which can be used as an overlay for streaming/recording applications.

## [Latest version](https://github.com/Taiiwo/lol-cat/releases)
* Window is now resizable (thanks JapanPanda)
* Dragging the window should no longer be buggy
* Added an option for chroma key green background
* More performance fixes (thanks JapanPanda)
## Changing the cat images
It is entirely possible to edit the png files to make the cat look different (totally understandable, they look bad). However, when doing so you need to make sure that the new picture files have a color depth of 32 bits. Otherwise the program will not work. One way of doing this is by just re-saving the images in a program like paint.net and select the [32-bit color depth option](http://puu.sh/ByjvT/8023ae8252.png). I plan on fixing this bug in the future

