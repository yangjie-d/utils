import glob
from tqdm import tqdm
import shutil

file_list=glob.glob("labels/*")
for file_path in tqdm(file_list):
    img_path = file_path.replace("labels","../img_data").replace("txt","jpg")
    new_file_path = img_path.replace("../img_data","images/")
    shutil.copy(img_path,new_file_path)
    

