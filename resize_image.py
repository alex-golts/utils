# resize image
import cv2
original_image_path = '/home/alexgo/code/ZSSR/test_data/air_small.png'
output_path = '/home/alexgo/code/ZSSR/test_data/air_small_x2.png'

im = cv2.imread(original_image_path)
im = cv2.resize(im,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
cv2.imwrite(output_path, im)
