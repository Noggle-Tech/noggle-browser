# Noggle Browser

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/ee4c4db5fce84ca6ba2bddfe6d408f03)](https://www.codacy.com/gh/Noggle-Tech/noggle-browser/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Noggle-Tech/noggle-browser&amp;utm_campaign=Badge_Grade)<br>
**Please make sure you have all prerequisites installed before making an issue. Saves a lot of time. Thanks!**

A new browsing experience that's really... really... slow. Not internet explorer slow, but whatever. Based on Chromium. Coded in Python using PyQt5. Designed for NationStates.

## Prerequisites

Python 3, PyQt5, PyQtWebEngine

### Windows and MacOS

On Windows, you should be able to run installdep.bat to install the dependencies. If that doesn't work, or you're on MacOS, do these steps below:

[Download Python for Windows or Macintosh](https://www.python.org/downloads/)

Get PyQt5 via pip
`pip install PyQt5`

Get PyQtWebEngine via pip
`pip install PyQtWebEngine`

### Linux

#### Debian and Ubuntu

Run `./debianubuntu.bash` on your command line in the directory Noggle Browser is installed in to get the dependencies. If it says it is unexecutable, or something along those lines, run `chmod 755 debianubuntu.bash` in the directory Noggle Browser is installed in to make the file executable.

#### Other Distributions

Yeah, I'll get around to the other distros eventually.

Python 3 should still come preinstalled on most Linux distributions. For PyQt5 and PyQtWebEngine, check with your distribution's package list.

Some package lists:

[Fedora](https://src.fedoraproject.org/)<br>
[Arch](https://archlinux.org/packages/)<br>
[Gentoo](https://packages.gentoo.org/)<br>
[Linux Mint](http://packages.linuxmint.com/)<br>
[Manjaro](https://discover.manjaro.org/packages/)<br>

## Running the Program

Navigate to the directory the `noggle.py` file is in, which will be 2 directories down from the place you extracted to. Then run the command `python3 noggle.py` (or `py noggle.py`) or run it directly from your file manager.

## Known Issues

On sites that open links in new tabs, you'll have to middle click the link that opens in a new tab. The fix for this would be to add tabs, which I can't be bothered to do right now, but will probably eventually fix it.

## Trying to Install Extensions

It won't work :)