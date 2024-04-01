import os
import concurrent.futures
from pathlib import Path
def find_video_files(folder_path):
    video_files = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.mp4') or file.endswith('.MOV') or file.endswith('.mov') or file.endswith('.mkv'):
                video_files.append(os.path.join(root, file))

    return video_files
def process_file(input_file, output_file):

    # 使用ffmpeg调整视频大小
    os.system(f"ffmpeg -i {input_file} -vf scale=1920:1080 {output_file}")
    
    print(f"转换完成: {input_file} -> {output_file}")

def main():
    # 输入文件夹
    input_folder = "海康隧道视频/上午"

    # 输出文件夹
    output_folder = "海康隧道视频-zhuan/"

    # 确保输出文件夹存在
    Path(output_folder).mkdir(parents=True, exist_ok=True)
    max_workers = 5

    # 列出输入文件夹中的所有.mp4文件
    video_files = find_video_files(input_folder)
    print(video_files)

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 使用多线程处理每个视频文件
        futures = {executor.submit(process_file, video_file, output_folder + video_file.split("/")[-1]): video_file for video_file in video_files}

        # 等待所有任务完成
        concurrent.futures.wait(futures)

if __name__ == "__main__":
    main()

