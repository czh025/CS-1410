"""
Project Name: Data Visualization Project
Author: Zhihui Chen
Due Date: 06/17/2022
Course: CS1410-X01

I declare that the following source code was written solely by me.
    I understand that copying any source code, in whole or in part, constitutes cheating, and that
    I will receive a zero on this project if I am found in violation of this policy.

This program can read all .dat file from current directory,
    finally output an .out file and a .pdf file
    out file shows the location where the pulse occurred
        and the area of the pulse from original data
    pdf file shows both original data and processed data figure
"""

import glob
import sys
import numpy as np
import matplotlib.pyplot as plt  # pylint: disable=import-error

VT = 100
PULSE_NUMBER = 50


def find_pulses(data, pulses, index=0):
    """Find every pulse in data.

    Use the recursion to find the data where is greater than VT, save the index to pulses,
    then skip the continuous rising data until a descending data appears, starts the next recursion

    :param list data: processed data
    :param list pulses: empty list for storing pulse
    :param int index: the index of data
    :return: a list of pulse index
    :rtype: list
    """
    if index >= len(data) - 2:
        return pulses
    if data[index + 2] - data[index] > VT:
        pulses.append(index)
        # skip the continuous rise
        while data[index + 1] > data[index]:
            index += 1
    return find_pulses(data, pulses, index + 1)


def process_data(raw_data):
    """Make the raw data into smoothed data.

    After processing data add first three and last three data from raw data into the smoothed data

    :param numpy.ndarray raw_data: unprocessed data
    :return: a list of processed data
    :rtype: list
    """
    data = [int((raw_data[i - 3] + 2 * raw_data[i - 2] + 3 * raw_data[i - 1] +
                 3 * raw_data[i] + 3 * raw_data[i + 1] + 2 * raw_data[i + 2] +
                 raw_data[i + 3]) // 15)
            for i in range(3, len(raw_data) - 3)]
    [data.insert(0, int(i)) for i in reversed(raw_data[:3])]
    [data.append(int(i)) for i in raw_data[-3:]]
    return data


def analyze(f_name):
    """Calling different functions in this function.

    read the raw data from f_name
    process raw data into smoothed data
    save data into a pdf file
    save data into a out file

    :param str f_name: file name
    """
    raw_data = np.loadtxt(f_name)
    smooth_data = process_data(raw_data)
    save_to_pdf(raw_data, smooth_data, f_name)
    save_to_out(raw_data, smooth_data, f_name)


def save_to_pdf(raw_data, smooth_data, file_name):
    """Save both raw data and smooth data to a .pdf file.

    The pdf shows both raw data and smooth data, the raw data's x-axis is invisible.
    Finally, save the figure to dpf file.

    :param numpy.ndarray raw_data: unprocessed data
    :param list smooth_data: processed data
    :param str file_name: file name
    """
    # ignore first variable
    _, axs = plt.subplots(2)

    # figure of raw data
    axs[0].plot(raw_data, lw=.2)
    axs[0].set(title=file_name, ylabel="raw")
    axs[0].axes.get_xaxis().set_visible(False)

    # figure of smooth data
    axs[1].plot(smooth_data, lw=.3)
    axs[1].set(ylabel="smooth")

    plt.savefig(f"{file_name[:-4]}.pdf")


def save_to_out(raw_data, smooth_data, file_name):
    """Save index and data of pulses to a .out file

    use smooth data to find the range, then use the range to retrieve the data from raw data
    pulse range up to 50, if the value in pulses list is not last one, it may end early

    :param numpy.ndarray raw_data: unprocessed data
    :param list smooth_data: processed data
    :param str file_name: file name
    """
    pulses = find_pulses(smooth_data, [], 0)
    with open(f"{file_name[:-4]}.out", "w", encoding="utf-8") as write_f:
        write_f.write(f"{file_name}:\n")
        for index, val in enumerate(pulses):
            pulse_range = PULSE_NUMBER
            # avoid double counting of area
            if index < len(pulses) - 1 and val + pulse_range > pulses[index + 1]:
                pulse_range = pulses[index + 1] - val
            pulse_range = min(pulse_range, len(smooth_data) - val)
            area = int(sum(raw_data[val:val + pulse_range]))
            write_f.write(f"Pulse {index + 1}: {val} ({area})\n")


def main():
    """Find all files with the dat extension in the current directory
    """
    # set maximum recursion limit to 10000
    sys.setrecursionlimit(10000)
    for f_name in glob.glob("*dat"):
        analyze(f_name)


if __name__ == "__main__":
    main()
