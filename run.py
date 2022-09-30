# -*- coding: utf-8 -*-
# @Time    : 2022/9/30 23:11
# @Author  : Circleone_
import sys


def main():
    argvs = sys.argv
    print(argvs)
    if 'task' in argvs:
        print('执行任务')
    else:
        print('未接收到任务参数')

if __name__ == '__main__':
    main()