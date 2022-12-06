from skimage import util
import os
import cv2



input_path = ""

output_path = ""
cmd = 'mkdir -p ' + output_path
os.system(cmd)


print("Starting add noise...")
i = 0
for elem in os.listdir(input_path):
    i += 1
    if i % 1000:
        print("Processed " + i "...")
    img = cv2.imread(f'{input_path}/{elem}')
    out2 = util.random_noise(img, "s&p")
    out2 = out2 * 255
    out2 = out2.astype(np.int16)
    cv2.imwrite(output_path, img)


