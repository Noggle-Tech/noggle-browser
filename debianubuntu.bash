echo "Now installing Python 3 and the required dependencies for Noggle Browser"
echo "If you already have these programs installed, they will not install during runtime"
echo "This program assumes you are running Debian, Ubuntu, or other Debian-based distributions"

sudo apt-get update
sudo apt-get install -y python3
sudo apt-get install -y python3-pyqt5
sudo apt-get install -y python3-pyqt5.qtwebengine

echo "Done."