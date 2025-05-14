import os

def delete_tif_files(folder_path, numbers_to_delete):
    """
    删除指定文件夹中以特定数字命名的 .tif 文件。

    :param folder_path: 文件夹路径
    :param numbers_to_delete: 要删除的数字列表
    """
    # 确保文件夹路径存在
    if not os.path.exists(folder_path):
        print(f"文件夹 {folder_path} 不存在！")
        return

    deleted_files = []
    # 遍历文件夹中的文件
    for file_name in os.listdir(folder_path):
        # 检查文件名是否为数字加后缀 .tif
        if file_name.endswith(".tif") and file_name[:-4].isdigit():
            file_number = int(file_name[:-4])  # 提取数字部分
            if file_number in numbers_to_delete:
                file_path = os.path.join(folder_path, file_name)
                os.remove(file_path)
                deleted_files.append(file_name)

    # 输出删除结果
    if deleted_files:
        print(f"已删除以下文件：{', '.join(deleted_files)}")
    else:
        print("没有找到需要删除的文件。")

# 示例用法
image_path = "D:\Desktop\dataset\\temp\image"
boundary_path = 'D:\Desktop\dataset\\temp\\boundary'
distance_path = 'D:\Desktop\dataset\\temp\distance'
mask_path = 'D:\Desktop\dataset\\temp\mask'

# 范围可以修改
numbers_to_delete = list(range(3136,3138))
# numbers_to_delete = [1, 2, 5, 10]  # 自定义要删除的数字列表

delete_tif_files(image_path, numbers_to_delete)
delete_tif_files(mask_path, numbers_to_delete)
delete_tif_files(boundary_path, numbers_to_delete)
delete_tif_files(distance_path, numbers_to_delete)
