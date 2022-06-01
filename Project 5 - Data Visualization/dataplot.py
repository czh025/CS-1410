"""
Project Name: Data Visualization Project
Author: Zhihui Chen
Due Date: 06/17/2022
Course: CS1410-X01

Put your description here, lessons learned here, and any other information someone using your
program would need to know to make it run.
"""

import numpy as np
import matplotlib.pyplot as plt
import glob
import sys

VT = 100
PULSE_NUMBER = 50


def find_pulses(data, pulses, index=0):
    if index >= len(data) - 2:
        return pulses
    if data[index + 2] - data[index] > VT:
        pulses.append(index)
        # skip the continuous rise
        while data[index + 1] > data[index]:
            index += 1
    return find_pulses(data, pulses, index + 1)


def process_data(raw_data):
    data = [int((raw_data[i - 3] + 2 * raw_data[i - 2] + 3 * raw_data[i - 1] +
                 3 * raw_data[i] + 3 * raw_data[i + 1] + 2 * raw_data[i + 2] +
                 raw_data[i + 3]) // 15)
            for i in range(3, len(raw_data) - 3)]
    [data.insert(0, int(i)) for i in reversed(raw_data[:3])]
    [data.append(int(i)) for i in raw_data[-3:]]
    return data


def analyze(f_name):
    raw_data = np.loadtxt(f_name)
    data = process_data(raw_data)
    save_to_pdf(raw_data, data, f_name)
    save_to_out(raw_data, data, f_name)


def save_to_pdf(raw_data, smooth_data, file_name):
    fig, axs = plt.subplots(2)

    axs[0].plot(raw_data, lw=.2)
    axs[0].set(title=file_name, ylabel="raw")
    axs[0].axes.get_xaxis().set_visible(False)

    axs[1].plot(smooth_data, lw=.3)
    axs[1].set(ylabel="smooth")

    # plt.show()
    plt.savefig(f"{file_name[:-4]}.pdf")


def save_to_out(raw_data, smooth_data, file_name):
    pulses = find_pulses(smooth_data, [], 0)
    with open(f"{file_name[:-4]}.out", "w", encoding="utf-8") as write_f:
        write_f.write(f"{file_name}:\n")
        for i in range(len(pulses)):
            start_pulse = pulses[i]
            pulse_range = PULSE_NUMBER
            # avoid double counting of area
            if i < len(pulses) - 1 and pulses[i] + pulse_range > pulses[i + 1]:
                pulse_range = pulses[i + 1] - start_pulse
            pulse_range = min(pulse_range, len(smooth_data) - start_pulse)
            area = int(sum(raw_data[start_pulse:start_pulse + pulse_range]))
            write_f.write(f"Pulse {i + 1}: {start_pulse} ({area})\n")

def main():
    """
    Program starts here.
    """
    # set maximum recursion limit to 10000
    sys.setrecursionlimit(10000)
    for f_name in glob.glob("*dat"):
        analyze(f_name)


if __name__ == "__main__":
    main()
