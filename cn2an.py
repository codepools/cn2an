import os
import cn2an

files = os.listdir(".")  # 假定你的文件和这个脚本在同一个目录下。
#小王捡了一百块钱.mp4 这种文件格式都可以
# 模块的网址 https://pypi.org/project/cn2an/   
for file in files:
    newname=cn2an.transform(file, "cn2an")
    os.rename(file,newname);