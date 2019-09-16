## Required Packages:
For CAN Bus communication on beagle bone: 
```
sudo apt-get install can-utils
pip install python-can
```
Installing [can-utils](https://github.com/linux-can/can-utils) will provide an 
installation of socketCAN for linux. Most linux installs will come with an 
implementation of socketCAN, though some really stripped down installs may omit it.

Installing [python-can](https://python-can.readthedocs.io/en/master/) provides an 
object-oriented python package for CAN that can use socketCAN as a backend.

## PARSEC's CANbus Configuration
Currently (16 Sept 2019), I (Julian) am planning on running our CANbus at a bitrate 
of 500 kb/s, and the beaglebone is configured to interface to the bus through
the channel 'can1', which is the CAN hardware connected to pins P9\_24 and P9\_26 as Rx and Tx pins, respectively. Thus, you would configure python-can's rc dictionary
```python
can.rc['interface'] = 'socketcan'
can.rc['channel']   = 'can1'
can.rc['bitrate']   = 500000
```
And to interface with CAN from the terminal using socketCAN/can-utils,
```bash
sudo ip link set can1 up type can bitrate 500000
sudo ip can1 up
```
You can then use the `candump` and `cansend` commands, passing 'can1' to `candump`'s
`<CAN interface>` field and `cansend`'s `<device>` field.

## Beaglebone Hardware Configuration
To enable the can1 device on the beaglebone, I followed the 
[instructions](https://elinux.org/Beagleboard:BeagleBoneBlack_Debian#U-Boot_Overlays)
for applying a U-bootoverlay to the beagle. Specifically I changed a line in 
`/boot/uEnv.txt` from
```
#uboot_overlay_addr4=/lib/firmware/<file4>.dtbo
```
to
```
uboot_overlay_addr4=/lib/firmware/BB-CAN1-00A0.dtbo
```
Namely, uncommenting the line and inserting the file from `/lib/firmware` containing
the device tree overlay object file for enabling CAN hardware and pinmux. Note that
many online sources will say you need to manually set the pinmux using config-pin,
but I find that the .dtbo file actually seems to lock in CAN as the setting for
the relevant pins and won't let you change it. This method may be valid if you
just want to enable CAN without booting with a device tree overlay. Also, to get
access to the device tree overlays and make sure it works properly, you should run
```
sudo apt-get install --upgrade-only bb-cape-overlays
```
This package should be installed on any Debian install meant for bealgebone, but
older versions seem to have trouble with CAN according to the [github issues](https://github.com/beagleboard/bb.org-overlays/issues), so updating just in case is a
a good move.

As of 16 Sept 2019 I've already done all of this hardware stuff for the beagle.
