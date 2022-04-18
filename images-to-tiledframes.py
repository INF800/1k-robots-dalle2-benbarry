from pathlib import Path
import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image

images = sorted(list(Path("./images").glob("*.png")))[7:]

idxs = np.arange(1000)
idxs = np.reshape(idxs, (50, 20))
for fnum, fids in enumerate(idxs):
    fig, axs = plt.subplots(4, 5, figsize=(10,8))
    axs = axs.flatten()
    for i, idx in enumerate(fids):
        idx = idx%len(images)
        im = Image.open(str(images[idx]))
        # im = im.resize((100,100))
        axs[i].imshow(im)
        axs[i].axis("off")

    plt.subplots_adjust(wspace=0, hspace=0)
    plt.savefig(f"frames/frame_{str(fnum).zfill(3)}.jpg")
    # plt.show()
    


