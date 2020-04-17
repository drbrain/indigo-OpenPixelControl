#!/usr/bin/env python3

from time import sleep
from colorsys import hsv_to_rgb
import json
import opc
import sys

rainbow_offset = 0

def rainbow(pixel_count, s, v):
    global rainbow_offset
    pixels = [None] * pixel_count
    h = rainbow_offset

    for i in range(pixel_count):
        hue = ((h * 0.5 - i * 1.0) % 100) / 100
        h += 1

        r, g, b = hsv_to_rgb(hue, s, v)
        pixels[i] = (r * 255, g * 255, b * 255)

    return pixels

config = json.load(sys.stdin)

address   = config["device"]
channel   = config.get("channel", 0)
led_count = config["LEDs"]

client = opc.Client(address)

while True:
    pixels = rainbow(led_count, 0.5, 0.5)
    rainbow_offset += 1

    if client.put_pixels(pixels, channel = channel):
        sleep(1 / 30.0)
    else:
        exit(1)

