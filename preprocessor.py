import matplotlib.pyplot as plt
import os

from tqdm import tqdm
from matplotlib import image
import numpy as np

LFW_DIR = "lfw-deepfunneled" # Download and extract from http://vis-www.cs.umass.edu/lfw/lfw-deepfunneled.tgz
SAVE_FILE = "x.npy"

def preprocess_img(img):
    img = np.array(img, dtype=np.float16) # Save memory, colors are only 0-255
    resq = 61
    img = img[resq:-resq, resq:-resq] # Take only the center crop of the image
    img = img/255.0 # Scale pixel values between 0 and 1
    return img

if __name__ == "__main__":
    x = []
    for folder in tqdm(os.listdir(LFW_DIR)):
        path = os.path.join(LFW_DIR, folder)
        for file_name in os.listdir(path):
            if file_name.split(".")[-1] == "jpg":
                img_path = os.path.join(path, file_name)
                img = image.imread(img_path)
                print(img.shape)
                exit()
                img = preprocess_img(img)
                x.append(img)

    x = np.array(x)
    # np.save("x.npy", x)

