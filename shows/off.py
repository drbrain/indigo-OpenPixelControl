#!/usr/bin/env python3

from time import sleep
import json
import opc
import sys

config = json.load(sys.stdin)

address   = config["device"]
channel   = config.get("channel", 0)
led_count = config["LEDs"]

client = opc.Client(address)

if not client.can_connect():
    sys.exit(1)

pixels = [(0, 0, 0)] * led_count

client.put_pixels(pixels, channel = channel)

sleep(1)

