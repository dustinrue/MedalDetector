MedalDetector
=============

MedalDetector detects medals earned in Halo: The Master Chief Collection Xbox 
GameDVR clips. Combined with GameDVR2Local, MedalDetector allows you to assign
Finder tags to downloaded videos based on what medals were earned in the clip

Requirements
------------

MedalDetector is currently meant for OS X and:

* Python 2.7
* Via Brew
  * ffmpeg
  * tag
  * opencv
  * imagemagick
* Some symlinks
  * cd /Library/Python/2.7/site-packages/
  * sudo ln -s /usr/local/Cellar/opencv/2.4.9/lib/python2.7/site-packages/cv.py cv.py
  * sudo ln -s /usr/local/Cellar/opencv/2.4.9/lib/python2.7/site-packages/cv2.so cv2.so
* /usr/local/bin must be in your PATH

How to use
----------

* For single file, use tag_video.sh `<path to video>`
* For a directory or file containing a list of files (with full path) use tag_videos.sh
* To manually process a video so you can do what you wish with the output run:
  * split_video.sh `<path to video> <path to outputdir>`
  * find_medal.py -i `<path to outputdir>`

Hints from <http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html> and <https://jjyap.wordpress.com/2014/05/24/installing-opencv-2-4-9-on-mac-osx-with-python-support/>

