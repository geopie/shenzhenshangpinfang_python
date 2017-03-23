#coding=utf-8
import sys
import requests
from bs4 import BeautifulSoup as bs
import re
from Tkinter import *


reload(sys)
sys.setdefaultencoding('utf-8')

url = 'http://ris.szpl.gov.cn/credit/showcjgs/ysfcjgs.aspx?cjType=0' #网址
html1 = requests.get(url)

datefile = bs(html1.text,'lxml')
date = datefile.select("#lblCurTime1")
date = date[0].text

chengjiaoxiaoji = datefile.select("#clientList1 > tr:nth-of-type(13) > td:nth-of-type(2)")#python是不支持上面的选择器的部分语法的，比如nth或者tbody,需要进行修改。
chengjiaoxiaoji = chengjiaoxiaoji[0].text

junjia = datefile.select("#clientList1 > tr:nth-of-type(13) > td:nth-of-type(4)")
junjia = junjia[0].text
junjia = junjia.replace("\r\n","")
junjia = junjia.strip()   #去除前后空格

file = open('quanshidata.txt','a')
line =   '\n' + date + ' ' + chengjiaoxiaoji + ' ' + ' ' + junjia + ' '
file = file.write(line)


post_data = {
    'ctl00$ContentPlaceHolder1$scriptManager1':'ctl00$ContentPlaceHolder1$updatepanel1|ctl00$ContentPlaceHolder1$hypBa',
    '__EVENTTARGET':'ctl00$ContentPlaceHolder1$hypBa',
    '__EVENTARGUMENT':'',
    '__LASTFOCUS':'',
    '__VIEWSTATE':'skfdEWTmJhePlWPDKHCMaCkp3h0KkOCfdX90/5wg+RAokzisdlTLvAR30e1ORoIHt7Jri/qoWu2r06S8C67EAtIZ4R4g6fxTXEpfMpGi2B4bg55Jlw1kK9Q6C0f+6l4s/uI/3m2G1u6KTRj9SxvfyU7JIrxNm/FrRQOO5pQXu6Z4rcs46yMCJ1QG5e+l04w4YtBEmQFtKLmI7ZOkZhJo1DTb5X0ep3OQduSRJla/hcCh1OVWJ1w3j1r+xkqxLU+4uPqWh+bNLQBfIpVQ0m5MdSLTrdUbcgKC2YYDPxZjPgQ0XRjoIxN//myE1dBF1JXJAq/6ZDigiMMNVc5cZFmE4Vno+4E/yq2LCrhDg21/3RMXXzICVHk4Pk4azfpskfNuLeYi6tCOvsO9Xs4ThKjUuBOcfHlyX4VxwB/ss3FciJ9k+ADH+Ljbd+IVPGbAfWthGGS20iDHQPac9BBFNyEsFQdyq3ktjQYYpS4tmlwxKM2Sb17mWVHzyLcTIdJl+XxU+kjMupl2ltQU2n/s9SU4NnoP/U32kt9Lh3GhebGEJuOaL+Xfh5Ov/AEuEXDKtXs+L+f9hFZxsHyXrWDAPYXTMiaWSis8hZMrJy4XMdvAZ5pJTyv46U8Gl/eENWARJrjc3XJDETfUvt+p5K13dWEcmUvpyfrmbO8FIICZQxzIoRYhswZpDPgZbGbfx7WZQt7oSQaALtD4mWx/rKSd1CGPMVyT5XQ3tlmm8b3I3n/TiKVPc8xQyYa3cU/NBElaXl50+zp8XUNOMEevp2mfqvMqtyanCSkvfET+ExdYoQEcTdMqR/3sIAHT9PH2rKxOF+zqnCo5JFKnVqR4nYT1MPpaS73Fh24he5z32nEyLwNMlasXUvD3GH04/z8VdGWD8XaR8DODH/M7EPNFLKXUAE++lbJLrhfDGN2Td+I4iqFQrbOFB5uctcLC8gME1sl4Br/y5evQDw1oQxan7misJUcJwYLp5RcOwvx0fJP7MkQIRvjETH13M70rPa8LI4bBikVHNB03COVQfJRlMww22oNn+jpwReFBR7RTyqJ+hoO1KNmMwCFCTfCuXBc4zD3qL2tah0MnQZvqn8xz7dpFPIChVl5gweEbE/fIJ81BFIP9rxklLFyy5tujVLko4Mpq/FLqGqplAFhZi4Qd5gtMDNQzMgO3S83R3GGPqm+NjIv3REabQwng0VkohEPpIr8bd6K0+o4KLN3G6xEf7hHS3uwBijmUGwQ+/QlhCI1CnBeAKH3oM5LCNnEG88J3vUzkmSrU2YT6yj0DZ7iLPgiuuB3AXoXuC1vBe/yYE/PAL9ySRS7C5A7+y3CGXVwdviFHO4xntYRPeRjABJ4Ch0MCqsQdB2jo4/p2F0e6Ckp9nCdtXY63h8uCXhKRHLX6pzV//kBwA5OnmmDt59WUnAtl/7QlYE0jUvzZGAIp4x0+jBt1xKNtuLPAgiwAiwQVZLMVcQ4t8q8VfdDl6ergOZush7JImqMsXIXbIL8o3zHqB+ItzN3l+wN6Ha2yAryoNPD7VPyCQsz8L09brVsJI8G+q2cwt8SM3r5RwM56CFDGdKLxILKklvMH+UBQgXdi4fxeOYv/4KdqRm2tKx9j0l4TBG3OMbE+UQPFNXy2izO8800zzWqVqcsZk98FuoZCAdYdfqqIak17E9cbadKc00iOk9R86oDBy5hpsyk1Qn9Bu6yXAFQbki5SHevmFgBjmVB8n50C3gFTKg==',
    '__VIEWSTATEGENERATOR':'9030114A',
    '__VIEWSTATEENCRYPTED':'',
    '__EVENTVALIDATION':'YfYaEAdPS/wCH3RLG4cJb/TeABb4K9qlyWaIDk8FK50pryF5R10WJcSMYP3+H1EnbtXhWkyarx2ORzYE9csE94BsiUuRt6coVM6BzswqXSHIJHlI3oZfTO5xu0j9nzEcv3wvb+t5seGdT8Gfw9FXSFuEIHwmQf4PSGgWBE9aLfiTuXpw',
    'ctl00$ContentPlaceHolder1$radSelect':'0',
}
html2 = requests.post(url,data = post_data)

datefile = bs(html2.text,'lxml')
#date = datefile.find_all(id="lblCurTime1")
date = datefile.select("#lblCurTime1")
date = date[0].text

#clientList1 > tbody > tr:nth-child(11) > td:nth-child(2)

chengjiaoxiaoji = datefile.select("#clientList1 > tr:nth-of-type(11) > td:nth-of-type(2)")#python是不支持上面的选择器的部分语法的，比如nth或者tbody,需要进行修改。
chengjiaoxiaoji = chengjiaoxiaoji[0].text

#clientList1 > tbody > tr:nth-child(11) > td:nth-child(4)
junjia = datefile.select("#clientList1 > tr:nth-of-type(11) > td:nth-of-type(4)")
junjia = junjia[0].text
junjia = junjia.replace("\r\n","")
junjia = junjia.strip()   #去除前后空格


file = open('baoandata.txt','a')
line =  '\n' + date + ' ' + chengjiaoxiaoji + ' ' + ' ' + junjia + ' '


# 对象file的write方法将字符串line写入file中
file = file.write(line)

root = Tk()
root.title("深圳商品房信息 v1.0")
root.geometry('600x200')
l = Label(root, text="数据获取成功^_^", font=("Arial", 12), width=30, height=100)
l.pack(side=BOTTOM)  #这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
root.mainloop()