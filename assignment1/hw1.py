#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np


def histogram_times(filename):
    import re
    with open(filename) as f:
        csv_reader = csv.reader(f)
        plane_data = list(csv_reader)

    crash_times = [0] * 24
    for crash in plane_data[1:]:
        if crash[1]:
            hour = int(re.sub('[^0-9]', "", crash[1])[-4:-2])
            crash_times[hour] += 1

    return crash_times


def weigh_pokemons(filename, weight):
    with open(filename) as f:
        poke_reader = json.load(f)

    pokemon_arr = []
    for pokemon in poke_reader['pokemon']:
        if float(pokemon['weight'][:-2]) == weight:
            pokemon_arr.append(pokemon['name'])

    return pokemon_arr


def single_type_candy_count(filename):
    with open(filename) as f:
        poke_reader = json.load(f)

    candy_count = 0
    for pokemon in poke_reader['pokemon']:
        if 'candy_count' in pokemon and len(pokemon['type']) == 1:
            candy_count += pokemon['candy_count']

    return candy_count


def reflections_and_projections(points):
    #points is a 2 by n matrix
    point_arr = points
    #reflect point over line y = n
    n = 1
    point_arr[1] = 2 * n - point_arr[1]
    #rotate the point rotateRad radians around origin CCW
    #rotateRad = np.pi / 2
    #rotateMat = np.array([[np.cos(rotateRad), -np.sin(rotateRad)],[np.sin(rotateRad), np.cos(rotateRad)]])
    rotate_mat = np.array([[0, -1], [1, 0]])
    point_arr = rotate_mat.dot(point_arr)
    #project point onto line y = 3x
    m = 3
    point_arr = np.array([[1, m], [m, m ** 2]]).dot(point_arr) / (1 + m ** 2)

    return point_arr


def normalize(image):
    norm_image = image
    pixel_max = norm_image.max()
    pixel_min = norm_image.min()
    if pixel_min == pixel_max:
        return norm_image

    norm_image = 255 * (norm_image - pixel_min) / (pixel_max - pixel_min)
    return norm_image


def sigmoid_normalize(image):
    norm_image = image
    pixel_max = norm_image.max()
    pixel_min = norm_image.min()
    if pixel_min == pixel_max:
        return norm_image

    norm_image = 255.0 / (1 + np.e ** ((norm_image - 128) / (pixel_min - pixel_max)))
    return norm_image
