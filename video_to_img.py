import os

# 定义一个函数，用于递归查找视频文件
def find_video_files(folder_path):
    video_files = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.mp4') or file.endswith('.MOV') or file.endswith('.mov') or file.endswith('.mkv'):
                video_files.append(os.path.join(root, file))

    return video_files

# 定义视频文件所在的文件夹路径
folder_path = "./hei"

# 获取所有视频文件，包括子文件夹中的视频
video_files = find_video_files(folder_path)


import cv2
import threading

# 定义一个函数，用于播放视频
def play_video(video_path,b):
    
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"无法打开视频文件：{video_path}")
        return
    

    for i in range(20,int(cap.get(cv2.CAP_PROP_FRAME_COUNT)),100):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = cap.read()
        if not ret:
            break
        img_path=f"img-hei/{b}_{str(i)}.jpg"
        cv2.imwrite(img_path,frame)
        print(img_path)


    cap.release()
# 创建一个线程列表，每个线程播放一个视频
threads = []
for b,video_file in enumerate(video_files):
    thread = threading.Thread(target=play_video, args=(video_file,b))
    threads.append(thread)

# 启动所有线程
for thread in threads:
    thread.start()

# 等待所有线程完成
for thread in threads:
    thread.join()

