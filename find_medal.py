#!/usr/bin/env python
import cv2
import numpy as np
import os
import sys
import glob
import argparse
from matplotlib import pyplot as plt


# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF_NORMED']
parser = argparse.ArgumentParser(description='Demonstrate mouse interaction with images')
parser.add_argument("-i","--input", default='./', help="Input directory.")
args = parser.parse_args()
path = args.input

tag_output = []
for infile in glob.glob( os.path.join(path, '*.png') ):
  ext = os.path.splitext(infile)[1][1:] #get the filename extenstion
  fname = os.path.basename(infile)

  img_rgb = cv2.imread(infile)
  img2 = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
  for template_file in glob.glob('medals/*/*.*'):
    template = cv2.imread(template_file,0)
    path, medal = os.path.split(template_file)
    path = path.split(os.sep)
    game = path[1]
    medal_name = os.path.splitext(os.path.basename(template_file))[0]
    w, h = template.shape[::-1]

    for meth in methods:
        img = img2.copy()
        method = eval(meth)

        # Apply template Matching
        res = cv2.matchTemplate(img,template,method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        img_rgb_output = img_rgb.copy()

        threshold = 0.9
        loc = np.where( res >= threshold)
        matches = 0
        for pt in zip(*loc[::-1]):
            matches = matches + 1
            cv2.rectangle(img_rgb_output, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

        if matches > 0:
            if not game in tag_output:
              tag_output.append(game)

            if not medal_name in tag_output:
              tag_output.append(medal_name)

            cv2.imwrite('matches/' + fname + '-' + medal + '.png', img_rgb_output)


loop = 0
for tag in tag_output:
  if loop > 0:
    sys.stdout.write(', ')
  sys.stdout.write(tag)
  loop = loop + 1
