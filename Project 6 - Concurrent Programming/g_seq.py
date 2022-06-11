"""
Project Name: Concurrent Programming Project
Author: Zhihui Chen
Due Date: 06/23/2022
Course: CS1410-X01

I declare that the following source code was written solely by me.
    I understand that copying any source code, in whole or in part, constitutes cheating, and that
    I will receive a zero on this project if I am found in violation of this policy.

This program download img sequentially (no concurrency)
"""

import time
import os
import requests  # pylint: disable=import-error


def download_img(flag):
    """Only do download img.

    :param str flag: name of country flag
    :return: size of the img
    :rtype: int
    """
    url = f"https://www.sciencekids.co.nz/images/pictures/flags96/{flag}.jpg"
    img = requests.get(url).content
    with open(f"G_seq/{flag}.jpg", "wb") as img_f:
        img_f.write(img)
    return len(img)


def main():
    """Download img and record time
    """
    img_bytes = 0

    if not os.path.exists("G_seq"):
        os.makedirs("G_seq")

    with open("flags.txt", "r", encoding="utf-8") as flag_f:
        time_start = time.perf_counter()
        for flag in flag_f:
            img_bytes += download_img(flag.strip())
        time_stop = time.perf_counter()

    with open("G_seq_result.txt", "w", encoding="utf-8") as result_f:
        result_f.write(f"Elapsed time: {(time_stop - time_start):.8f}\n")
        result_f.write(f"{img_bytes} bytes downloaded")


if __name__ == "__main__":
    main()
