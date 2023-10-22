# -*- coding: utf-8 -*-
# By:Eastmount CSDN
import urllib.request
import re 
from bs4 import BeautifulSoup
import codecs

#-------------------------------------爬虫函数-------------------------------------
def crawl(url, headers):

    print('爬取豆瓣电影250: \n')
    request = urllib.request.Request(url='https://movie.douban.com/top250', headers=headers)
    response = urllib.request.urlopen(request)
    contents = response.read().decode('utf-8')
                                       
    # print('爬取豆瓣电影250: \n')
    # page = urllib.request.Request(url, headers=headers)
    # page = urllib.request.urlopen(page)
    # contents = page.read()
    
    soup = BeautifulSoup(contents, "html.parser") 
    infofile.write("")

    
    for tag in soup.find_all(attrs={"class":"item"}):
        #爬取序号
        num = tag.find('em').get_text()
        print(num)
        infofile.write(num + "\r\n")
        
        #电影名称
        name = tag.find_all(attrs={"class":"title"})
        # print(name)
        # print(name[0])
        zwname = name[0].get_text()
        print('[中文名称]', zwname)
        infofile.write("[中文名称]" + zwname + "\r\n")

        wwname = name[1].get_text().strip().lstrip('/') if len(name)>1 else "null"

        print('[外文名称]', wwname)
        infofile.write("[外文名称]" + wwname + "\r\n")

        
        #网页链接
        url_movie = tag.find(attrs={"class":"hd"}).a
        urls = url_movie.attrs['href']
        print('[网页链接]', urls)
        infofile.write("[网页链接]" + urls + "\r\n")

        #导演和演员信息
        actors = tag.find(attrs={"class":"bd"}).p
        actor_info=actors.get_text().replace(' ','').replace('\n',' ')
        print('[制作信息]',actor_info)
        print(actors.attrs['quote'].get_text())

        urls = actors.attrs['href']
        print('[网页链接]', urls)
        infofile.write("[网页链接]" + urls + "\r\n")
        
        # #爬取评分和评论数
        info = tag.find(attrs={"class":"star"}).get_text()
        info = info.replace('\n',' ')
        info = info.lstrip()
        print('[评分评论]', info)
        
        # #获取评语
        info = tag.find(attrs={"class":"inq"})
        if(info): #避免没有影评调用get_text()报错
            content = info.get_text()
            print('[影评]', content)
            infofile.write(u"[影评]" + content + "\r\n")
        print('')
        


#-------------------------------------主函数-------------------------------------
if __name__ == '__main__':
    print("hello")
    #存储文件
    infofile = codecs.open("Result_Douban.txt", 'a', 'utf-8')
    
    #消息头
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}

    #翻页
    i = 0
    while i<10:
        print('页码', (i+1))
        num = i*25 #每次显示25部 URL序号按25增加
        url = 'https://movie.douban.com/top250?start=' + str(num) + '&filter='
        crawl(url, headers)
        infofile.write("\r\n\r\n")
        i = i + 1
    infofile.close()