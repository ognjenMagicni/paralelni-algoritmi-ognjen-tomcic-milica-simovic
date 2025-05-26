import matplotlib.pyplot as plt
from skimage import io
import numpy as np
from skimage import exposure
import time
from multiprocessing import Pool, cpu_count
from skimage.color import rgb2gray
from functions import import_color_picture, histogram, kulumulativni_hist, apply_T,find_T, show_result, show_time, show_pictures

print(f"Broj jezgara: {cpu_count()}")

def serilization(img):
    print("Serilizaciona implementacija")
    T, t_1 = find_T(img)
    new_img, t_2 = apply_T(img, T)
    show_time(t_1,t_2)
    return new_img
