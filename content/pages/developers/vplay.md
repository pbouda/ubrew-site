Title: Build and run a game with V-Play
Menuindex: 1

After reading this section you will be able to compile V-Play games with the
Qt Creator and run them on the Raspberry. Make sure that you successfully
[installed the μbrew development kit]({filename}ubrewkit.md).

# Clone the μbrew Flappy Bird repository

As an example game we will build and run the Flappy Bird demo that is also part
of V-Play and that is covered in [an excellent tutorial on the V-Play
website](http://v-play.net/doc/howto-flappybird-game/). For μbrew we will use
a specific fork of the code from the μbrew repository, as this version supports
gamepads and contains landscape mode graphics for monitors. To clone the
repository open a terminal and type:

    $ git clone https://github.com/ubrew-it/FlappyBird.git

This will download the μbrew code of Flappy Bird.

# Open the project in Qt Creator

Next, you open the project file of Flappy Bird in Qt Creator. Start the Qt
Creator that came with V-Play and choose `File -> Open File or Project...` from
the menu. Browse to the Flappy Bird folder and open `FlappyBird.pro`. Qt Creator
will open a page with the title `Configure Project`. Make sure you select the
Raspberry kit that you created for the μbrew development kit as shown in the
screenshot:

![Screen of Qt Creator dialog to Configure Project]({filename}/images/qt_creator_configureproject.png)

Then click on `Configure Project` to close the dialog and save your settings.
Qt Creator will now parse the project files and generate Makefiles to compile
the game later. Before we run the project, we still have to set the working
directory on the Raspberry in the project settings. Click on `Projects` in the
left pane of Qt Creator and choose the `Run` tab of the Raspberry kit:

![Screen of Qt Creator dialog for Run settings]({filename}/images/qt_creator_projects.png)

Under the heading `Run` you will find the setting for the `Working directory`.
Enter `/opt/FlappyBird` into the input field:

![Screen of Qt Creator dialog for Working directory]({filename}/images/qt_creator_workingdir.png)

You are now ready to start the game on the Raspberry. Make sure the Raspberry
is turned on and accessible over the local network. Qt Creator will try to
access the remote device via SSH, so make sure you the login works. If you
followed the instructions to install the μbrew development kit, the connection
settings are already stored in Qt Creator as part of the Qt kit. Click on the
`Run` button of Qt Creator in the lower left corner (the big green Play
button). Qt Creator will now compile, deploy and run the game on the Raspberry!

Feel free to play around with the Flappy Bird code to make yourself familiar
with Qt Creator and the development process. Whenever you change some code now
you can simply press `Run`, and the modified version will be started on the
Raspberry. Happy coding and gaming!
