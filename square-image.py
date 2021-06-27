import cv2
import os
import numpy as np
import glob
import pandas as pd
import requests
from PIL import Image

def read_img_url(url):
    pil_img = Image.open(requests.get(url, stream=True).raw)
    cv_img = np.array(pil_img) 
    return cv_img

def pad_image(image):
    if image.shape[0] == image.shape[1]:
        return image

    is_width_longer = image.shape[1] > image.shape[0]
    print(f"Width longer: {is_width_longer}")

    longest_side = max(image.shape[0], image.shape[1])
    shortest_side = min(image.shape[0], image.shape[1])
    padded_image = np.zeros((longest_side, longest_side, 4), dtype=np.uint8)
    print(padded_image.shape)

    if image.shape[2] == 3:
        image = np.concatenate((image, np.full((image.shape[0], image.shape[1], 1), 255, dtype=np.uint8)), axis=2)

    if is_width_longer == True:
        # center vertically
        start_index = (longest_side - shortest_side) // 2
        padded_image[start_index:start_index+shortest_side, :, :] = image
    else:
        # center horizontally
        start_index = (longest_side - shortest_side) // 2
        padded_image[:, start_index:start_index+shortest_side, :] = image
    
    return padded_image

if __name__ == "__main__":
    OUTPUT_DIR = "/home/karlis/Desktop/shopify_product_images"
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    shopify_df = pd.read_csv("/home/karlis/Desktop/products_export_1.csv")
    product_dict = dict()

    for img in glob.glob("/home/karlis/Downloads/product_images/*"):
        
        output_fn = os.path.splitext(img)[0] + ".png"
        print(output_fn)

        # read image from local
        img = cv2.imread(img, cv2.IMREAD_UNCHANGED)
        # pad the image with transparent px
        img = pad_image(img)
        cv2.imwrite(output_fn, img)


    # for i, row in shopify_df.iterrows():
    #     handle = row["Handle"]
    #     if handle in product_dict:
    #         product_dict[handle] += 1
    #     else:
    #         product_dict[handle] = 1
    #     output_name = f"{handle}-{product_dict[handle]}.png"

    #     output_fn = os.path.join(OUTPUT_DIR, output_name)
    #     file_url = row["Image Src"]
    #     if file_url is None:
    #         continue
    #     # read image from shopify cdn
    #     try:
    #         img = read_img_url(file_url)
    #     except Exception:
    #         continue
    #     # convert to bgr
    #     img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    #     # pad the image with transparent px
    #     img = pad_image(img)
    #     cv2.imwrite(output_fn, img)