# -*- coding: UTF-8 -*-
import os
import subprocess


class FileUtils(object):

    def __init__(self):
        print(self)

    def get_all_file(self, path):
        files = []
        for root, dirs, files in os.walk(path):
            for file in files:
                files.append(os.path.join(root, file))

    def del_dir(self, path):
        for root, dirs, files in os.walk(path):
            for file in files:
                if (os.path.join(root, file).endswith(".html.z")):
                    print("remove=====" + os.path.join(root, file))
                    os.remove(os.path.join(root, file))

    def replace(self, path):
        for root, dirs, files in os.walk(path):
            for file in files:
                if (os.path.join(root, file).endswith(".html")):
                    print("replace=====" + os.path.join(root, file))
                    subprocess.Popen([
                        r"D:\Software\GIT\git\usr\bin\sed.exe ", "-i",
                        "s/Q　　Q：1234567/QQ:344769631/g",
                        os.path.join(root, file)
                    ],
                                     shell=True,
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.STDOUT)


if __name__ == "__main__":
    # fl=FileTools()
    # fl.replace(r"E:\博客文章\saibiao")
    print(__name__)
