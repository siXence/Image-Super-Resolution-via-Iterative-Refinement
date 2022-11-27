from PIL import Image
import os
in_paths = ["/Users/wangxu21/project/deblurring/Image-Super-Resolution-via-Iterative-Refinement/dataset/cifar-10-batches-py/train", "/Users/wangxu21/project/deblurring/Image-Super-Resolution-via-Iterative-Refinement/dataset/cifar-10-batches-py/eval"]
out_paths = ["/Users/wangxu21/project/deblurring/Image-Super-Resolution-via-Iterative-Refinement/dataset/cifar-10-batches-py/train_gray", "/Users/wangxu21/project/deblurring/Image-Super-Resolution-via-Iterative-Refinement/dataset/cifar-10-batches-py/eval_gray"]
for in_path, out_path in zip(in_paths, out_paths):
    file_list = os.listdir(in_path)
    # 循环
    print(in_path , " start converting...")
    for image in file_list:
        I = Image.open(in_path + "/" + image)
        gray = I.convert('L')
        gray.save(out_path + "/" + image)
        #print(file)
    print(in_path , " done!!")

