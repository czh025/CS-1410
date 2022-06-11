"""
Project Name: Concurrent Programming Project
Author: Zhihui Chen
Due Date: 06/23/2022
Course: CS1410-X01

I declare that the following source code was written solely by me.
    I understand that copying any source code, in whole or in part, constitutes cheating, and that
    I will receive a zero on this project if I am found in violation of this policy.

This program download img concurrently using futures with threads
"""

import time
import os
from concurrent.futures import ThreadPoolExecutor
import requests  # pylint: disable=import-error


def download_img(flag):
    """Only do download img.

    :param str flag: name of country flag
    :return: size of the img
    :rtype: int
    """
    url = f"https://www.sciencekids.co.nz/images/pictures/flags96/{flag}.jpg"
    img = requests.get(url).content
    with open(f"G_thread/{flag}.jpg", "wb") as img_f:
        img_f.write(img)
    return len(img)


def main():
    """Download img with ThreadPoolExecutor and record time

    Read flags.txt file,
    save total download img size
    write result to G_thread_result.txt
    """
    # if G_thread folder does not exist, create it
    if not os.path.exists("G_thread"):
        os.makedirs("G_thread")

    with open("flags.txt", "r", encoding="utf-8") as flag_f:
        flags = [flag.strip() for flag in flag_f]

    time_start = time.perf_counter()
    with ThreadPoolExecutor() as executor:
        img_bytes = sum(executor.map(download_img, flags))
    time_stop = time.perf_counter()

    with open("G_thread_result.txt", "w", encoding="utf-8") as result_f:
        result_f.write(f"Elapsed time: {(time_stop - time_start):.8f}\n")
        result_f.write(f"{img_bytes} bytes downloaded")


if __name__ == "__main__":
    main()
