# ADB select
Quickly run commands on a device without having to type `adb -s SOMEDEVICEID blah blah blah`. Useful if you use ADB from the terminal with multiple devices connected.

# Installation
1. Paste this file somewhere in your executable path (I have a `~/scripts` directory as part of my $PATH)
2. Make it executable `chmod +x adb-select.py`
3. Alias the command for quicker invocation. Add `alias adbs='adb-select.py` to your `.bash_profile`.
4. Reload your bash profile `source ~/.bash_profile`

# Selecting a device
Invoke `adbs` or `adb-select.py` to select from connected devices
```
ben$ adbs
0) emulator-5554          device product:sdk_gphone_x86 model:Android_SDK_built_for_x86 device:generic_x86
1) 8XV7N16116005231       device usb:342032384X product:angler model:Nexus_6P device:angler
Enter selection [0 - 1] >> 1
```
# Running ADB commands to the selected device
Run any ADB command, but use `adbs` instead of `adb` at the beginning
```
ben$ adbs uninstall com.bendaschel.myapp
Success
```
