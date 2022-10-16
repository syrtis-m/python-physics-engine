# python-physics-engine
 built for HACK WashU 2022. 
 works with a raspberry pi and a unicorn hat HD
 using FastLine: https://github.com/MrGolden1/FastLine

TODO:
- figure out why collision alg will throw objects DNE errors when it trys to remove them from list
- make collision alg more efficient (figure out Big-O runtime :D)

## setup
- put the Unicorn Hat HD onto your raspberry pi's GPIO pins
- install unicornhathd from https://github.com/pimoroni/unicorn-hat-hd
- install FastLine `pip3 install FastLine`
- clone this repo
- run `python3 main.py` for demos