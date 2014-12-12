You must have OpenCV and ImageMagick installed via brew.

Hints from <http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html> and <https://jjyap.wordpress.com/2014/05/24/installing-opencv-2-4-9-on-mac-osx-with-python-support/>

Required:

* Brew
  * ffmpeg
  * tag
  * opencv
* Some symlinks
  * cd /Library/Python/2.7/site-packages/
  * sudo ln -s /usr/local/Cellar/opencv/2.4.9/lib/python2.7/site-packages/cv.py cv.py
  * sudo ln -s /usr/local/Cellar/opencv/2.4.9/lib/python2.7/site-packages/cv2.so cv2.so
* /usr/local/bin must be in your PATH

How to use:

* For single file, use tag_video.sh
* For a directory or file containing a list of files (with full path) use tag_videos.sh

