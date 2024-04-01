# coding=utf-8
import numpy as np
import cv2
import glob
label_path = r"labels/4_1242_shigao.txt"
image_path = r"images/4_1242_shigao.jpg"
image_path_list = glob.glob("images/*.jpg")

# 坐标转换，原始存储的是YOLOv5格式
# Convert nx4 boxes from [x, y, w, h] normalized to [x1, y1, x2, y2] where xy1=top-left, xy2=bottom-right
def xywhn2xyxy(x, w=640, h=640, padw=0, padh=0):
    y = np.copy(x)
    y[:, 0] = w * (x[:, 0] - x[:, 2] / 2) + padw  # top left x
    y[:, 1] = h * (x[:, 1] - x[:, 3] / 2) + padh  # top left y
    y[:, 2] = w * (x[:, 0] + x[:, 2] / 2) + padw  # bottom right x
    y[:, 3] = h * (x[:, 1] + x[:, 3] / 2) + padh  # bottom right y
    return y

for image_path in image_path_list:
    # 读取labels
    label_path=image_path.replace("images","labels").replace("jpg","txt")
    print(label_path)
    with open(label_path, 'r') as f:
        lb = np.array([x.split() for x in f.read().strip().splitlines()], dtype=np.float32)  # labels
    # 读取图像文件
    img = cv2.imread(image_path)
    h, w = img.shape[:2]
    if lb.any():
        lb[:, 1:] = xywhn2xyxy(lb[:, 1:], w, h, 0, 0)  # 反归一化

        # 绘图
        for _, x in enumerate(lb):
            class_label = int(x[0])  # class
            cv2.rectangle(img, (int(x[1]), int(x[2])), (int(x[3]), int(x[4])), (0, 255, 0))
    cv2.imshow("show",cv2.resize(img, (int(w*0.5),int(h*0.5)), interpolation=cv2.INTER_LINEAR))
    if cv2.waitKey(int(1000 / 2)) & 0xFF == ord('q'):
            break
    #cv2.imshow('show', img)
    #cv2.waitKey(0)  # 按键结束
cv2.destroyAllWindows()
