from pathlib import Path
import cv2
import numpy as np

# choose codec according to format needed
frames = sorted(list(Path("./frames").glob("*.jpg")))
width, height = 1000, 800
fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
video = cv2.VideoWriter('video.avi', fourcc, 2, (width, height))

for path in frames:
    print(path)
    img = cv2.imread(str(path))
    video.write(img)

cv2.destroyAllWindows()
video.release()