"""
Project Name: Human Pyramids Project
Author: Zhihui Chen
Due Date: 05/25/2022
Course: CS1410-X01

Put your description here, lessons learned here, and any other information someone using your
program would need to know to make it run.
"""

import sys
import time


def main():
    """
    TODO
    """
    rows = int(sys.argv[1])
    file = open("part2.txt", "w")
    weight = 200.00

    def weight_on(r, c, count=0):
        """
        r: rows
        c: column
        """
        total = 0.0
        count += 1
        if r == 1:
            # first column
            return [total, count]
        elif r > c == 1:
            # leftmost person
            previous_row = weight_on(r - 1, c, count)
            total += round((weight + previous_row[0]) / 2, 2)
            return [total, previous_row[1]]
        elif r == c:
            # rightmost person
            previous_row = weight_on(r - 1, c - 1, count)
            total += round((weight + previous_row[0]) / 2, 2)
            return [total, previous_row[1]]
        else:
            # people in interior
            previous_row_left = weight_on(r - 1, c - 1, count)
            # avoid double counting!!!!!
            count = 0
            previous_row_right = weight_on(r - 1, c, count)
            total += round((weight * 2 + previous_row_left[0] + previous_row_right[0]) / 2, 2)
            return [total, previous_row_left[1] + previous_row_right[1]]

    function_calls_times = 0
    time_start = time.perf_counter()
    for row in range(1, rows + 1):
        line = ""
        for column in range(1, row + 1):
            result = weight_on(row, column)
            line += f"{result[0]:.2f} "
            function_calls_times += result[1]
        file.write(f"{line}\n")
    time_stop = time.perf_counter()
    file.write(f"Elapsed time: {time_stop - time_start} seconds\n")
    file.write(f"Number of function calls: {function_calls_times}")


if __name__ == "__main__":
    main()

