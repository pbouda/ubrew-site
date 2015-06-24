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
and to create your games later is called the "host".


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


# Step 3: Install μbrew development kit

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

    $ export VPLAY_SDK_PATH=/home/pbouda/VPlay-SDK

The just run the `install.sh` script:

    $ install.sh

This will start the build process, which may take several hours. Check out
some of the V-Play tutorials meanwhile, and learn to build your first game!

[http://v-play.net/doc/](http://v-play.net/doc/)


# Step 4: Prepare Qt Creator for cross-compilation

TODO


# More info

* [Buildroot website](http://buildroot.net/)
* [Qt website](http://www.qt.io/)
* [V-Play Game Engine website]()