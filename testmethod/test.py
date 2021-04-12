# -*- coding:utf-8 -*-
# /usr/bin/env python
import commands



def getTopCpu():
    top_list = commands.getoutput("adb shell top -m 100 -n 1 -d 5 ").split('\n')
    dimension_two = [top_list[i].split() for i in range(len(top_list))]
    # 提取信息
    info = get_key(dimension_two)
    # 打印
    print(info)
    for key, value in info.items():
        print key, value

    return info


def get_key(dimension_two):
    keys = ['PID', 'CPU%', 'Name']
    info = {}
    print(1111, dimension_two)
    for i, row in enumerate(dimension_two):  # row = dimension_two[i]
        print(i , row)
        for j, val in enumerate(row):  # val = dimension_two[i][j]
            print(j, val)
            if val in keys:
                info[val] = [dimension_two[t][j] for t in range(i + 1, len(dimension_two))]

    return info


if __name__ == '__main__':
    getTopCpu()