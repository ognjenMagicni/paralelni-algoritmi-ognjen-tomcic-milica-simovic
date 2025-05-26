import matplotlib.pyplot as plt
from skimage import io
import numpy as np
from skimage import exposure
import time
from multiprocessing import Pool, cpu_count
from skimage.color import rgb2gray
from functions import find_T, apply_T, show_time, import_color_picture, find_apply_T, show_pictures


def parallel_equalization_I(img):
    print("Paralelna implementacija, gdje se kulmulativni histogram računa serilizaciono")

    num_cores = cpu_count()
    img_split = np.array_split(img, num_cores, axis=0)
    T,t_1 = find_T(img)
    with Pool(processes=num_cores) as pool:
        r = pool.starmap(apply_T, [(chunk, T) for chunk in img_split])
    show_time(t_1,r[0][1])

    return np.vstack([res[0] for res in r])
    

def parallel_equalization_II(img):
    print("Paralelna implementacija, gdje se kulmulativni histogram računa paralelno")
    
    num_cores = cpu_count()
    img_split = np.array_split(img, num_cores, axis=0)

    with Pool(processes=num_cores) as pool:
        r = pool.starmap(find_apply_T, [(chunk, ) for chunk in img_split])
    show_time(r[0][1],r[0][2])

    return np.vstack([results[0] for results in r])
    