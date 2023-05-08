# -*- coding: <utf-8> -*-
import subprocess


class SystemUtils(object):

    def __init__(self):
        super()

    def execommand(self, command):
        out = subprocess.Popen(command,
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)
        return out.stdout.readlines()

    def get_all_process(self):
        lst = self.execommand("ps -ef")
        dic = dict()
        for line in lst:
            strs = line.decode("UTF8").split(",")
            dic[strs[1].replace('"', '')] = strs[0].replace('"', '')
        return dic


if __name__ == "__main__":
    cls = SystemUtils()
    ss = "12344ggg"
    for s in ss:
        print(s)
    # print(cls.getAllProcess())
