#!/bin/sh
echo '[ Cyber Physical System for Environmental Monitoring Setup ]';
wait
echo '[Developed by:Sasha F Suhel]'
wait
echo '[Notice !!!!: Preparing... Make Sure RPi is connected to the Internet]'
sudo apt-get update
wait
sudo apt-get install build-essential python-dev
wait
sudo apt-get install git
wait
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
wait
cd Adafruit_Python_DHT
wait
sudo python3 setup.py install
wait
pip3 install numpy
wait
pip3 install pandas
wait
pip3 install matplotlib
wait
pip3 install pyserial
wait
sudo apt-get install qt5-default pyqt5-dev pyqt5-dev-tools
echo '[ COMPLETED !!!]'
