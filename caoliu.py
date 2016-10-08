#coding=utf-8
import urllib,re,urllib2,thread,threading
import requests,chardet
import os
picpath="D:\crapy\caoliu\\"

def saveImg(imageURL,fileName):
    u = urllib2.urlopen(imageURL).read()
    f = open(fileName, 'wb')
    f.write(u)
    f.close()
def savecontent(fileName,content):
    f = open(fileName, 'w')
    f.write(content.encode('utf-8'))
    f.close()
def savePage(pagelist,content):

    for i in pagelist:
        url=i
        regid=re.compile('.*/(.*?).html')
        a=regid.findall(url)
        try:
            os.makedirs('D:\\crapy\\caoliu\\file'+a[0])
        except:
            print 'this page has downloaded'
            continue
        filepath='D:\\crapy\\caoliu\\file'+a[0]
        page=requests.get(url).text
        regex=re.compile(r"<input src='(.*?)' type='image'.*?>")
        items=regex.findall(page)
        x=1
        savecontent(filepath+'\\'+'content.txt',content)
        for link in items:
            try:
                filename=filepath+'\\'+'%s.jpg'%x
                x+=1
                saveImg(link,filename)
            except:
                print 'error when downlading %s'%link
                continue                 
        print('done')

url1='http://t66y.com/thread0806.php?fid=16&search=&page=2'
url='http://t66y.com/thread0806.php?fid=16'
page=requests.get(url).text.encode('iso-8859-1').decode('gbk')

if 'codeform.php' in page:
    print 'need verification'
    page1=requests.get('http://t66y.com/codeform.php').text
    page2=page1.encode('iso-8859-1').decode('gbk')
    #print page2


    import cookielib
    CaptchaUrl = "http://t66y.com/require/codeimg.php"
    PostUrl = "http://t66y.com/codeform.php"
    # 验证码地址和post地址
    cookie = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    # 将cookies绑定到一个opener cookie由cookielib自动管理
    username = 'username'
    password = 'password123'
    # 用户名和密码
    picture = opener.open(CaptchaUrl).read()
    # 用openr访问验证码地址,获取cookie
    local = open('C:\Users\mikelee\Desktop\image.jpg', 'wb')
    local.write(picture)
    local.close()

    # 保存验证码到本地
    SecretCode = raw_input('输入验证码：')


    postData = {
    'validate':SecretCode
    }
    # 根据抓包信息 构造表单
    print postData

    headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',

    'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
    'Cache-Control':'max-age=0',
    'Content-Length':13,
    'Content-Type':'application/x-www-form-urlencoded',
    'Cookie':'__cfduid=d2c8f9e5e4a7bc83511a05831f29316751446276271; 227c9_lastfid=0; 227c9_lastvisit=0%091466218032%09%2Fread.php%3Ftid%3D1962629%26fpage%3D0%26toread%3D%26page%3D4; CNZZDATA950900=cnzz_eid%3D528847293-1446273281-http%253A%252F%252Ft66y.com%252F%26ntime%3D1475766349; PHPSESSID=5vnqonkj1n12vsbbhu06t7l3c5',
    'DNT':1,
    'Host':'t66y.com',
    'Origin':'http://t66y.com',
    'Proxy-Connection':'keep-alive',
    'Referer':'http://t66y.com/codeform.php',
    'Upgrade-Insecure-Requests':1,
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
    }
        # 根据抓包信息 构造headers
    data = urllib.urlencode(postData)
    print data
    # 生成post数据 ?key1=value1&key2=value2的形式
    request = urllib2.Request(PostUrl, data, headers)
    # 构造request请求
    try:
        response = opener.open(request)
        print response.read()
        print '-----------------------------'
        result = response.read().decode('gb2312')
    # 由于该网页是gb2312的编码，所以需要解码
        print result
    # 打印登录后的页面
    except urllib2.HTTPError, e:
        print 'error'
        print e.code












    

regex=re.compile(r'<a href="(.*?)" target="_blank".*?>(.*?)</a>')
regex1=re.compile(r'<a href="htm_data(.*?)" target="_blank".*?>(.*?)</a>')
items_dict=regex.findall(page)
items1=regex1.findall(page)
a=dict(items_dict)

items=[]
for key in a:
    items.append(key)
lis=[]
content=[]
for i in items:
    if 'htm_data' in i:
        lis.append('http://t66y.com/'+i)
        content.append(a[i])
        continue
print 1
threadLock = threading.Lock()
threads = []

for j in range(len(lis)):
    print 2
    thread1=threading.Thread(target=savePage,args=([lis[j]],content[j]))
    thread1.start()
    threads.append(thread1)
print 3

for t in threads:
    t.join()
print "Exiting Main Thread"
