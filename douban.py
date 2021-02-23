# encoding:utf-8
from bs4 import BeautifulSoup #网页解析,获取数据
import re          #正则表达式,文字匹配
import urllib       #获取网页数据
import urllib.request
import urllib.parse
import xlwt         #进行excel操作
import sqlite3      #进行SQLITE数据库操作
def main():
    baseurl='https://movie.douban.com/top250?start='
    #爬取网页
    datalist=getdata(baseurl)
    savepath='豆瓣电影Top250.xls'
    #保存数据
    savedata(datalist,savepath)


findlink = re.compile(r'<a href="(.*?)">',re.S)
findimg = re.compile(r'<img.*src="(.*?)"',re.S)
findtitle = re.compile(r'<span class="title">(.*)</span>')
findscore = re.compile((r'<span class="rating_num" property="v:average">(.*)</span>'))
findnum = re.compile(r'<span>(\d*)人评价</span>')
findinu = re.compile(r'<span class="inq">(.*)。</span>')
finddetail = re.compile('<p class="">(.*?)</p>',re.S)

def askurl(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}

    req = urllib.request.Request(url=url, headers=headers)
    re = urllib.request.urlopen(req)
    ht=re.read().decode('utf-8')
    return ht

#爬取网页
def getdata(baseurl):
    datalist=[]
    for i in range(10):
        url=baseurl+str(25*i)
        ht=askurl(url)
        soup = BeautifulSoup(ht,'html.parser')
        for item in soup.find_all('div',class_="item"):
            data=[]
            item=str(item)

            link=re.findall(findlink,item)[0]
            data.append(link)

            img=re.findall(findimg,item)[0]
            data.append(img)

            title=re.findall(findtitle,item)
            if(len(title)==2):
                ctitle=title[0]
                data.append(ctitle)
                otitle=title[1].replace('/','')
                data.append(otitle)
            else:
                data.append(title[0])
                data.append(' ')

            score=re.findall(findscore,item)[0]
            data.append(score)

            num=re.findall(findnum,item)[0]
            data.append(num)

            inu=re.findall(findinu,item)
            if len(inu)!=0:
                inu=inu[0].replace('。','')
                data.append(inu)
            else:
                data.append(' ')

            detail = re.findall(finddetail, item)[0]
            detail = re.sub('<br(\s+)?/(\s+)?>',' ',detail)
            detail = re.sub('/',' ',detail).strip()
            data.append(detail)
            datalist.append(data)
            # print(link)
            # print(img)
            # print(title)
            # print(score)
            # print(num)
            # print(inu)
            # print(detail)
            # break

    return datalist



    return

#保存数据
def savedata(datalist,savepath):
    print('save...')
    book = xlwt.Workbook(encoding='utf-8',style_compression=0)
    sheet = book.add_sheet('豆瓣电影TOP250',cell_overwrite_ok=True)
    col = ('电影详情链接','图片链接','影片中文名','影片外国名','评分','评价数','概况','相关信息')
    for i in range(0,8):
        sheet.write(0,i,col[i])
    for i in range(0,250):
        print('第%d条'%(i+1))
        data=datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])
    book.save(savepath)

if __name__ == '__main__':
    main()