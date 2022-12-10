from skimage import util
from skimage.color import rgb2gray
import numpy as np
import os
import cv2



input_path = "/Users/wangxu21/project/deblurring/Image-Super-Resolution-via-Iterative-Refinement/dataset/ffhq_64_512/sr_64_512"

output_path = "/Users/wangxu21/project/deblurring/Image-Super-Resolution-via-Iterative-Refinement/dataset/ffhq_64_512/noise_sr_64_512"
cmd = 'mkdir -p ' + output_path
os.system(cmd)


print("Starting add noise...")
i = 0
for elem in os.listdir(input_path):
    i += 1
    if i % 1000:
        print("Processed " + str(i) + "...")
    img = cv2.imread(f'{input_path}/{elem}')
    out2 = util.random_noise(rgb2gray(img), "gaussian")
    out2 = out2 * 255
    out2 = out2.astype(np.int16)
    #cv2.imwrite(f'{output_path}/{elem}', img)
    cv2.imwrite(f'{output_path}/{elem}', out2)


