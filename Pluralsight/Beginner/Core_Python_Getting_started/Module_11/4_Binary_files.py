# Binary Files.
#
# 
import generating_pixel_data
pixels = generating_pixel_data.mandelbrot(448, 256)
import reprlib
print(reprlib.repr(pixels))

import bmpwriter as bmp
bmp.write_grayscale("mandel.bmp", pixels)
##########################################

