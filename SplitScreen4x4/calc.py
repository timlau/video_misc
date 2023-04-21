# border thickness
border = 1.5

# Video Size
x_width = 1920
y_width = 1080

# Calc border with in pixels for (16:9)
border_x = border * 16
border_y = border * 9

# calc size of each clip
x_size = round((x_width - (border_x)) / 2)
y_size = round((y_width - (border_y)) / 2)

# pixels to shift clip on x axis.
dx = border_x / 4

# Top Left
x_TL = round(dx)
y_TL = round(0)
# Bottom Left
x_BL = round(dx)
y_BL = round(border_y + y_size)
# Top Right
x_TR = round(x_width - x_size - dx)
y_TR = round(0)
# Bottom Right
x_BR = round(x_width - x_size - dx)
y_BR = round(border_y + y_size)


print(f"border factor = {border} : ({border_x} px, {border_y} px)")

print(f"Top Left     : {x_TL} , {y_TL}  ( {x_size} x {y_size} )")
print(f"Top Right     : {x_TR} , {y_TR}  ( {x_size} x {y_size} )")
print(f"Bottom Left  : {x_BL} , {y_BL}  ( {x_size} x {y_size} )")
print(f"Bottom Right  : {x_BR} , {y_BR}  ( {x_size} x {y_size} )")
