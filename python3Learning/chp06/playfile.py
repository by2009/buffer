#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""

##############################################################################
尝试打开任意一种媒体文件。总是使用通用网页浏览器架构，不过也允许使用特定播放器。
代码不经修改，有可能在你的系统上无法正常工作；对于音频文件，在Unix下使用filter
和命令行打开，在windows下利用文件名关联通过start命令打开(也就是说，使用你的机器
上的程序打开.au文件，可能是一个音频播放器，也可能是一个网页浏览器)。可以根据需要
进行配置和扩展。playknownfile假定你知道想打开的文件的媒体类型，而playfile尝试利
用python mimetypes模块自动决定媒体类型；碰到未知mimetype或系统平台时，二者都尝试
用python webbrowser模块启动一个网页浏览器，作为最后一招。
##############################################################################
"""

import os, sys, mimetypes, webbrowser

helpmsg = """
Sorry: can't find a media player for '%s' on your system!
And an entry for your system to the media player dictionary
for this type of file in playfile.py, or play the file manually.
"""

def trace(*args): print(*args)

############################################################
# 播放器技巧：通用或特定：待扩展
############################################################

class MediaTool:
    def __init__(self, runtext=''):
        self.runtext = runtext
    def run(self, mediafile, **options):
        fullpath = os.path.abspath(mediafile)
        self.open(fullpath, **options)

class Filter(MediaTool):
    def open(self, mediafile, **ignored):
        media = open(mediafile, 'rb')
        player = os.popen(self.runtext, 'w')
        player.writer(media.read())

class Cmdline(MediaTool):
    def open(self, mediafile, **ignored):
        cmdline = self.runtext % mediafile
        os.system(cmdline)

class Winstart(MediaTool):
    def open(self, mediafile, wait=False, **other):
        if not wait:
            os.startfile(mediafile)
        else:
            os.system('start /WAIT' + mediafile)

class Webbrowswer(MediaTool):
    def open(self, mediafile, **options):
        webbrowser.open_new('file://%s' % mediafile, **options)

######################################################################
# 媒体类型特异且系统平台特异的策略：修改，或者传入一个新的策略作为代替
######################################################################

# 建立系统平台和播放器的对应关系：在此修改！

audiotools = {
    'sunos5': Filter('/usr/bin/audioplay'),
    'linux': Cmdline('cat %s > /dev/audio'),
    'sunos4': Filter('/usr/demo/SOUND/play'),
    'win32':  Winstart()
}

videotools = {
    'linux': Cmdline('tkcVideo_c700 %s'),
    'win32':  Winstart()
}

imagetools = {
    'linux': Cmdline('eog %s'),
    'win32':  Winstart()
}

texttools = {
    'linux': Cmdline('videotools %s'),
    'win32':  Cmdline('notepad %s')
}

apptools = {
    'win32': Winstart()
}

# 建立文件名的mimetype与播放器表格的对应关系

mimetable = {
    'audio': audiotools,
    'video': videotools,
    'image': imagetools,
    'text':  texttools,
    'application': apptools
}


############################################################
# 顶层接口
############################################################

def trywebbrowser(filename, helpmsg=helpmsg, **options):
    """
    用网页浏览器打开文本/html，另外对于其他文件类型，如果碰到未知mimetype
    或系统平台，也用网页浏览器进行尝试，作为最后的办法
    """
    
    trace('trying browser', filename)
    try:
        player = Webbrowswe()
        player.run(filename, **options)
    except:
        print(helpmsg % filename)

def playknownfile(filename, playertable={}, **options):
    """
    播放类型已知的媒体文件：使用平台特异的播放器对象，如果这个平台下没有相对应
    工具则派生一个网页浏览器；接受媒体特异的播放器表格
    """

    if sys.platform in playertable:
        playertable[sys.platform].run(filename, **options)
    else:
        trywebbrowser(filename, **options)

def playfile(filename, mimetable=mimetable, **options):
    """
    播放任意类型媒体文件：使用mimetypes猜测媒体类型并对应到平台特异的播放器表格；
    如果是文本/html，或者未知媒体类型，或者没有播放器表格，则派生网页浏览器
    """

    contenttype, encoding = mimetypes.guess_type(filename)
    if contenttype == None or encoding is not None:
        contenttype = '?/?'
    maintype, subtype = contenttype.split('/', 1)
    if maintype == 'text' and subtype == 'html':
        trywebbrowser(filename, **options)
    elif maintype in mimetable:
        playknownfile(filename, mimetable[maintype], **options)
    else:
        trywebbrowser(filename, **options)

############################################################
# 自测代码
############################################################

if __name__ == '__init__':
    playfile('1.jpg')
