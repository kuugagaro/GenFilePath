import os

file_dir = r"C:\Users\Kuuga\Desktop\view2_1"
i = 1
a = os.walk(file_dir)
b = None
for root, dirs, files in os.walk(file_dir):
    # print(i)
    i += 1
    print(root)  # 当前目录路径
    # print(dirs)  # 当前路径下所有子目录
    print(files)  # 当前路径下所有非目录子文件

    for file in files:
        if file:
            path = root + '\\' + file
            print(path)
            # print(path)
            aFile = file.replace('.', '_').replace('-', '_')
            rpath = root + '\\' + aFile
            print(rpath)
            os.rename(path, rpath)
