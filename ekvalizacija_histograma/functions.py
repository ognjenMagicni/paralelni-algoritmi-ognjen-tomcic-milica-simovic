import matplotlib.pyplot as plt
from skimage import io
import numpy as np
from skimage import exposure
import time
from multiprocessing import Pool, cpu_count
from skimage.color import rgb2gray

def import_color_picture(path):
    img_c = io.imread(path)
    gray = rgb2gray(img_c)
    img = (gray * 255).astype('uint8')
    return img

def histogram(img):
    numpy_hist, nbin_edges = np.histogram(img, bins = np.arange(257))
    return numpy_hist

def kulumulativni_hist(hist):
    return np.cumsum(hist)

def find_T(img):
    t_1 = time.time()
    hist = np.histogram(img, bins = np.arange(257), density=True)[0]
    T = 255 * np.cumsum(hist)
    T = np.round(T).astype('uint8')
    t_2 = time.time()
    return T, t_2-t_1

def apply_T(img, T):
    t_1 = time.time()
    new_img = T[img]
    t_2 = time.time()
    return new_img, t_2-t_1

def find_apply_T(img):
    T,t_1 = find_T(img)
    t_2 = time.time()
    new_img = T[img]
    t_3 = time.time()
    return new_img, t_1,t_3-t_2

def show_result(img1,hist1,cul1,img2,hist2,cul2):
    plt.subplot(2,3,1)
    plt.imshow(img1,cmap='gray')
    plt.subplot(2,3,2)
    plt.plot(np.arange(256),hist1)
    plt.subplot(2,3,3)
    plt.plot(np.arange(256),cul1)
    plt.subplot(2,3,4)
    plt.imshow(img2,cmap='gray')
    plt.subplot(2,3,5)
    plt.plot(np.arange(256),hist2)
    plt.subplot(2,3,6)
    plt.plot(np.arange(256),cul2)
    plt.show()

def show_time(t_1,t_2):
    print(f"Vrijeme da se konstruise T: {t_1}")
    print(f"Vrijeme da se konvertuje slika: {t_2}")
    print(f"Ukupno {t_1+t_2}")

def show_pictures(img, img1, img2, img3):
    plt.subplot(2,2,1)
    plt.title("Original")
    plt.imshow(img,cmap='gray')
    plt.subplot(2,2,2)
    plt.title("Serilizacija")
    plt.imshow(img1,cmap='gray')
    plt.subplot(2,2,3)
    plt.title("Paralelizacija I")
    plt.imshow(img2,cmap='gray')
    plt.subplot(2,2,4)
    plt.title("Paralelizacija II")
    plt.imshow(img3,cmap='gray')
    plt.show()