Title: Build the μbrew development kit for the Raspberry
Menuindex: 0

Before you can start to develop games for the μbrew gaming console you need
to build the μbrew development kit. Basically, it's a config file for Buildroot,
the V-Play binaries for the Raspberry and a set of scripts that build the system
for you. As a result you will get a Linux image to boot your Raspberry and
a toolchain to build games with the V-Play SDK for μbrew. The following steps
should be easy to follow, most of the work is done by the script in the μbrew
development repository. Depending on your computer's speed the whole build
might take a few hours to complete, though. But you can do something else
meanwhile, like going throught the tutorials of the V-Play SDK to learn how
to build your first game!


# Prerequisites

As we use Buildroot to create the Linux environment and the toolchain you need
to boot your computer with Linux. We recommend a distribution like
[Ubuntu](http://www.ubuntu.com/) or [Kubuntu](http://www.kubuntu.org/) as they
are easy to install and use. Just follow the instructions on the distribution's
website to install and boot Linux. The computer that you use to build Buildroot
and to create your games later is called the "host". The device that runs the
games is called the "target" (the Raspberry, in our case).


# Step 1: Install developer tools

You also need a toolchain with compiler, linker, etc. on your host. Ubuntu and
Kubuntu do not install all tools by default so you need to install them
manually. The easiest way to do this is to install the package
`build-essentials`. Open a terminal window and install the package by entering:

    $ sudo apt-get install build-essential

This will install all the necessary tools for the next steps on your computer.


# Step 2: Install V-Play SDK

V-Play is an advanced game engine with sophisticated tools to create your own
tools for desktop computers and mobile devices. The games that you develop
with V-Play a cross-platform, meaning that you can run your games on different
platforms (like your PC, iPhone and Android phone). Just download and install
the free version of V-Play for Linux from the V-Play website:

[https://v-play.net/download/](https://v-play.net/download/)

The V-Play download does not contain the necessary libraries for the Raspberry.
We will install the Raspberry binaries in the next step.


# Step 3: Build μbrew development kit

The μbrew development kit consists of a config file for
[Buildroot](http://buildroot.net/) and some scripts to install V-Play and
a gamepad library to the Buildroot environment. Buildroot does not only provide
a toolchain to build your games, but will also create a Linux file system that
we will install on an SD card later. As V-Play is based on
[Qt](http://www.qt.io/), the main purpose of our μbrew Buildroot config file is
to select all the mandatory packages for Qt and V-Play. For more information
about using Buildroot for Embedded Qt development please visit the [GitHub page
of the buildroot-qt-dev project](https://github.com/pbouda/buildroot-qt-dev).
The installer script of the μbrew development kit will use the
`buildroot-qt-dev` project to create the Buildroot environment.

First, you have to clone the μbrew development repository from GitHub:

    $ git clone https://github.com/ubrew-it/ubrew-dev-buildroot.git

The repository contains a script `install.sh` that will install the complete
μbrew development kit with Linux image and toolchain. You need to set the
environment variable `VPLAY_SDK_PATH` to point to you V-Play installation before
running the script. The standard path of the V-Play SDK is your home directory,
for example:

    $ export VPLAY_SDK_PATH=/home/user/V-PlaySDK

Then just run the `install.sh` script:

    $ ./install.sh

This will start the build process, which may take several hours. Check out
some of the V-Play tutorials meanwhile, and learn to build your first game!

[http://v-play.net/doc/](http://v-play.net/doc/)

# Step 4: Prepare SD card

The SD card has to co be prepared with a certain partition layout in order to
be bootable on the Raspberry. The standard layout is a small FAT partition and
a larger ext4 partition in this order. The easiest way to prepare the card is
to install a standard Raspbian on the card. This will also install the
mandatory binary firmware and license to boot the Raspberry. You can find
information about the process on the Raspberry download page:

[https://www.raspberrypi.org/downloads/](https://www.raspberrypi.org/downloads/)

Just follow the instructions given on the page under the `Raspbian` heading.


# Step 5: Install μbrew Linux image on SD card

To install the root file system we will now format the second partition on the
SD card with an ext4 file system, extract the file system that Buildroot created
and copy the Buildroot kernel onto the first FAT partition. The repository
contains the file `buildroot-qt-dev/script/installrootfs.sh` that executes all
commands. The script needs to know the device of your SD card. Please check
carefully which device your SD card uses and adapt the script. Currently the
device for the SD card is `/dev/sdX`. Change those device names to your setup
*in all locations*.

If your SD card is still mounted from the previous step you might just call
`mount` to see a list of all file systems. Find your SD card in this list and
use the device names that are listed (like `/dev/sdc1` and `/dev/sdc2`).

*Careful: Your SD card has to prepared with the two Raspberry partitions. If
you do not edit the script `installrootfs.sh` with the correct device names
your hard disk might get formatted!*

You can now run the script. The script expects the path to the root file system
image and the kernel as the first argument. Buildroot puts those in the folder
`output/images`. So change directory into `scripts` and run `installrootfs.sh`
with the absolute path to your `buildroot-2015.05/output/images` folder:

    $ cd buildroot-qt-dev/scripts/
    $ ./installrootfs.sh /path/to/buildroot-qt-dev/buildroot-2015.05/output/images

This will format, extract and copy. After the script finishes it is safe to
remove the SD card from your computer and insert it into your Raspberry. Power
on the Raspberry and see the system boot. If you attached a network cable
you should be able open a shell via SSH. The username is `root` with password
`raspi`. Here is a nice one liner to find your Raspberry on the network (needs
`nmap` installed):

    $ sudo nmap -sP 192.168.1.0/24 | awk '/^Nmap/{ip=$NF}/B8:27:EB/{print ip}'

[via [pierre-o's Known](https://microblog.pierre-o.fr/2015/one-liner-to-find-raspberrypi-on-your-local-network)]


# Step 6: Prepare Qt Creator for cross-compilation

To develop games for the Raspberry we will use the Qt Creator that comes with
V-Play. It provides a light-weight IDE for Qt development with several tools
that make your life as a developer much easier. But first, we have to add the
Qt version of the Buildroot environment as a so-called "Kit" in Qt Creator.

Start by opening the Qt Creator that was shipped with V-Play. It should be
installed as a standard application that you can find in your Linux application
menu. Alternatively you can start `qtcreator` in your V-Play installation at
`V-PlaySDK/Tools/QtCreator/bin`.

Now open the options dialog in the menu `Tools -> Options...`. Open the section
`Devices` of the dialog. Here we will add the Raspberry as a remote device, so
that we can deploy and run any game later on the Raspberry. This requires the
Raspberry to be turned on and connected to the local network. If you followed
all the above steps and connected a network cable to the Raspberry
everything should work fine. As a reminder, to find the IP address of your
Raspberry on the network you can type:

    $ sudo nmap -sP 192.168.1.0/24 | awk '/^Nmap/{ip=$NF}/B8:27:EB/{print ip}'

Then enter the IP address, the user name ("root"), the password ("raspi") and
a device name ("Raspi 2", for example) in the dialog, like shown in the
following screenshot:

![Screen of Qt Creator dialog for Devices]({filename}/images/qt_creator_devices.png)

Next, change to the section `Build & Run`. Here we will add the GCC compiler of
Buildroot. Click on the tab `Compilers` and then on `Add -> GCC`. Next to the
field `Compiler path` click on `Browse...` and browse to the Buildroot
directory. The cross-compiler `arm-buildroot-linux-gnueabihf-g++` is stored in
`output/host/usr/bin`, the full path might look something like:

    /path/to/ubrew-dev-buildroot/buildroot-qt-dev/buildroot-2015.05/output/host/usr/bin/arm-buildroot-linux-gnueabihf-g++

Select the compiler and set a name to find it later (like "GCC Raspi 2 V-Play"):

![Screen of Qt Creator dialog for compilers]({filename}/images/qt_creator_compilers.png)

Parallel to the compiler we need to set the path to `qmake` in Buildroot.
Change to the tab `Qt versions` and click on `Add...`. Browse again to the
`output/host/usr/bin` of Buildroot and select the `qmake` there. Don't forget
to set a name for your Qt version:

![Screen of Qt Creator dialog for Qt Versions]({filename}/images/qt_creator_qtversions.png)

The last step is to create a kit from the device, compiler and the Qt version.
You need to click on `Apply` now in the dialog so that all settings are stored.
Change to the tab `Kits` and click `Add`. Now enter a name for the kit and
choose the device, compiler and Qt version that you just created from the
drop-down lists:

![Screen of Qt Creator dialog for Kits]({filename}/images/qt_creator_kits.png)

To store your settings click `OK` in the dialog. You are now ready to run your
first game on the Raspberry!


# Next steps

When you finished the setup of the μbrew development kit it is time to build
your first game with V-Play. In the next section you will learn how to compile
and run Flappy Bird on the Raspberry.

[Create a game with V-Play]({filename}vplay.md)


# More info

* [Buildroot website](http://buildroot.net/)
* [Qt website](http://www.qt.io/)
* [V-Play Game Engine website]()