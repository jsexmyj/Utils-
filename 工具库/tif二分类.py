import rasterio
import numpy as np
import matplotlib.pyplot as plt
import os

def process_tif_to_bw(input_folder, output_folder, threshold=128):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".tif"):
            input_tif = os.path.join(input_folder, filename)
            output_tif = os.path.join(output_folder, filename)
            
            with rasterio.open(input_tif) as src:
                band = src.read(1)  # 读取单波段
                
                # 归一化到0-255
                band = (band - band.min()) / (band.max() - band.min()) * 255
                band = band.astype(np.uint8)
                
                # 二值化处理
                binary_band = np.where(band > threshold, 255, 0).astype(np.uint8)
                
                # 保存新的二值图像
                profile = src.profile
                profile.update(dtype=rasterio.uint8, count=1)
                
                with rasterio.open(output_tif, 'w', **profile) as dst:
                    dst.write(binary_band, 1)
                
                # 显示处理后的图像
                # plt.imshow(binary_band, cmap='gray')
                # plt.axis('off')
                # plt.show()

# 示例用法
process_tif_to_bw("france\mask", "france\\new_mask")
