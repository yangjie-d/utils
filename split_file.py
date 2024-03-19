import glob
from tqdm import tqdm
import shutil
import random
file_list=glob.glob("labels/*")
random.shuffle(file_list)
split_num = int(len(file_list) * 0.7)
for file_path in tqdm(file_list[:split_num]):
    new_file_path = file_path.replace("labels","datasets/labels/train")
    shutil.copy(file_path,new_file_path)
    
    img_path = file_path.replace("labels","images").replace("txt","jpg")
    new_img_path = img_path.replace("images","datasets/images/train")
    shutil.copy(img_path,new_img_path)
    
for file_path in tqdm(file_list[split_num:]):
    new_file_path = file_path.replace("labels","datasets/labels/val")
    shutil.copy(file_path,new_file_path)
    
    img_path = file_path.replace("labels","images").replace("txt","jpg")
    new_img_path = img_path.replace("images","datasets/images/val")
    shutil.copy(img_path,new_img_path)
