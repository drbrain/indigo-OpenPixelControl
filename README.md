## Writing your own light shows

The `shows/` directory contains example executables that will display a light
show on an Open Pixel Control device.

The executable must read a JSON configuration set from `stdin` which will
describe the configuration of the Open Pixel Control device.

Example:

```json
{
  "device": "localhost:7890",
  "channel": 0,
  "LEDs": 128
}
```

The `device` field is required.  It is the host and port to connect to.

The `channel` field is optional.  It is the Open Pixel Control channel to
control.

The `leds` field is optional.  It is the number of LEDs connected.

After loading the JSON configuration the program should connect to the `device`
and issue commands for a light show.
