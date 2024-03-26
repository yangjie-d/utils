import glob
def create_file(file_name, content=None):
    """
    根据文件名创建文件，并写入内容。

    参数：
    file_name: 要创建的文件名，包括路径。
    content: 要写入文件的内容，可选。

    返回：
    无
    """
    with open(file_name, 'w') as file:
        if content is not None:
            file.write(content)
        print(f"文件 '{file_name}' 已创建。")
A = glob.glob("images/*")
for i in A:
    #file_name=i.replace("img-none","labels/val").replace("jpg","txt")
    file_name=i.replace("images","labels").replace("jpg","txt")
    create_file(file_name)
