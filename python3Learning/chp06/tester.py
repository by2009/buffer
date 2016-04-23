#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""

########################################################################
测试某一目录下的python脚本，传入命令行参数，将stdin和管道相连，通过捕获
stdout、stderr和退出状态来探测运行失败，以及获得前一次运行输出的回归记录。
利用subprocess模块派生和控制流(类似python 2.x中的os.popen3)，并可跨平台
运行。流在subprocess中均为二进制字节。测试用的输入、参数、输出和错误均映
射到子目录中的文件。

这是一个命令行脚本，使用可选的命令行参数作为测试目录名和强制生成标识符。
我们可以将它封装成一个可以调用的函数，不过它的结果是消息和输出文件，而
在这种情况下似乎调用/返回模型的用处不大。

建议的功能加强：可以扩展成通过测试脚本接受多组命令行参数和输入，以多次
运行同一个脚本(利用glob处理多个带有" .in"后缀的输入文件?)。还可以将所有
测试文件以不同扩展名保存在同一个目录下以简化软件结果，不过这个目录会随着
时间而增大。另外可以在运行失败时保存stderr和stdout，不过我个人倾向于在输
出中以回归的方式记录预期/实际输出。
########################################################################
"""

import os
import sys
import glob
import time
from subprocess import Popen, PIPE

# 配置参数
testdir = sys.argv[1] if len(sys.argv) > 1 else os.curdir
forcegen = len(sys.argv) > 2
print('Start tester:', time.asctime())
print('in', os.path.abspath(testdir))


def verbose(*args):
    print('-' * 80)
    for arg in args:
        print(arg)


def quiet(*args): pass

trace = quiet

# 对待测的脚本运行glob
testpatt = os.path.join(testdir, 'Scripts', '*.py')
testfiles = sorted(glob.glob(testpatt))
trace(os.getcwd(), *testfiles)

numfail = 0
for testpath in testfiles:
    testname = os.path.basename(testpath)  # 去除目录路径

    # 获取输入和参数
    infile = testname.replace('.py', '.in')
    inpath = os.path.join(testdir, 'Inputs', infile)
    indata = open(inpath, 'rb').read() if os.path.exists(inpath) else b''

    argfile = testname.replace('.py', '.args')
    argpath = os.path.join(testdir, 'Args', argfile)
    argdata = open(argpath).read() if os.path.exists(argpath) else ''

    # 定位输出和错误，清除前次结果
    outfile = testname.replace('.py', '.out')
    outpath = os.path.join(testdir, 'Outputs', outfile)
    outpathbad = outpath + '.bad'
    if os.path.exists(outpathbad):
        os.remove(outpathbad)

    errfile = testname.replace('.py', '.err')
    errpath = os.path.join(testdir, 'Errors', errfile)
    if os.path.exists(errpath):
        os.remove(errpath)

    # 测试运行时使用重定向过的流
    pypath = sys.executable
    command = '%s %s %s' % (pypath, testpath, argdata)
    trace(command, indata)

    process = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    process.stdin.write(indata)
    process.stdin.close()
    outdata = process.stdout.read()
    errdata = process.stderr.read()
    exitstatus = process.wait()
    trace(outdata, errdata, exitstatus)

    # 分析结果
    if exitstatus != 0:
        print('ERROR status:', testname, exitstatus)
    if errdata:
        print('ERROR stream:', testname, errpath)
        open(errpath, 'wb').write(errdata)
    if exitstatus or errdata:
        numfail += 1
        open(outpathbad, 'wb').write(outdata)
    elif not os.path.exists(outpath) or forcegen:
        print('generating:', outpath)
        open(outpath, 'wb').write(outdata)

    else:
        priorout = open(outpath, 'rb').read()
        if priorout == outdata:
            print('passed:', testname)
        else:
            numfail += 1
            print('FAILED output:', testname, outpathbad)
            open(outpathbad, 'wb').write(outdata)

print('Finished:', time.asctime())
print('%s tests were run, %s tests failed.' % (len(testfiles), numfail))
