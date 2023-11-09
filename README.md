# 182 project

## Setup + Compile + Run Checker using libxml

```
sudo apt install libxml2-dev
gcc example_reader_validator.c -I/usr/include/libxml2 -lxml2
./a.out
```

## Setup + Run Python Script

```
python3 -m venv venv/
source venv/bin/activate
python3 -m pip install -r requirements.txt
python3 script.py
```