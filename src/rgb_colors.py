#!/usr/bin/env python
# -*- coding: utf-8 -*-
#=======================================================================
# bgb_colors.py
# -------------
# Generate 2D-images with one pixel for each color in the color cube.
#
#
# Author: Joachim Strömbergson
# (c) 2014, Secworks Sweden AB
#
#=======================================================================

#-------------------------------------------------------------------
# Python module imports.
#-------------------------------------------------------------------
import sys
import math
import random
from PIL import Image, ImageDraw


#-------------------------------------------------------------------
# Symbolic values and flags.
#-------------------------------------------------------------------
VERBOSE = False


#-------------------------------------------------------------------
# main()
#
# Test the bitcounter.
#-------------------------------------------------------------------
def main():
    color_depth = 7
    num_hues = 2**color_depth
    num_pixels = 2**(color_depth * 3)
    print("Number of pixels: %d" % num_pixels)
    dimension = int(math.sqrt(num_pixels))
    print("Image dimension: %dx%d" % (dimension, dimension))
    print("Generating...")

    im = Image.new('RGB', (dimension, dimension), (0, 0, 0))
    draw = ImageDraw.Draw(im)
    
    # Select start point at centre
#    x = dimension / 2
#    y = dimension / 2
    
    x = 0
    y = 0
    
    r = 0
    g = 0
    b = 0
    
#    r = random.randint(0, num_hues)
#    g = random.randint(0, num_hues)
#    b = random.randint(0, num_hues)    

    for i in range(num_pixels):
        draw.point((x ,y), fill=(r, g, b))

        x += 1
        if x == dimension:
            x = 0
            y += 1
            
        r += 1
        if r == num_hues:
            r = 0
            g += 1
            if g == num_hues:
                g = 0
                b += 1
        if VERBOSE:
            print("x = %d, y = %d, r = %d, g = %d, b = %d" % (x, y, r, g, b))
    
    print("Done.")
    im.show()

#-------------------------------------------------------------------
# __name__
# Python thingy which allows the file to be run standalone as
# well as parsed from within a Python interpreter.
#-------------------------------------------------------------------
if __name__=="__main__": 
    # Run the main function.
    sys.exit(main())

#=======================================================================
# EOF bitcount.py
#=======================================================================
