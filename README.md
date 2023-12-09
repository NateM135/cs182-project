# 182 project

## Setup + Compile + Run Checker using libxml

### Linux Setup

```
sudo apt install libxml2-dev
gcc validate.c -I/usr/include/libxml2 -lxml2
./a.out example1.xml
```

### Mac Setup

```
brew install libxml2-dev
gcc validate.c -lxml2
./a.out example1.xml
```

### Windows Setup

- Install libxml2 headers vian preferred installation methods, suggested is pacman via msys2.

```
gcc validate.c -lxml2
./a.exe example1.xml
```


## Setup + Run Python Script

The following lines of code carry out the following tasks:

- Create a new virtual environment that we can use to install dependencies in an isolated environment
- Activate the virtual environemnt, overwriting our PATH so that pip and python no longer point to the system binaries but to the virtual environment
- Install dependencies using the requirements.txt file provided. This downloads all the needed python libraries and sets it up according to your local system
- Run the script. Note that the libxml validation program must be compiled prior to running the script. Note that the script will take a significant amount of time to execute to older machines and outputs files with a visual view of the results and debug info.


```
python3 -m venv venv/
source venv/bin/activate
python3 -m pip install -r requirements.txt
python3 script.py
```
