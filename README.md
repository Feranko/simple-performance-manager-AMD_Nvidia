ok so this is made for simple stuf like get cpu, ram, iGPU, dGPU it was writed in python for simple work, probably  I work on a version writed in C++ or Rust or some speed language

dependencies:
	***Ubuntu:*** 
 update all the repo
```
sudo apt update -y && sudo apt upgrade
```
install dependencies
```
sudo apt install python3 python3-tk python3-dev radeontop
```
!!!Make sure you have installed  Nvidia Driver

***Arch:***
update and upgrade all the repo
```
sudo pacman -Syuu
```
install dependencies
```
sudo pacman -S python3 tk nvidia radeontop
```

after that you simply do chmod +x control_panel 
