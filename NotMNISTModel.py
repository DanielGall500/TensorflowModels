import matplotlib.pyplot as plt
import numpy as np
import os 
import sys

train_folders = '/Users/dannyg/Desktop/notMNIST_large'
test_folders = '/Users/dannyg/Desktop/notMNIST_small'

img_size = 28 # 28 x 28
pixel_depth= 255.0 # number of levels per pixel

def load_letter(folder, min_num_images):
	img_files = os.listdir(folder)

	dataset = np.ndarray(shape=(len(img_files), img_size, img_size), dtype=np.float32)

	for img_indx, image in enumerate(img_files):
		img_file = os.path.join(folder, image)

		try:
			img_data = (ndimage.imread(img_file).astype(float) - pixel_depth / 2) / pixel_depth

			if img_data.shape != (img_size, img_size):
				print 'Unexpected Image Size'

			dataset[img_indx, :, :] = img_data

		except IOError as e:
			print 'Could not read: ', image_file

		num_images = img_indx + 1

		dataset = dataset[0:num_images, num_images, num_images]

		if num_images < min_num_images:
			print 'Many less images then expected'

		return dataset

