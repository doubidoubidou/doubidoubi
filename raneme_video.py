import os

# 适用于'作者/日期/文件夹/文件'格式
folderpath = r'H:\懂的都懂\COS\000\Tokar浵卡'
folders_out = os.listdir(folderpath)
for folder_out in folders_out:
    folder_out_path = os.path.join(folderpath, folder_out)
    folders_in = os.listdir(folder_out_path)
    for folder_in in folders_in:
        folder_in_path = os.path.join(folder_out_path, folder_in)
        if os.path.isdir(folder_in_path):
            videos = os.listdir(folder_in_path)
            if len(videos) == 1:
                raw_video = os.path.join(folder_in_path, videos[0])
                current_video = os.path.join(folder_in_path, folder_in + '.mp4')
                os.rename(raw_video, current_video)
                print([raw_video, current_video])
            else:
                index = 1
                for video in videos:
                    raw_video = os.path.join(folder_in_path, video)
                    current_video = os.path.join(folder_in_path, folder_in + '_' + str(index) + '.mp4')
                    os.rename(raw_video, current_video)
                    index += 1
                    print([raw_video, current_video])
