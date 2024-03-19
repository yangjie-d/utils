import glob
X = glob.glob("./image-none/*")
import random
random.shuffle(X)
train_size = int(len(X)*0.7)
val_size = len(X) - train_size
import shutil
for i in X[:train_size]:
    new_path_img = i.replace("image-none","data-1w-none/images/train")
    old_path_txt = i.replace("image-none","txt-none").replace(".jpg",".txt")
    new_path_txt = old_path_txt.replace("txt-none","data-1w-none/labels/train")
    #print(new_path_img)
    #print(new_path_txt)
    #print(old_path_txt)
    #print(i)
    #break
    shutil.copy(i,new_path_img)
    shutil.copy(old_path_txt,new_path_txt)

for i in X[train_size:]:
    new_path_img = i.replace("image-none","data-1w-none/images/val")
    old_path_txt = i.replace("image-none","txt-none").replace(".jpg",".txt")
    new_path_txt = old_path_txt.replace("txt-none","data-1w-none/labels/val")
    #print(new_path_img)
    #print(new_path_txt)
    #print(old_path_txt)
    #print(i)
    #break
    shutil.copy(i,new_path_img)
    shutil.copy(old_path_txt,new_path_txt)
