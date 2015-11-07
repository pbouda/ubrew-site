Title: DIY Gamepad... and ZEOMA!
Date: 2015-11-07 13:48
Image: /images/blog/diy_gamepad_main.jpg

First of all I want to introduce you to new project that is now featured on this
site and that we will be working on in the future. The working title is ZEOMA,
and it is a modular game console based on the
[EOMA-68 concept](http://elinux.org/Embedded_Open_Modular_Architecture/EOMA-68).
We will publish more information about the project in the coming weeks, and how
you might join in to build the first open and modular game console!

As one of the steps to create prototypes of the
[different PCBs](http://rhombus-tech.net/community_ideas/games_console/news/pcb_block_diagram_updated2_23sep2015/)
I am currently working on the gamepad boards (2nd and 3rd PCBs in the
schematics). I use a Nucleo STM32F072 development board und recently got the
USB HID examples of the [libopencm3 project](http://libopencm3.org/wiki/Main_Page)
working. My idea now is to write a little firmware that takes the input from the
analog sticks and the buttons and transforms it into USB HID data that I can
send to the main computer board (currently my PC). A DIY gamepad, so to speak.
To make things a little easier I bought a gamepad shield for the Arduino, as the
Nucleo board provides a compatible header. Here are some photos of the result:

![DIY Gamepad for ZEOMA progress](/images/blog/diy_gamepad.gif)

Already looks awesome! The next step is now the firmware... Stay tuned for
updates!
