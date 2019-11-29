# coding = UTF-8

import urllib.request
import re
import os


# open the url and read
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    page.close()
    return html

# compile the regular expressions and find
# all stuff we need
def getUrl(html):
    reg = r'(?:href|HREF)="?((?:http://)?.+?\.pdf)'
    url_re = re.compile(reg)

    # url_lst = url_re.findall(html.decode('gb18030')) #爬icfa解码
    # url_lst = url_re.findall(html.decode('gb2312')) #爬所网页解码
    url_lst = url_re.findall(html.decode('utf-8'))
    return(url_lst)

def getFile(url,nameorder):
    url1 = url.split('/')[-1]  #除去url里不要的信息做为文件名
    #file_name = file_name1 #file_name = 'No' +str(nameorder) + '- -' + file_name1  #从url里提取的文件名加编号
    # url1 = str(url[41:51])
    # url1 = url1.replace('/', "-")  #url1.split('/')   #url1=re.sub('/')#url1.strip('/')   #
    print (url1)
    file_name = url1 #+ '.pdf'
    print(url)
    print ("try to download" + " " + file_name)
    print(url)

    u = urllib.request.urlopen(url)
    f = open(file_name, 'wb')or url in url_lst[:]
    nameorder += 1
    url = root_url + url

    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        f.write(buffer)
    f.close()
    print ("Sucessful to download" + " " + file_name)


root_url = ''

raw_url ="http://sci-hub.tw/10.1016/0005-7916(72)90029-8"
# "http://sci-hub.tw/10.1037/h0058775"
    #'http://sci-hub.tw/10.3389/fphys.2019.00111'
#https://indico.pshttps://indico.psi.ch/event/6698/contributions/16529/attachments/13708/17935/
#'https://indico.psi.ch/event/6698/timetable/#20190227'
#'http://acc1.ihep.ac.cn/bepcyx/zbb/index.shtml'

html = getHtml(raw_url)
url_lst = getUrl(html)

foldername = '值班表'
if os.path.exists(foldername)==0:  #判读目录是否存在
        os.mkdir(foldername)  #创建目录
os.chdir(os.path.join(os.getcwd(), foldername))  #打开目录

nameorder = 0



for url in url_lst[:]:
    nameorder += 1
    url = root_url + url
    url = url[1:]
    getFile(url, nameorder)
