import RPi.GPIO as GPIO
import os
import time
import sys
sys.stdout = open('/home/pi/internet-power.log','a')
pin=18
cycle_down_time=20
cycle_wait_for_internet=60 * 3
def power_on():
    log("\tpower on")
    GPIO.output(pin, 1)
    
def power_off():
    log("\tpower off")
    GPIO.output(pin, 0)

def setup(): 
    log("initializing")
    log("\tGPIO.VERSION {0}".format(GPIO.VERSION))
    GPIO.setmode(GPIO.BCM)
    log("\tset mode to GPIO.BCM")
    GPIO.setup(pin, GPIO.OUT)
    log ("\tset pin #{0}  to OUT".format(pin))
    power_on()
    log("initializing complete")


def power_cycle():
    log("starting power cycle, {0}s downtime, {1}s wait time".format(cycle_down_time, cycle_wait_for_internet))
    power_off()
    time.sleep(cycle_down_time)
    power_on()
    time.sleep(cycle_wait_for_internet)
    log("power cycle complete")

def log(message):
    print("{0}: {1}".format(time.strftime("%Y-%m-%d %H:%M:%S"), message))

try: 
    setup()
    while True:
        hostname = "google.com"
        response = os.system("ping -c 1 " + hostname + "  > /dev/null 2>&1")
        if(response != 0):
            log("Internet appears down")
            power_cycle()
        else: 
            time.sleep(10)
finally:
    GPIO.cleanup()