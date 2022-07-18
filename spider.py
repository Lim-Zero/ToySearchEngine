from ast import keyword
from unittest import result
import requests
def getserarch(keyword):
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    res = requests.get('https://www.baidu.com/s?wd={}'.format(keyword),headers = header)
    result = res.text
    return result
if __name__=='__main__':
    keyword = input('请输入关键词：')
    res = getserarch(keyword)
    print(res)