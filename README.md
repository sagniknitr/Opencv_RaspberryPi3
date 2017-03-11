# Camera library
![Camera Library logo](https://github.com/danny270793/Camera/blob/master/images/picamera.png)

Project description:

 * Control the Raspberry Pi camera.


## Download code
Install git and clone the repository
```
sudo apt-get install git
```
Install the openCV library and the PiCamera library
```
sudo apt-get install python-opencv
sudo apt-get install python-picamera
```
Install numpy
```
sudo apt-get install python-numpy
```
## Enable the camera module
```
sudo raspi-config
```
Select "6 Enable Camera"<br>
![raspi-config execution](https://github.com/danny270793/Camera/blob/master/images/raspiconfig.png)<br>
Confirm you want to enable it<br>
![Enable module](https://github.com/danny270793/Camera/blob/master/images/enable.png)<br>
And that its all<br>
![Module enabled](https://github.com/danny270793/Camera/blob/master/images/enabled.png)<br>
At the end it will ask you for reboot, reboot it<br>
![Ask for reboot](https://github.com/danny270793/Camera/blob/master/images/reboot.png)<br>
Download the Gpio library code
```
sudo git clone https://github.com/danny270793/Camera.git
cd Camera
