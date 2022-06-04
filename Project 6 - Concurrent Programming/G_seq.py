"""
Project Name: Concurrent Programming Project
Author: Zhihui Chen
Due Date: 06/23/2022
Course: CS1410-X01

Put your description here, lessons learned here, and any other information someone using your
program would need to know to make it run.

Download sequentially (no concurrency)
"""

import requests
import time
import os


def download_img(flag):
    url = f"https://www.sciencekids.co.nz/images/pictures/flags96/{flag}.jpg"
    img = requests.get(url).content
    with open(f"G_seq/{flag}.jpg", "wb") as img_f:
        img_f.write(img)
    return len(img)


def main():
    """
    Program starts here.
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
