"""
Manipulating images – resizing and thumbnails
Page 94
"""

from PIL import Image
import glob
import os

for filename in glob.glob("*.jpg"):
    name, ext = os.path.splitext(filename)
    if name .endswith("_thumb"):
        continue
    img = Image.open( filename )
    thumb = img.copy()
    w, h = img.size
    largest = max(w, h)
    w_n, h_n = w*128//largest, h*128//largest
    print(f"Resize {filename} from {w},{h} to {w_n},{h_n}")
    thumb.thumbnail( (w_n, h_n), Image.ANTIALIAS )
    thumb.save(f"{name}_thumb.{ext}")
