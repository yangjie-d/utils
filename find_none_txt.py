import os

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

# 指定文件夹路径
folder_path = "./labels/train"

# 查找空txt文件
empty_txt_files = find_empty_txt_files(folder_path)

# 打印结果
if empty_txt_files:
    print("空的txt文件:")
    for file_path in empty_txt_files:
        print(file_path)
else:
    print("未找到空的txt文件。")

