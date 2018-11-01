# crop image
import cv2
original_image_path = '/home/alexgo/code/ZSSR/test_data/air.png'
output_path = '/home/alexgo/code/ZSSR/test_data/air_small.png'
row_min=0
row_max=1024
col_min=0
col_max=1024
im = cv2.imread(original_image_path)
im=im[row_min:row_max, col_min:col_max,:]
cv2.imwrite(output_path, im)
