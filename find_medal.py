#!/usr/bin/env python 
import cv2
import numpy as np
import os
import sys
import sys
sys.path.append("/usr/local/lib/MedalDetector")
import glob
import argparse
import classes.medal as medal
import multiprocessing
from multiprocessing import Queue, Pool
from matplotlib import pyplot as plt

debug_output_dir = '/tmp/matches'

methods = ['cv2.TM_CCOEFF_NORMED']
parser = argparse.ArgumentParser(description='Finds Halo medals in video frames.')
parser.add_argument("-i","--input", default='./', help="Input directory.")
parser.add_argument("-d","--debug", default=False,action='store_true', help="Write out matching frames and provide some messages?")
args = parser.parse_args()
path = args.input
in_debug = args.debug

def detect(medals, image, results):
  fname = os.path.basename(image)

  tag_output = []
  if in_debug:
    sys.stderr.write("Processing " + fname + "\n")

  img_rgb = cv2.imread(image)
  img2 = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

  for a_medal in medals:
    template = a_medal.template
    path = a_medal.medal_path
    medal = a_medal.medal_title
    game = a_medal.game
    medal_name = a_medal.name
    fname_no_extension = os.path.splitext(fname)[0][0:] #get the filename extension
    w = a_medal.width
    h = a_medal.height

    #if in_debug:
    #  sys.stderr.write(" - Looking for " + medal + "\n")

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

      if matches > 0:
        #if not game in tag_output:
        #  tag_output.append(game)

        if not medal_name in tag_output:
          tag_output.append(medal_name)
        if in_debug:
          if not os.path.exists(debug_output_dir):
            os.makedirs(debug_output_dir)
          cv2.rectangle(img_rgb_output, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
          cv2.imwrite(debug_output_dir + os.sep  + fname_no_extension + '-' + medal_name + '.png', img_rgb_output)
  if len(tag_output) > 0:
    results.put(tag_output)


#preload the medals
medals = []

for template_file in glob.glob('/usr/local/lib/MedalDetector/medals/*/*.*'):
  template = cv2.imread(template_file,0)
  medal_path, medal_title = os.path.split(template_file)
  medal_path = medal_path.split(os.sep)
  game = medal_path[1]
  medal_name = os.path.splitext(os.path.basename(template_file))[0]
  w, h = template.shape[::-1]
  medals.append(medal.Medal(medal_name,template,medal_path,medal_title,game,w,h))

results = Queue()

# builds a list of jobs
process_pool = Pool()
mp_manager = multiprocessing.Manager()
results = mp_manager.Queue()
for infile in glob.glob( os.path.join(path, '*.png') ):
  process_pool.apply_async(detect, args=(medals, infile, results,))
  #detect(medals, infile, results)


process_pool.close()
process_pool.join()
  
resultdict = []
while not results.empty():
  item = results.get()
  for i in item:
    if i not in resultdict:
      resultdict.append(i)

loop = 0
for tag in resultdict:
  if loop > 0:
    sys.stdout.write(', ')
  sys.stdout.write(tag)
  loop = loop + 1
