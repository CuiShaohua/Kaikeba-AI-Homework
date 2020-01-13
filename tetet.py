'''
a = [1,2,3,4,5,6,7,8]
b = [3,5]
def Arr_split(a,b):
    num_arr1 = []
    num_arr2 = []
    num_arr3 = []
    for i in a:
        num_arr1.append(i)
        #print(num_arr1)
        if num_arr1[-1] in b:
            num_arr1.pop()
            #b.pop(0)
            num_arr2 += [num_arr1.copy()]  # 可变对象赋值果然是个坑
            #print(num_arr2)
            num_arr1.clear()
            b.pop(0)
        elif not b:
            num_arr2 += [a[a.index(i):]]
            return num_arr2

print(Arr_split(a,b))
'''
'''
1
body > div > div.content > div.sub_map > div.line_content > div:nth-child(43) > a
body > div > div.content > div.sub_map > div.line_content > div:nth-child(44) > div

body > div > div.content > div.sub_map > div.line_content > div:nth-child(45)
body > div > div.content > div.sub_map > div.line_content > div:nth-child(46)
body > div > div.content > div.sub_map > div.line_content > div:nth-child(70) > a

body > div > div.content > div.sub_map > div.line_content > div:nth-child(94) > a
'''
'''
import requests
from bs4 import BeautifulSoup
import lxml
import re
num = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

user_agent ='Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
headers = {'User_Agent': user_agent}
sessions = requests.session()
sessions.keep_alive = False
url = 'https://www.bjsubway.com/station/xltcx/'
#url = 'https://www.bjsubway.com/e/action/ListInfo/?classid=39&ph=1'
sessions.headers = headers
content = sessions.get(url,allow_redirects=True,verify = False)
content.encoding = 'gbk'
soup = BeautifulSoup(content.text, 'lxml')

statin_re = r'(>(\w+))'
try:
    rail_station_with_tag= str(soup.select('body > div > div.content > div.sub_map > div.line_content > div:nth-child(45) > a')[0])
except IndexError:
    rail_station_with_tag = rail_station_with_tag= str(soup.select('body > div > div.content > div.sub_map > div.line_content > div:nth-child(45) ')[0])

station = re.findall(statin_re, rail_station_with_tag)[0][1]
print(rail_station_with_tag)
print(station)

'''

import os
import json
a = {'a':1,'b':2}

#files =  os.walk('./')
for root, dirs, files in os.walk(".", topdown=False):
    if 'subway.txt' not in files:  # 这句到底是不是查当前目录
        print(False)
        json_dict = json.dumps(a)
        f = open('subway.txt', 'w')
        f.write(json_dict)
        f.close()
    else:
        f = open('subway.txt', 'r')
        json_dict = f.read()
        js_data = json.loads(json_dict)
        print(js_data, type(js_data))
        f.close()
    print(1)





    '''
import json
dict_1={'val_loss':handle_loss,'val_acc':handle_acc,'val_precision':handle_precision,'val_recall':handle_recall,'val_fmeasure':handle_fmeasure,'val_top_3_categorical_accuracy':handle_top_3_categorical_accuracy}

jsObj = json.dumps(dict_1)

fileObject = open(r'D:\code_python\matrix_dic2.json', 'w')

fileObject.write(jsObj)

fileObject.close()
    
    '''



