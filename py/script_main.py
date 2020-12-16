import os
from cv2 import cv2
from PIL import Image, ImageChops
from skimage.metrics import structural_similarity as ssim

# from skimage.measure import compare_ssim


def getSIIM(index, imageA, imageB):
    # resize if not same shape
    if (imageA.shape != imageB.shape):
        heightA, widthA = imageA.shape
        heightB, widthB = imageA.shape
        imageA = cv2.resize(imageA, (min(heightA, heightB), min(widthA, widthB)))
        imageB = cv2.resize(imageB, (min(heightA, heightB), min(widthA, widthB)))

    # cover with gray color
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    # compare similarity of images
    (score, diff) = ssim(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    diff_percentage = 100 - score * 100


    # print out the result in percentage
    print('\n--------------------------------------------------------------------------------------------------------------------')
    print ("[Pair ID: {}] Difference (percentage): {}%".format(index, diff_percentage))
    print('--------------------------------------------------------------------------------------------------------------------\n')

    # # show image in 2D matrix
    # print (diff,  "\n")

    # # show SSIM
    # print("SSIM: {}".format(score))


def getAllImages(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
               images.append(img)
    return images


# -------------------------------------------- Main ----------------------------------------------------- #

# dirr1 = "../Desktop/3d_kartinki/"
# dirr2 = "../Desktop/3d_kartinkiEdited/"


dirr3 = "./1st_folder/"
dirr4 = "./2nd_folder/"


imgs1 = getAllImages(dirr3)
imgs2 = getAllImages(dirr4)

assert len(imgs1) == len(imgs2), "Two set sizes are not equal."

for i in range(len(imgs1)):
    getSIIM(i, imgs1[i], imgs2[i])
