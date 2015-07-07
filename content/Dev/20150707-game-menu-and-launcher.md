Title: Game menu and app launcher
Date: 2015-07-07 09:27
Image: /images/blog/default.png

I was looking for an existing solution for an app launcher on mobile and
embedded devices that we could use to present and launch games on the μbrew
console. Ideally, it should also support package management with online
repositories. I read about the [PND package manager on the
OpenPandora](http://pandorawiki.org/Libpnd_hub) last week and found the solution
both simple and quite perfect for our purposes. Looking for a Qt-based
application launcher I finally found the Panorama launcher, which was also
developed for the Pandora:

[https://github.com/bzar/panorama](https://github.com/bzar/panorama)

I am now working on a Qt5 port of the Panorama (and its backend,
[qtpndman](https://github.com/bzar/qtpndman)). The pndman Qt wrapper `qtpndman`
was easy to port, as it doesn't not contain any UI. Panorama seems to involve
some more work on porting from the deprecated Declarative module to the Quick
and Qml modules, but until now it's still straight-forward. I am also learning
a lot about the cmake build system. You can follow the progress in our forks
of the repositories:

* [https://github.com/ubrew-it/qt5pndman](https://github.com/ubrew-it/qt5pndman)
* [https://github.com/ubrew-it/panorama](https://github.com/ubrew-it/panorama)

### More info

* [Porting QML Applications to Qt5](http://doc.qt.io/qt-5/qtquick-porting-qt5.html)
* [CMake build system](http://www.cmake.org/)
