"""
Project Name: Concurrent Programming Project
Author: Zhihui Chen
Due Date: 06/23/2022
Course: CS1410-X01

This program download imgs concurrently using futures with threads
"""

import requests
import time
import os
from concurrent.futures import ThreadPoolExecutor


def download_img(flag):
    """
    flag: str, name of country flag
    download img
    return int, img size
    """
    url = f"https://www.sciencekids.co.nz/images/pictures/flags96/{flag}.jpg"
    img = requests.get(url).content
    with open(f"G_thread/{flag}.jpg", "wb") as img_f:
        img_f.write(img)
    return len(img)


def main():
    """
    if G_thread folder does not exist, create it

    read flags.txt file,
    Use ThreadPoolExecutor to download imgs at the same time
        instead of waiting for one img to finish downloading
    save total download img size

    write result to G_thread_result.txt
    """
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
