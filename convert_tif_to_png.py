# convert an image to png
import cv2
original_image_path = '/home/alexgo/code/ZSSR/test_data/air.tif'
output_png_path = '/home/alexgo/code/ZSSR/test_data/air.png'

im = cv2.imread(original_image_path)

cv2.imwrite(output_png_path, im)