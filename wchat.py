#import os 
#print("正在爬取Requests库....")
#pip_install_re = os.system("pip install requests")


# 导入requests库访问百度
#import requests
#r = requests.get("http://www.baidu.com")
#r.status_code 
#print("当前网页返回的状态码是:",r.status_code)
#print("当前返回的状态请求:",type(r))
#print("当前页面的头部信息:",r.headers)
#print("当前页面的默认编码为:",r.encoding)
#print("当前页面备选的编码模式为:",r.apparent_encoding)
# r.encoding = "utf-8"
# print(r.text)
#def gethtmlurl(url):
#    try:
#        r = requests.get(url,timeout=30)
#        r.raise_for_status() # 如果状态不是200,引发HTTPError错误
#        r.encoding = r.apparent_encoding
#        return r.text
#    except:
#        return "产生异常"
#if __name__ == "__main__":
#    url = "http://www.baidu.cosm"
#    print(gethtmlurl)

# Head请求
'''
import requests
   r = requests.head("https://www.baidu.com/get")
a = r.headers
b = r.text
print(a,b)
'''
# Post请求 去更新资源提交字典
#import requests
#payload = {"Key1":"Values2","Key3":"Values4"}
#r = requests.post("http://httpbin.org/post",data = payload)
#print(r.text)
# 向URL提交一个ABC
#import requests
#r = requests.post("http://httpbin.org/post",data = "ABC")
#print(r.text)
#import requests
#payload = {"Key1":"Values2","Key3":"Values4"}
#r = resquests.post("http://www.baidu.com/put",data = payload)
#print(r.text)

#import requests
#kv = {"1":"2"}
#r = requests.request("GET","http://python123.io/ws",params=kv)
#print(r.url)

#import requests
#r = requests.get("http://192.168.232.118")
#r.status_code
#print(r.status_code)
import requests
url = "https://item.jd.com/1214883.html"
try:
    r = requests.get(url)
    r.rails_for_status()
    r.encoding = r.apparent_conding
    print(r.text)
except:
    print("失败")
    print(r.status_code)
