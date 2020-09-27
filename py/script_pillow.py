import os
from PIL import Image, ImageChops
from cv2 import cv2

img1 = Image.open('./imgs/original_02.png')
img2 = Image.open('./imgs/modified_02.png')

# img3 = Image.open('./first_folder/test1.jpg')
# img4 = Image.open('./second_folder/test1.jpg')


# img1.show()
# img2.show()

def getAllImages(folder):
    images = []
    for filename in os.listdir(folder):
        img = Image.open(folder + '/' + filename)
        if img is not None:
               images.append(img)
    return images

imgs1 = getAllImages('./1st_folder')
imgs2 = getAllImages('./2nd_folder')

diff_path = './diff_folder/'

assert len(imgs1) == len(imgs2), "Two set sizes are not equal."

# write images to diff_folder
for i in range(len(imgs1)):
    img = ImageChops.difference(imgs1[i], imgs2[i])
    img.save('{}diff_img_{}.jpg'.format(diff_path ,i))

# open diff_folder
os.startfile(os.path.realpath(diff_path))



# diff = ImageChops.difference(img1, img2)

# if diff.getbbox():
#     diff.show()

# -------------------------------------------- Difference ----------------------------------------------------- #


# assert img1.mode == img2.mode, "Different kinds of images."
# assert img1.size == img2.size, "Different sizes."

# pairs = zip(img1.getdata(), img2.getdata())
# if len(img1.getbands()) == 1:
#     # for gray-scale jpegs
#     dif = sum(abs(p1-p2) for p1,p2 in pairs)
# else:
#     dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
 
# ncomponents = img1.size[0] * img1.size[1] * 3
# print ("Difference (percentage):", (dif / 255.0 * 100) / ncomponents) 



