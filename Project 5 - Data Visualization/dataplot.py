"""
Project Name: Data Visualization Project
Author: Zhihui Chen
Due Date: 06/17/2022
Course: CS1410-X01

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
    """
    use the recursion to find the data where is great then VT, save the index to pulses,
    then skip the continuous rising data until a descending data appears, starts the next recursion
    return list
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
    """
    Make the raw data into smoothed data
    finally add the first three and last three data from the raw data into the smoothed data
    return list
    """
    data = [int((raw_data[i - 3] + 2 * raw_data[i - 2] + 3 * raw_data[i - 1] +
                 3 * raw_data[i] + 3 * raw_data[i + 1] + 2 * raw_data[i + 2] +
                 raw_data[i + 3]) // 15)
            for i in range(3, len(raw_data) - 3)]
    [data.insert(0, int(i)) for i in reversed(raw_data[:3])]
    [data.append(int(i)) for i in raw_data[-3:]]
    return data


def analyze(f_name):
    """
    read the raw data from f_name
    process raw data into smoothed data
    save data into a pdf file
    save data into a out file
    """
    raw_data = np.loadtxt(f_name)
    smooth_data = process_data(raw_data)
    save_to_pdf(raw_data, smooth_data, f_name)
    save_to_out(raw_data, smooth_data, f_name)


def save_to_pdf(raw_data, smooth_data, file_name):
    """
    the pdf shows both raw data and smooth data,
    the raw data's x-axis is invisible
    finally save the figure to dpf file
    """
    fig, axs = plt.subplots(2)

    axs[0].plot(raw_data, lw=.2)
    axs[0].set(title=file_name, ylabel="raw")
    axs[0].axes.get_xaxis().set_visible(False)

    axs[1].plot(smooth_data, lw=.3)
    axs[1].set(ylabel="smooth")

    # plt.show()
    plt.savefig(f"{file_name[:-4]}.pdf")


def save_to_out(raw_data, smooth_data, file_name):
    """
    use smooth data to find the range, then use the range to retrieve the data from raw data
    pulse range up to 50, if the value in pulses list is not last one, it may end early
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
    """
    set maximum recursion limit to 10000
    find all files with the dat extension in the current directory
    """
    sys.setrecursionlimit(10000)
    for f_name in glob.glob("*dat"):
        analyze(f_name)


if __name__ == "__main__":
    main()
