#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""

######################################################################
为迁移站点，创建转向链接页面。
为每个已有站点的html文件身材一个页面；将生成的文件上传到你的旧网站。
关于在页面文件生成时或者之后在脚本中执行上传的方法，请参考本书稍后
关于ftplib的部分。
######################################################################
"""

import os

servername = 'learning-python.com'      # 站点迁移的目的地
homedir = 'books'                       # 站点根目录
sitefilesdir = r'html'                  # 站点文件在本地的路径
uploaddir = r'pulic'                    # 准备存放转向链接文件的目录
templatename = 'template.html'          # 待生成的页面的模板

try:
    os.mkdir(uploaddir)
except OSError: pass

template = open(templatename).read()
sitefiles = os.listdir(sitefilesdir)

count = 0;
for filename in sitefiles:
    if filename.endswith('.html') or filename.endswith('.htm'):
        fwdname = os.path.join(uploaddir, filename)
        print('creating', filename, 'as', fwdname)
        filetext = template.replace('$server$', servername)
        filetext = filetext.replace('$home$', homedir)
        filetext = filetext.replace('$file$', filename)
        open(fwdname, 'w').write(filetext)
        count += 1

print('Last file =>\n', filetext, sep='')        
print('Done:', count, 'forward files created.')

