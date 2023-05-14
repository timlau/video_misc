Scripts to create presets for the **Crop: Rectangle** filter in the [Shotcut](http://shotcut.org) video editor.

Presets need to be copied to the Shotcut App Data Directory (Settings -> App Data Directory -> Show)

![](data/../../data/ex1.png)


## Requirements

Python 3.11 on Linux, Windows or Mac

# create_grid_preset.py
Create crop presets for a Row x Column Grid, with padding between each cell.

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

![](data/../../data/Testing%20Grid.gif)

# create_slidein_preset.py
Create crop presets for a animated grid cell growing from the 4 corners

## Howto use

```
usage: pyhton create_slide_presets.py [-h] [--width WIDTH] [--height HEIGHT]
                                      [--xpad XPAD] [--ypad YPAD] [--update] [-o OUTPUT]
                                      [--fps FPS] [--size SIZE]
                                      columns rows

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
  --fps FPS             Frames per second
  --size SIZE           Size in grid elements
```
## Examples


```
python create_slidein_presets.py 3 3 --size 2 
```
Create presets for a 2x2 cell from a 3x3 Grip (FHD: 1920x1080, 30 FPS) in local directory

```
python create_slidein_presets.py 3 3 --size 2 --height 2160 --width 3840 -fps 24 o <Path to Shotcut App Data Dir>
```
Create presets for a 2x2 cell from a 3x3 Grip (UHD: 3840x2160, 24 FPS) in the Shotcut App Data directory

