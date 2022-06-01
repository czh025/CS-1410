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
    pulses = find_pulses(data, [], 0)
    print(f"{f_name}:")
    for i in range(len(pulses)):
        start_pulse = pulses[i]
        pulse_range = PULSE_NUMBER
        # avoid double counting of area
        if i < len(pulses) - 1 and pulses[i] + pulse_range > pulses[i + 1]:
            pulse_range = pulses[i + 1] - start_pulse
        pulse_range = min(pulse_range, len(data) - start_pulse)
        area = int(sum(raw_data[start_pulse:start_pulse + pulse_range]))
        print(f"Pulse {i + 1}: {start_pulse} ({area})")


def main():
    """
    Program starts here.
    """
    sys.setrecursionlimit(5000)
    # plt.figure(figsize=(48, 27))
    for f_name in glob.glob("*dat"):
        analyze(f_name)
    # t = np.arange(0., 5., 0.2)
    # plt.plot(t, t, 'rs', t, t ** 2, 'bs', t, t ** 3, 'g^')
    #
    # # print(t)
    # # plt.plot([1, 2, 3, 4], [2, 3, 3, 2])
    # plt.ylabel("some numbers")
    # plt.show()


if __name__ == "__main__":
    main()
