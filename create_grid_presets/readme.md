Tool to create presets for the **Crop: Rectangle** filter in the [Shotcut](http://shotcut.org) video editor.

Presets need to be copied to the Shotcut App Data Directory (Settings -> App Data Directory -> Show)

## Requirements

Python 3.11 on Linux, Windows or Mac

## Howto use

```
usage: pyhton create_grid_presets.py [-h] [--width WIDTH] [--height HEIGHT] [--xpad XPAD] [--ypad YPAD] [--update] [-o OUTPUT] columns rows

Create preset for crop: rectangle filter in Shotcut

positional arguments:
  columns               Number of grid colums
  rows                  Number of grid rows

options:
  -h, --help            show this help message and exit
  --width WIDTH         Frame Width (Default: 1940)
  --height HEIGHT       Frame Height (Default: 1080)
  --xpad XPAD           padding between columns (default: 15px)
  --ypad YPAD           padding between rows
  --update              Update existing presets
  -o OUTPUT, --output OUTPUT
                        output directory (default: current dir)

```
## Examples


```
python create_grid_presets.py 3 3
```
Create presets for a 3x3 Grip (FHD: 1920x1080) in local directory

```
python create_grid_presets.py --height 2160 --width 3840 3 2 -o <Path to Shotcut App Data Dir>
```
Create presets for a 3x2 Grip (UHD: 3840x2160) in the Shotcut App Data directory


