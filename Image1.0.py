# -*- coding:utf-8 -*-

import urllib
import urllib2
import re
          
def getHtml(url,params):
  # 将参数变换为网址中参数传递的方式
  data = urllib.urlencode(params)
  
  # 这里使用的是post的方式，如果想用get的方式，需url + '？' + data
  request = urllib2.Request(url, data)
  
  try:
    response = urllib2.urlopen(request)
  except urllib2.URLError:
    print e.reason
  
  # read() , readline() , readlines() , fileno() , close() ：这些方法的使用方式与文件对象完全一样;
  # info()：返回一个httplib.HTTPMessage 对象，表示远程服务器返回的头信息
  # getcode()：返回Http状态码。如果是http请求，200表示请求成功完成;404表示网址未找到；
  # geturl()：返回请求的url
  html = response.read()
  return html
  
def getImagesUrl(html):
  # 自己写的，有问题，最终将 http://hdsia/df/fd/df.jpg,http://sdf/sfda/sfd.png,http://dsf/t/er.jpg 这种串当做一个输出
  # instr = r"http://.*/.*\.jpg"
  
  instr = r'src="(.+?\.jpg)"'
  pattern = re.compile(instr)
  
  # 有关正则表达式中的其他方法，参考 http://python.jobbole.com/81346/
  images = re.findall(pattern, html)
  return images

def retrieveImages(images):
  i = 1
  for image in images:
    # urllib.urlretrieve(url[, filename[, reporthook[, data]]])
    # 参数说明：
    # url：外部或者本地url
    # filename：指定了保存到本地的路径（如果未指定该参数，urllib会生成一个临时文件来保存数据）；
    # reporthook：是一个回调函数，当连接上服务器、以及相应的数据块传输完毕的时候会触发该回调。我们可以利用这个回调函数来显示当前的下载进度。
    urllib.urlretrieve(image, "d:/python grap/%s.jpg" %i)
    i = i + 1

def main():
  url = "http://image.baidu.com/search/index"
  params = {'tn':'baiduimage','ipn':'r','ct':'201326592','cl':'2','lm':'-1',
          'st':'-1','sf':'1','fmq':'1450429988847_R','ic':'0','nc':'1',
          'showtab':'0','fb':'0','s':'0','face':'0','st':'-1','ie':'utf-8',
          'word':'%E6%AC%A7%E7%BE%8E%E5%A4%B4%E5%83%8F#z=0','face':'0','istype':'2'}
  html = getHtml(url,params)
  images = getImagesUrl(html)
  retrieveImages(images)
          
if __name__ == '__main__':
    main()