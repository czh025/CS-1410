"""
Project Name: Human Pyramids Project
Author: Zhihui Chen
Due Date: 05/25/2022
Course: CS1410-X01

In order for this program to run properly, it needs to accept an input from the user (e.g. python3 pyramid.py 7)
This program uses recursion to calculate the weight each person bears in the pyramid
    and uses cache to avoid unnecessary calculations
The weight of each person bears, the time the program runs, the number of recursions, and the number of cache uses
    will eventually be written to a file called part2.txt
"""

import sys
import time

cache = {}


def weight_on(r, c, count=0, cache_hits_count=0, weight=200.0):
    """
    r: int, rows from iteration
    c: int, column from iteration
    count: int, count how many times the function has been run
    cache_hits_count: num, count how many times the cache has been use
    weight: float, human's weight

    total: float, total weight that person holding up

    this function accepts two parameter: r and c, in order to calculate the weight hold up by each person in pyramid
    after each calculation, the data will be stored in the cache to avoid repeated calculations

    return:
    total, count, and cache_hits_count
    """
    global cache
    total = 0.0
    count += 1
    if cache.get((r, c)) is not None:
        cache_hits_count += 1
        return [cache[(r, c)], count, cache_hits_count]
    else:
        if r == 1:
            # first column
            cache[(r, c)] = total
            return [total, count, cache_hits_count]
        elif r > c == 1:
            # leftmost person
            previous_row = weight_on(r - 1, c, count, cache_hits_count)
            total += round((weight + previous_row[0]) / 2, 2)
            cache_hits_count += previous_row[2]
            cache[(r, c)] = total
            return [total, previous_row[1], cache_hits_count]
        elif r == c:
            # rightmost person
            previous_row = weight_on(r - 1, c - 1, count, cache_hits_count)
            total += round((weight + previous_row[0]) / 2, 2)
            cache_hits_count += previous_row[2]
            cache[(r, c)] = total
            return [total, previous_row[1], cache_hits_count]
        else:
            # people in interior
            previous_row_left = weight_on(r - 1, c - 1, count, cache_hits_count)
            # count = 0: avoid double counting!!!!!
            previous_row_right = weight_on(r - 1, c, count=0, cache_hits_count=cache_hits_count)
            total += round((weight * 2 + previous_row_left[0] + previous_row_right[0]) / 2, 2)
            cache_hits_count += previous_row_left[2] + previous_row_right[2]
            cache[(r, c)] = total
            return [total, previous_row_left[1] + previous_row_right[1], cache_hits_count]


def main():
    """
    rows: int, from user's input, it should be an integer
    file: for storing final data
    function_calls_times: int, storing the number of times the weight_on function has been run after each loop
    cache_hits_times: int, storing the number of times the cache has been used after each loop
    time_start, time_stop: calculate the time consumed by the function to run
    """
    try:
        rows = int(sys.argv[1])
    except ValueError:
        return print("Please enter an integer (e.g. 7). ")
    file = open("part2.txt", "w")
    function_calls_times = 0
    cache_hits_times = 0

    time_start = time.perf_counter()
    for row in range(1, rows + 1):
        line = ""
        # start with 1, not 0
        for column in range(1, row + 1):
            result = weight_on(row, column)
            line += f"{result[0]:.2f}\t"
            function_calls_times += result[1]
            cache_hits_times += result[2]
        file.write(f"{line}\n")
    time_stop = time.perf_counter()
    file.write(f"Elapsed time: {(time_stop - time_start):.20f} seconds\n")
    file.write(f"Number of function calls: {function_calls_times}\n")
    file.write(f"Number of cache hits: {cache_hits_times}")


if __name__ == "__main__":
    main()
