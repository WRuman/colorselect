import RPi.GPIO as gpio
from time import sleep
import signal as sig
import sys

DEFAULT_FREQ = 120
HI_IS_OFF = True
SLEEP_T = 1.0
pwm_pins = [11, 13, 15]
pwm_handles = []

def _setup():
    global pwm_handles
    gpio.setmode(gpio.BOARD)
    for pin in pwm_pins:
        gpio.setup(pin, gpio.OUT)
        p = gpio.PWM(pin, DEFAULT_FREQ)
        p.start(0.0)
        pwm_handles.append(p)

def _set_rgb_duty(p, v):
    frac = v / 255.0
    if HI_IS_OFF:
        frac = 1 - frac
    p.ChangeDutyCycle(frac * 100)

def _rgb_from_input(msg):
    r = 0
    g = 0
    b = 0
    if msg.startswith('#') and len(msg) == 7:
        r = int(msg[1:3], 16)
        g = int(msg[3:5], 16)
        b = int(msg[5:7], 16)
    print("Using ({}, {}, {})".format(r, g, b))
    return (r, g, b)


def _repl():
    while True:
        print("Enter an RGB value in hex form (e.g. #FF8500)")
        msg = input("> ")
        set_color(msg)

def _cleanup(signal, frame):
    print("Cleaning up...")
    gpio.cleanup()
    sys.exit(0)

def set_color(rgb_code):
    rgb = _rgb_from_input(rgb_code)
    _set_rgb_duty(pwm_handles[0], rgb[0])
    _set_rgb_duty(pwm_handles[1], rgb[1])
    _set_rgb_duty(pwm_handles[2], rgb[2])

def cli():
    start()
    _repl()

def start():
    sig.signal(sig.SIGINT, _cleanup)
    _setup()
    sleep(SLEEP_T)
