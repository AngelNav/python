import subprocess
import re

command_output = subprocess.run(
    ["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode()

profile_names = (re.findall("All User Profile     : (.*)\r", command_output))

wifi_list = list()


if len(profile_names) != 0:
    for name in profile_names:
        # Every wifi connection will need its own dictionary which will be appended
        wifi_profile = dict()

        profile_info = subprocess.run(
            ["netsh", "wlan", "show", "profile", name], capture_output=True).stdout.decode()

        # We use a regular expression to only look for the absent cases
        if re.search("Security key           : Absent", profile_info):
            continue
        else:
            # Assign the ssid of the wifi profile to the dictionary
            wifi_profile["ssid"] = name
            profile_info_pass = subprocess.run(
                ["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output=True).stdout.decode()
            password = re.search(
                "Key Content            : (.*)\r", profile_info_pass)

            # Check if we found a password in the regular expression. All wifi connection will not hacked
            if password == None:
                wifi_profile["password"] = None
            else:
                wifi_profile["password"] = password[1]

            wifi_list.append(wifi_profile)

for x in range(len(wifi_list)):
    print(wifi_list[x])
