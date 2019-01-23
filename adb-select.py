#!/usr/bin/env python
import sys
import os
import subprocess
import os.path

def get_file_path():
    return os.path.expanduser("~/.adb-select")

def map_device_id(line):
    """
    :param line: adb device line
    :type line: str
    :return:
    """
    return line.split()[0]

def format_selection_line(index, adb_raw_line):
    return '%d) %s' % (index, adb_raw_line)

def write_selection(device_id):
    output_path = get_file_path()
    with open(output_path, "w") as output:
        output.write(device_id)

def adb_select():
    output = subprocess.check_output(["adb", "devices", "-l"])
    # Must decode byte literal to UTF-8 for proper print formatting
    lines = [line.decode("utf-8") for line in output.splitlines()[1::] if len(line) > 0]
    device_ids = [map_device_id(line) for line in lines]
    prompt_items = [format_selection_line(i, line) for i, line in enumerate(lines)]
    
    for item in prompt_items:
        print(item)

    max_item_index = len(prompt_items) -1
    selection = -1
    while selection < 0 or selection > max_item_index:
        try:
            selection = int(input("Enter selection [0 - %d] >> " % max_item_index))
        except ValueError:
            pass

    write_selection(device_ids[selection])

def run_adb():

    selection = ""
    with open(get_file_path(), 'r') as input_file:
        selection = input_file.readline()

    if selection == "":
        print("No device selected; exiting")
        return

    args = ["adb", "-s", selection] + sys.argv[1::]
    subprocess.call(args)

def main():
    if len(sys.argv) > 1:
        run_adb()
    else:
        adb_select()


if __name__ == '__main__':
    main()
