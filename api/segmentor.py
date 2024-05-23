import os
import cv2
import numpy as np

# import matplotlib.pyplot as plt
root = os.getcwd()
OUTPUT_DIR = os.path.join(root, "segmented")


def line_array(x):
    upper, lower = [], []
    for y in range(5, len(x) - 5):
        s_a, s_p = strtline(y, x)
        e_a, e_p = endline(y, x)
        if s_a >= 7 and s_p >= 5:
            upper.append(y)
        if e_a >= 5 and e_p >= 7:
            lower.append(y)
    return upper, lower


def strtline(y, array):
    prev, ahead = 0, 0
    for i in array[y : y + 10]:
        if i > 3:
            ahead += 1
    for i in array[y - 10 : y]:
        if i == 0:
            prev += 1
    return ahead, prev


def endline(y, array):
    ahead = 0
    prev = 0
    for i in array[y : y + 10]:
        if i == 0:
            ahead += 1
    for i in array[y - 10 : y]:
        if i > 3:
            prev += 1
    return ahead, prev


def endline_word(y, array, a):
    ahead = 0
    prev = 0
    for i in array[y : y + 2 * a]:
        if i < 2:
            ahead += 1
    for i in array[y - a : y]:
        if i > 2:
            prev += 1
    return prev, ahead


def end_line_array(array, a):
    list_endlines = []
    for y in range(len(array)):
        e_p, e_a = endline_word(y, array, a)
        # print(e_p, e_a)
        if e_a >= int(1.5 * a) and e_p >= int(0.7 * a):
            list_endlines.append(y)
    return list_endlines
