#!/bin/bash
"""
求求各位大哥不要解我的包!!!
我就是一个小白整合一下程序嘻嘻嘻.
不过解了的也没有问题....# 来自于二次元的问候！
解包的大哥麻烦告诉一下: QQ 3441789878
采用pyinstaller编译
python pyinstaller.py --onefile /tmp/hello.py
别问 问就是只会print
"""
print("""#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
# Name:       Google Search V1
# Purpose: Google search will return to the mainland
#
# Author:      Administrator
#
# Created:     2020-06-25
# Copyright:   Linux-Pop_OS
# Licence:     Google search will return to the mainland
#-------------------------------------------------------------------------------""")

# 判断是否同意许可协议
import win32api,win32con

win32api.MessageBox(0, """
    本软件许可协议通知   
1.本软件只用于学术交流无其他用途
2.禁止一切人用本软件进行盈利！！！
3.同不同意许可协议,你自己摸索....
4.生成Google.txt位于当前目录""", "使用须知",win32con.MB_OK)
win32api.MessageBox(0, """
    本软件许可协议通知   
1.优化搜索速度
2.更新弹窗提示框,兼容性使用win32
3.更新云数据库资源
4.修复前期判断失败bug
""", "更新内容",win32con.MB_OK)
# 程序执行开始
userin = int(input("是否同意本软件许可协议(1/2)："))
if userin == int(1):
    print("来咯来咯,他们真的来喽~~~")
    # 读取硬件信息
    print("读取本机硬件信息中.....请稍等")
    import time
    time.sleep(3) # 以s秒为单位,程序睡眠多少秒后执行下一步
    # 开始获取计算机信息
    import socket
#获取计算机名称
    hostname=socket.gethostname()
    print("当前主机名称为: {}".format(hostname))
#获取本机IP
    ip=socket.gethostbyname(hostname)
    print("当前IP地址为: {}".format(ip))
    print('读取成功')
# 同步网络数据库
    scale = 10
    print("------开始同步www.micomint.top数据库------")
    for i in range (scale+1):
                a = '*' * i 
                b = '.' * (scale - i)
                c = (i/scale)*100
                print("{:^3.0f}%[{}->{}]".format(c,a,b))
                time.sleep(0.1)
    print("--------------同步完成---------------------")
# 开始写入到C盘桌面
    import datetime
    nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("当前谷歌搜索镜像更新时间为：{}".format(nowTime))
    mytxt=open('Google.txt', mode = 'a',encoding='utf-8')
    print("""Google Search Image
https://soo.panda321.com/
https://google.9sr.ltd/
https://google.zenith.workers.dev
http://g.dosnav.com
https://goo.gle.workers.dev
https://www.sanzhima.com
https://www.enow.com
https://www.aolsearch.com
https://lite.qwant.com
https://www.gosearchresults.com
https://seeres.com
https://stats.searx.xyz
https://sou.wvw.win/
https://g.louqunhua.top/
http://206.189.135.241
https://g.zmirrordemo.com/
https://so.xilesou.287865.com
https://g3.luciaz.me/
http://ge1.azurewebsites.net/
https://g.wangcb.com/
https://2.52qu.xyz/
https://gogoo.ml/
https://goo.gle.workers.dev/
http://ggso.rinue.top/
https://googles.now.sh/
https://sou.wvw.win/
https://so.suo.fit/
https://ug1.hub-sci.net/
https://gg0.chn.moe/
http://sanzhima.com/
https://goo.gle.workers.dev/
https://gg1.chn.moe/
http://google.lyz810.com/
https://google.heng07.com/
https://uifox.cc/
https://gug1.icu/
https://goobe.io/
https://sougou.se/
谷歌学术镜像（google scholar）
http://so.hiqq.com.cn/
https://s0.unllu.com/
https://sc.panda321.com/
https://zz.glgoo.top/scholar
https://scholar.123admin.com/
https://b.glgoo.top/scholar/
https://xs.zb-welding.com/scholar/
https://g3.luciaz.me/extdomains/scholar.google.com/
维基百科
https://g.zmirrordemo.com/wiki
https://w.upupming.site/wiki/
https://wikipedia.sogou.se/wiki/
https://zh.wikis.website/
https://www.wikizero.com/zh/
http://wikipedia.moesalih.com/
谷歌学术镜像网站
https://xue.glgoo.net
https://xue.glgoo.org/
https://f.glgoo.top/
https://scholar.glgoo.org/
https://xues.glgoo.com/
https://xs.glgoo.top/scholar/
其它替代品
1、https://www.qwant.com （qwant搜索引擎，法国的一款搜索引擎）
2、https://nova.rambler.ru （俄罗斯的一款搜索引擎，由谷歌驱动）
3、https://sg.search.yahoo.com/ （雅虎）
4、https://search.avira.com/ （德国的一款搜索引擎）
5、https://www.ecosia.org/ （德国的一款搜索引擎，具有公益性）
6、https://suche.gmx.net （德国的一款搜索引擎）
7、https://duckduckgo.com （美国的一款搜索引擎）""", file=mytxt)
    mytxt.close()
    print("----->>>>>获取Google镜像成功----->>>>>>")
    print("已经打印到本地桌面Google.txt文件,请查收")
    print("""感谢大家的支持使用本软件,如果搜索镜像失效请网上自行寻找,关于这一点我非常的抱歉
收集不易 且行且珍惜 联系方式: Administrator 做好事不留名嘻嘻嘻~~~~""")
    print("")
    time.sleep(5) 


    
elif userin == int(2):
    print("未同意许可协议已经退出")
    print('\n'.join([''.join([('AndyLove'[(x - y) % 8] if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (
    x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(15, -15, -1)]))
    exit(0)
else:
    print("无效选项,请勿尝试使用其他数字或者字符特殊字符.")
    exit(1)
