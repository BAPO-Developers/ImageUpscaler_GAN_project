from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
from pathlib import Path

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err

def compare_images(imageA, imageB, title):
	# compute the mean squared error and structural similarity
	# index for the images
	m = mse(imageA, imageB)
	s = ssim(imageA, imageB)

	# setup the figure
	fig = plt.figure(title)
	plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))

	# show first image
	ax = fig.add_subplot(1, 2, 1)
	plt.imshow(imageA, cmap = plt.cm.gray)
	plt.axis("off")

	# show the second image
	ax = fig.add_subplot(1, 2, 2)
	plt.imshow(imageB, cmap = plt.cm.gray)
	plt.axis("off")

	# show the images
	plt.show()


originals_path = Path('./AnimationsCompare/Original/')
ibm_path = Path('./AnimationsCompare/IBM/')
srgan_path = Path('./AnimationsCompare/SRGAN/')

for i in [1, 2, 3, 4]:
    orig = cv2.imread(str(originals_path) + str(f'/{i}') + str('.jpg'))
    ibm = cv2.imread(str(ibm_path) + str(f'/{i}') + str('.png'))
    srgan = cv2.imread(str(srgan_path) + str(f'/{i}') + str('.jpg'))

    orig = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
    ibm = cv2.cvtColor(ibm, cv2.COLOR_BGR2GRAY)
    srgan = cv2.cvtColor(srgan, cv2.COLOR_BGR2GRAY)

    print(f'Image {i} -> Original: {orig.shape}, IBM: {ibm.shape}, SRGAN: {srgan.shape}')

    # print(f"Image: {i}\n")
    # print(f"Original vs IBM\n MSE: {mse(orig, ibm)}\n SSIM: {ssim(orig, ibm)}\n")
    # print(f"Original vs SRGAN\n MSE: {mse(orig, srgan)}\n SSIM: {ssim(orig, srgan)}\n")
    # print(f"SRGAN vs IBM\n MSE: {mse(ibm, srgan)}\n SSIM: {ssim(ibm, srgan)}\n")