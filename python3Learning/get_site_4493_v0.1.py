#!/usr/bin/env python3
# -*- coding=utf-8 -*-


import requests
import os
import json
from datetime import datetime
from bs4 import BeautifulSoup


class Picture:
    '''
    爬取'4493美图'网站的图片

    root:       http://www.4493.com
    category:   weimeixiezhen
    page:       爬取的页面数
    sub_page:   同一类别图片数量
    dir:        下载图片的根目录
    '''

    def __init__(self, root='http://www.4493.com',
                 category='weimeixiezhen',
                 page=10, pic_page=20, dir='./photos'):
        self.root = root
        self.category = category
        self.page = page
        self.pic_page = pic_page
        self.dir = dir

        # 开始爬取的页号
        self.beginpage = 0

        # 反反倒链
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36', 'Referer': ''}

        # 板块下的页面url
        self.page_pools = dict()
        # 具体图集页面的开始url
        self.pic_pools = dict()
        # 图片的url
        self.img_pools = dict()
        # create dir
        if not os.path.exists(dir):
            os.mkdir(dir)

    def getPage(self):
        '''
        爬取页面url，放进page_pools
        '''
        pagecount = self.beginpage
        while pagecount < self.page:
            pagecount += 1
            page_url = os.path.join(
                self.root,
                self.category,
                'index-%d.htm' %
                pagecount)
            # put page_url into page_pools
            if page_url not in self.page_pools.values():
                self.page_pools[
                    self.category + '-' + str(pagecount)] = page_url
        print('get %d page...' % len(self.page_pools))
        # 存储板块链接
        category_file = self.category + '_page.json'
        if not os.path.exists(category_file):
            with open(category_file, 'w') as file:
                json.dump(self.page_pools, file)

    def getPicUrl(self):
        '''
        爬取图片url，放进pic_pools
        '''
        # 抓取页面url
        self.getPage()

        for page_url in self.page_pools.values():
            try:
                page_request = requests.get(page_url, timeout=3)
                # status_code
                if page_request.status_code != requests.codes.ok:
                    continue
                page_content = page_request.content
                # BeautifulSoup
                page_soup = BeautifulSoup(page_content, 'lxml')

                # --title
                title = page_soup.title.string
                # print(title)

                # pic urls
                for ul in page_soup.select('.clearfix'):
                    ul = ul.encode('utf-8')
                    # ul BeautifulSoup
                    ul_soup = BeautifulSoup(ul, 'lxml')
                    for pic_url in ul_soup.select('a'):
                        # 获取图集名称
                        pic_name = pic_url.span.string
                        pic_url = self.root + pic_url['href']
                        # put pic url into pic_pools
                        self.pic_pools[pic_name] = pic_url
            except Exception as e:
                print(e)
        # print(self.pic_pools)
        # 存储图集入口信息
        altas_name = self.category + '_atlas.json'
        if not os.path.exists(altas_name):
            with open(altas_name, 'w') as file:
                json.dump(self.pic_pools, file)

    def getPicInfo(self):

        # 开始抓取的时间
        begin_time = datetime.now()
        print('begin time is %s' % str(begin_time))

        # 抓取图片url
        self.getPicUrl()

        for pic_url in self.pic_pools.values():
            url = pic_url.replace('1.htm', '')
            pic_num = 0
            while pic_num < self.pic_page:
                pic_num += 1
                pic_url = url + '%d.htm' % pic_num
                try:
                    pic_request = requests.get(pic_url)
                    # status_code
                    if pic_request.status_code != requests.codes.ok:
                        continue
                    pic_content = pic_request.content
                    # BeautifulSoup
                    pic_soup = BeautifulSoup(pic_content, 'lxml')

                    # pic dir name
                    pic_dir_name = pic_soup.title.string
                    pic_dir_name = "".join(pic_dir_name.split('_')[:1])

                    # img
                    pic_list = list()
                    for img_url in pic_soup.select('p > img'):
                        img_url = img_url['src']
                        pic_list.append(img_url)
                        # 打印下载图片提示
                        print(
                            'downloading pic ---> %s...' %
                            (pic_dir_name + '%d.jpg' %
                             (pic_num)))
                        # 下载图片
                        referer = pic_url
                        self.headers['Referer'] = referer
                        self.__downloadpic__(img_url, pic_dir_name, pic_num)
                    # put pic_list into img_pools
                    self.img_pools[pic_dir_name] = pic_list
                except Exception as e:
                    print(e)
        print(self.img_pools)
        # 存储图集url
        img_name = self.category + '_img.json'
        if not os.path.exists(img_name):
            with open(img_name, 'w') as file:
                json.dump(self.img_pools, file)

        # 结束抓取时间
        end_time = datetime.now()
        total_time = end_time - begin_time
        print('end time is %s' % str(total_time))

    def __downloadpic__(self, img_url, pic_dir_name, pic_index):
        try:
            # print(img_url)
            img_request = requests.get(img_url, headers=self.headers)
            img_content = img_request.content
            # img dir
            img_dir = os.path.join(self.dir, pic_dir_name)
            if not os.path.exists(img_dir):
                os.mkdir(img_dir)
            # img path
            img_path = os.path.join(
                img_dir,
                pic_dir_name +
                '%d.jpg' %
                pic_index)
            with open(img_path, 'wb') as img_file:
                img_file.write(img_content)
                img_file.close()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    pic = Picture('http://www.4493.com', 'weimeixiezhen')
    pic.getPicInfo()
