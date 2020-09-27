from cv2 import cv2
from skimage.measure import compare_ssim


img1 = './imgs/modified_02.png'
img2 = './imgs/original_02.png'

imageA = cv2.imread(img1)
imageB = cv2.imread(img2)


# resize if not same shape
if (imageA.shape != imageB.shape):
    heightA, widthA, channelsA = imageA.shape
    heightB, widthB, channelsB = imageA.shape
    imageA = cv2.resize(imageA, (min(heightA, heightB), min(widthA, widthB)))
    imageB = cv2.resize(imageB, (min(heightA, heightB), min(widthA, widthB)))

# cover with gray color
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

# compare similarity of images
(score, diff) = compare_ssim(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")
diff_percentage = 100 - score * 100

# print out the result in percentage
print('\n--------------------------------------------------------------------------------------------------------------------')
print ("Difference (percentage):", diff_percentage, img1, img2)
print('--------------------------------------------------------------------------------------------------------------------\n')

# show image in 2D matrix
print (diff,  "\n")

# show SSIM
print("SSIM: {}".format(score))