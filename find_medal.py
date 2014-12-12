#!/usr/bin/env python -u
import cv2
import numpy as np
import os
import sys
import glob
import argparse
from matplotlib import pyplot as plt

debug_output_dir = '/tmp/matches'

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF_NORMED']
parser = argparse.ArgumentParser(description='Finds Halo medals in video frames.')
parser.add_argument("-i","--input", default='./', help="Input directory.")
parser.add_argument("-d","--debug", default=False,action='store_true', help="Write out matching frames and provide some messages?")
args = parser.parse_args()
path = args.input
in_debug = args.debug

tag_output = []
for infile in glob.glob( os.path.join(path, '*.png') ):
  fname = os.path.basename(infile)

  if in_debug:
    sys.stderr.write("Processing " + fname + "\n")

  img_rgb = cv2.imread(infile)
  img2 = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
  for template_file in glob.glob('/usr/local/lib/MedalDetector/medals/*/*.*'):
    template = cv2.imread(template_file,0)
    path, medal = os.path.split(template_file)
    path = path.split(os.sep)
    game = path[1]
    medal_name = os.path.splitext(os.path.basename(template_file))[0]
    fname_no_extension = os.path.splitext(fname)[0][0:] #get the filename extenstion
    w, h = template.shape[::-1]

    if in_debug:
      sys.stderr.write(" - Looking for " + medal_name + "\n")
      sys.stdout.flush()

    img = img2.copy()
    method = cv2.TM_CCOEFF_NORMED

    # Apply template Matching
    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    img_rgb_output = img_rgb.copy()

    threshold = 0.8
    loc = np.where( res >= threshold)
    matches = 0

    for pt in zip(*loc[::-1]):
      matches = matches + 1
      cv2.rectangle(img_rgb_output, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

      if matches > 0:
        #if not game in tag_output:
        #  tag_output.append(game)

        if not medal_name in tag_output:
          tag_output.append(medal_name)
        if in_debug:
          if not os.path.exists(debug_output_dir):
            os.makedirs(debug_output_dir)
          cv2.imwrite(debug_output_dir + os.sep  + fname_no_extension + '-' + medal_name + '.png', img_rgb_output)


loop = 0
for tag in tag_output:
  if loop > 0:
    sys.stdout.write(', ')
  sys.stdout.write(tag)
  loop = loop + 1
