import os
import subprocess
import time

import reset_lib

counter = 0
serial_last_four = subprocess.check_output(
    ["cat", "/proc/cpuinfo"])[-5:-1].decode("utf-8"  # noqa: COM812, S603, S607
)
config_hash = reset_lib.config_file_hash()
ssid_prefix = config_hash["ssid_prefix"] + " "
reboot_required = False


reboot_required = reset_lib.wpa_check_activate(
    config_hash["wpa_enabled"], config_hash["wpa_key"]
)

reboot_required = reset_lib.update_ssid(
    ssid_prefix, serial_last_four  # noqa: COM812
)

if reboot_required:
    os.system("reboot")  # noqa: S605, S607


# reset_lib.reset_to_host_mode()
