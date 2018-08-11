# Internet down reboot!

This is a script for raspberry pi, which controls a relay on port 18. When the internet goes down, if flips the relay to
power cycle anything that might be attached.

## installation
1. put internet-power.py at the root of your rasberrypi, 
2. add
```
python3 /home/internet-power.py
```
to your /etc/rc.local before the `exit 0` line.
3. reboot your pi.

## Parts
1. https://www.amazon.com/SunFounder-Channel-Optocoupler-Expansion-Raspberry/dp/B00E0NTPP4
2. a raspberry pi
3. a power outlet
4. power cord
5. power box

## Assembly
all of this should be done so that the power outlet and the relay are inside the elecrtical junction box

Hook up your pi to your relay similar to how it's done here https://randomnerdtutorials.com/guide-for-relay-module-with-arduino/

hook your hot power cord up to the relay, then the other side of the relay to the hot side of the power outlet.

hook up ground and cold to directly to the power outlet.

Start your pi, and plug in the power cord.
