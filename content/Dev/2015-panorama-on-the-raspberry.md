Title: Panorama on the Raspberry
Date: 2015-07-14 10:48
Image: /images/blog/panorama_raspberry_1.jpg

We have a first version of our Qt5 port of the [Panorama menu
system](https://github.com/bzar/panorama) running on the Raspberry! This is a
big step forward to download, manage and launch games and apps on μbrew, as
Panorama allows you to control the system via a gamepad. The port itself was
quite straight-forward and did not require a lot of changes. After we finished
porting the rest of the Panorama plugins we will look into merging the code with
the original repository, maybe we can run the Qt5 port on the Pyra in the
future.

### What works, and what doesn't

First of all, we added [QtGamepad
support](http://code.qt.io/cgit/qt-labs/qtgamepad.git/) to the Panorama UI. On
the Pandora, the gamepad input is done via a `pandora` plugin in Panorama, that
we cannot use because our hardware is different. QtGamepad provides a nice
alternative to the plugin and is probably the way to go for platform-independent
gamepad support in Panorama.

In addition, our fork of Panorama and its underlying PND management library
`libpndman` scans the root filesystem for [PND
files](http://pandorawiki.org/Introduction_to_PNDs) (in `/pandora`). This
required a minor change to the library, as the original code only looks into
filesystems on devices that are not mounted at `/`. So all PNDs that you put
in `/pandora` on the Raspberry will already show up under `Installed packages`.
The screenshot above already lists the famous Flappy Bird game.

Our Panorama version also syncs with the original Pandora repositories, you are
even able to download and install packages, but of course they won't start on
the Raspberry. Launching games in general does not work yet, we are currently
looking into some issues here. But we feel confident to provide a first version
for gamers soon!

If you already want to check out our Qt5 port of Panorama you can clone our
fork on GitHub:

[https://github.com/ubrew-it/panorama](https://github.com/ubrew-it/panorama)

