import rasterio
import numpy as np
from rasterio.plot import reshape_as_image
from PIL import Image
import os

# file_path = r"D:\Desktop\dataset\\france\\image\\g212_00079_11.tif"
# 输入和输出文件夹
input_folder = r"D:\Desktop\dataset\\france\\test\\image"  # TIFF 影像所在文件夹
output_folder = r"D:\Desktop\dataset\\france\\test\\image_rgb"  # 处理后保存的文件夹
# 确保输出文件夹存在
os.makedirs(output_folder, exist_ok=True)
for filename in os.listdir(input_folder):
    if filename.endswith(".tif"):  # 只处理 TIFF 文件
        file_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        try:
            # 打开 TIFF 影像
            with rasterio.open(file_path) as dataset:
                # 获取影像波段数
                num_bands = dataset.count

                # 读取 R/G/B 波段（如果至少有 3 个波段）
                if num_bands >= 3:
                    r = dataset.read(1)  # 第一波段
                    g = dataset.read(2)  # 第二波段
                    b = dataset.read(3)  # 第三波段
                
                # 归一化到 8-bit
                rgb = np.stack([r, g, b], axis=-1)
                rgb_8bit = (rgb / rgb.max() * 255).astype(np.uint8)

                # 转换为 PIL 图像
                img = Image.fromarray(rgb_8bit)
                img.save(output_path)  


        except Exception as e:
            print(f"❌ 处理失败: {filename}, 错误信息: {e}")

print(f"✅ 处理完成")
