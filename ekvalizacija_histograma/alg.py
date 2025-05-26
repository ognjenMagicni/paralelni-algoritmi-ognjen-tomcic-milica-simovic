from alg_par import parallel_equalization_I, parallel_equalization_II
from alg_ser import serilization
from functions import import_color_picture,show_pictures

img = import_color_picture("low.png")
img1 = serilization(img)
img2 = parallel_equalization_I(img)
img3 = parallel_equalization_II(img)

show_pictures(img,img1,img2,img3)