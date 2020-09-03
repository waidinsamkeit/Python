
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 该脚本可以定位访问web页面的服务质量
# 通过Python下的pycurl模块来实现定位
# 它可以通过调用pycurl提供的方法，来探测Web服务质量
# 比如了解相应的HTTP状态码、请求延时、HTTP头信息、下载速度等
# PIP install 清华源码pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pycurl
# 采用pycurl方法对URL进行获取,以及Dnspython便利DNS信息
import time
import sys
import pycurl
import os
import dns.resolver
count=40
print('*'*count)
print("""[使用须知]
1.采用Pycurl进行获取URL内容链接,并且保存到html.txt,注意该txt文档只能保存一个url的全部信息,\n
如果下一次重新探测URL则会被替换。
2.采用Dnspythonv2.0.0,遍历最快速的DNS解析。
3.此程序仅仅用于探测web服务质量
4.此程序需要安装 os/time/sys/pycurl/dnspython
5.输入探测的域名的时候不要使用https!!!
6.支持Http自动跳转Https，如果网站本身没有rewrite则不支持！！！
7.如果报错curl: (60) SSL certificate problem: unable to get local issuer certificate,由于我没有设置安全信任
8.仅支持站点检测,子目录自测吧""")
print("*"*count)
# 探测目标URL
while True:
    URL = str(input("请输入探测目标URL: "))
    # 创建一个Curl对象
    pcu = pycurl.Curl()
    # 定义请求的URL变量
    pcu.setopt(pycurl.URL, URL)
    # 定义请求连接的等待时间
    pcu.setopt(pycurl.CONNECTTIMEOUT, 5)
    # 定义请求超时时间
    pcu.setopt(pycurl.TIMEOUT, 5)
    # 屏蔽下载进度条
    pcu.setopt(pycurl.FORBID_REUSE, 1)
    # 指定HTTP重定向的最大数为1
    pcu.setopt(pycurl.MAXREDIRS, 1)
    # 完成交互后强制断开连接，不重用
    pcu.setopt(pycurl.NOPROGRESS, 1)
    # 设置保存DNS信息的时间为30秒
    pcu.setopt(pycurl.DNS_CACHE_TIMEOUT,30)
    #创建一个文件对象，以“wb”方式打开，用来存储返回的http头部及页面内容
    indexfile = open(os.path.dirname(os.path.realpath(__file__)) + "/html.txt", "wb")
    #将返回的HTTP HEADER定向到indexfile文件
    pcu.setopt(pycurl.WRITEHEADER, indexfile)
    #将返回的HTML内容定向到indexfile文件对象
    pcu.setopt(pycurl.WRITEDATA, indexfile)
    try:
        pcu.perform()    #提交请求
    except Exception as e:
        print("connecion error:"+str(e))
        indexfile.close()
        pcu.close()
        sys.exit()

    NAMELOOKUP_TIME =  pcu.getinfo(pcu.NAMELOOKUP_TIME)    #获取DNS解析时间
    CONNECT_TIME =  pcu.getinfo(pcu.CONNECT_TIME)    #获取建立连接时间
    PRETRANSFER_TIME =   pcu.getinfo(pcu.PRETRANSFER_TIME)    #获取从建立连接到准备传输所消
                                                          #耗的时间
    STARTTRANSFER_TIME = pcu.getinfo(pcu.STARTTRANSFER_TIME)    #获取从建立连接到传输开始消
                                                            #耗的时间
    TOTAL_TIME = pcu.getinfo(pcu.TOTAL_TIME)    #获取传输的总时间
    HTTP_CODE =  pcu.getinfo(pcu.HTTP_CODE)    #获取HTTP状态码
    SIZE_DOWNLOAD =  pcu.getinfo(pcu.SIZE_DOWNLOAD)    #获取下载数据包大小
    HEADER_SIZE = pcu.getinfo(pcu.HEADER_SIZE)    #获取HTTP头部大小
    SPEED_DOWNLOAD=pcu.getinfo(pcu.SPEED_DOWNLOAD)    #获取平均下载速度
    #打印输出相关数据
    print("HTTP状态码:{}" .format(HTTP_CODE))
    print("HTTP状态码：%s" %(HTTP_CODE))
    print("DNS解析时间：%.2f ms"%(NAMELOOKUP_TIME*1000))
    print("建立连接时间：%.2f ms" %(CONNECT_TIME*1000))
    print("准备传输时间：%.2f ms" %(PRETRANSFER_TIME*1000))
    print("传输开始时间：%.2f ms" %(STARTTRANSFER_TIME*1000))
    print("传输结束总时间：%.2f ms" %(TOTAL_TIME*1000))
    print("下载数据包大小：%d bytes/s" %(SIZE_DOWNLOAD))
    print("HTTP头部大小：%d byte" %(HEADER_SIZE))
    print("平均下载速度：%d bytes/s" %(SPEED_DOWNLOAD))
    print("稍等,搜寻该站点DNS地址中......")
    import dns.resolver
    time.sleep(5)
    print("***************************")
    print("共遍历到以下DNS: ")
    print("***************************")
    A = dns.resolver.query(URL, 'A')  # 指定查询类型为A记录
    for i in A.response.answer:  # 通过response.answer方法获取查询回应信息
        for j in i.items:  # 遍历回应信息
            if j.rdtype == 1:  # 避免 "AttributeError: 'CNAME' object has no attribute 'address'" 错误
                print(j.address)
            else:
                pass
    print("当前检测地址为{} ---->DNS解析地址为:".format(URL),j.address)
    #关闭文件及Curl对象
    indexfile.close()
    pcu.close()
