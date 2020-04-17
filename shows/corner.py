#!/usr/bin/env python3

from time import sleep
import json
import opc
import sys

def curve(pixels, middle, width):
    start = int(middle - width / 2)

    for i in range(0, width):
        value = point(i, width)

        try:
            pixels[i + start] = (value * 127, 0, 0)
        except IndexError:
            return

def point(offset, total):
    step = 2.0 / total

    if offset <= total / 2:
        point = step * offset

        return ((point * 4) - 5) ** -2
    else:
        point = step * offset - 1 - step

        return ((point * 4) + 1) ** -2

config = json.load(sys.stdin)

address   = config["device"]
channel   = config.get("channel", 0)
led_count = config["LEDs"]

client = opc.Client(address)

if not client.can_connect():
    sys.exit(1)

pixels = [(0, 0, 0)] * led_count

curve(pixels, 119, 30)
curve(pixels, 230, 30)

while True:
    client.put_pixels(pixels, channel = channel)

    sleep(1)

