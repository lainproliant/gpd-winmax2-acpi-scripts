#!/usr/bin/python
# --------------------------------------------------------------------
# gpd-winmax2-acpi-wake.py
#
# Author: Lain Musgrove (lain.proliant@gmail.com)
# Date: Sunday February 19, 2023
#
# Distributed under terms of the MIT license.
# --------------------------------------------------------------------

import subprocess

# --------------------------------------------------------------------
ALLOWED_WAKE_DEVICES = ["LID0"]

# --------------------------------------------------------------------
def check(cmd) -> str:
    result = subprocess.run(cmd, check=True, capture_output=True, shell=True)
    return result.stdout.decode()

# --------------------------------------------------------------------
def check_lines(cmd) -> list[str]:
    return check(cmd).strip().split('\n')

# --------------------------------------------------------------------
def disable_device_wake(device):
    check(f'echo "{device}" > /proc/acpi/wakeup')

# --------------------------------------------------------------------
def get_enabled_wake_devices():
    return check_lines('cat /proc/acpi/wakeup | grep enabled | awk {\'print $1}\'')

# --------------------------------------------------------------------
def main():
    for device in get_enabled_wake_devices():
        if device not in ALLOWED_WAKE_DEVICES:
            print(f"Disabling wake for {device}.")
            disable_device_wake(device)

# --------------------------------------------------------------------
if __name__ == "__main__":
    main()
