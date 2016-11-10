## 介绍
这个脚本用来删除最近3年内所有的微博。

这个脚本目前单独作为一个项目了 :joy:，地址为[delmyweibo](https://github.com/crane-yuan/delmyweibo)

## 使用方式
这个脚本已经在Firefox49上经过了测试，可以使用。

### greasemonkey插件方式
- 添加这个脚本到[greasemonkey](https://greasyfork.org/zh-CN)；
- 登录上自己的新浪微博账号，点击“我的主页”即可。

### 手动方式
- 登录上自己的新浪微博账号，点击“我的主页”；
- 然后打开在Firefox（或者Google Chrome）下的js控制台，复制js代码到控制台，运行即可。

## 日志
- #2016-11-9，修复「删除微博脚本」中settimeout中循环执行函数问题，最终采用「闭包」解决。
- #2016-11-9 晚上，对「删除微博脚本」中删除逻辑部分进行了优化。
- #2016-11-10，「删除微博」单独抽出来作为一个独立的项目进行开发。