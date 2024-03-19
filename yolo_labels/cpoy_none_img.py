import os
import shutil

def find_empty_txt_files(folder_path):
    empty_txt_files = []

    # 遍历文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 检查文件是否是txt文件
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                # 检查文件大小是否为零
                if os.path.getsize(file_path) == 0:
                    empty_txt_files.append(file_path)

    return empty_txt_files

def copy_empty_txt_files(empty_txt_files, destination_folder):
    for file_path in empty_txt_files:
        # 构建目标文件路径
        file_path = file_path.replace(".txt",".jpg").replace("labels","images")
        destination_path = os.path.join(destination_folder, os.path.basename(file_path))
        # 复制文件
        try:
            shutil.copy2(file_path, destination_path)
        except:
            if "train" in file_path:
                file_path=file_path.replace("train","val")
            else:
                file_path=file_path.replace("val","train")
            shutil.copy2(file_path, destination_path)
        print(f"已复制文件: {file_path} 到 {destination_path}")

# 指定源文件夹路径和目标文件夹路径
source_folder = "./labels"
destination_folder = "./none_img"

# 查找空txt文件
empty_txt_files = find_empty_txt_files(source_folder)

# 复制空txt文件到目标文件夹
copy_empty_txt_files(empty_txt_files, destination_folder)

