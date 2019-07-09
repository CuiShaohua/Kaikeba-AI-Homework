# -*- coding: utf-8 -*c-
"""
Created on Tue Jul  9 11:26:49 2019

@author: c00495232
"""

'''

'''

import requests

Rails_url = "https://baike.baidu.com/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%81/408485"
user_agent ='Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
sessions = requests.session()
headers = {'User_Agent': user_agent}
sessions.headers = headers
content = sessions.get(Rails_url,allow_redirects=True)
content.encoding ='utf-8'
#print(content.text)

from bs4 import BeautifulSoup

soup = BeautifulSoup(content.text, 'lxml')

'''
body > div.body-wrapper > div.content-wrapper > div > div.main-content > table:nth-child(65) > tbody > tr:nth-child(2) > td:nth-child(1) > a

body > div.body-wrapper > div.content-wrapper > div > div.main-content > table:nth-child(65) > tbody > tr:nth-child(4) > td:nth-child(1) > a

body > div.body-wrapper > div.content-wrapper > div > div.main-content > table:nth-child(65) > tbody > tr:nth-child(6) > td:nth-child(1) > a

body > div.body-wrapper > div.content-wrapper > div > div.main-content > table:nth-child(65) > tbody > tr:nth-child(8) > td:nth-child(1) > a

body > div.body-wrapper > div.content-wrapper > div > div.main-content > table:nth-child(65) > tbody > tr:nth-child(42) > td:nth-child(1) > a

/html/body/div[4]/div[2]/div/div[2]/table[3]/tbody/tr[6]/td[1]/a
'''
#href = soup.select('body > div.body-wrapper > div.content-wrapper > div > div.main-content > table:nth-of-type(65) > tbody > tr:nth-child(2) > td:nth-of-type(1) > a')

href = soup.select('body > div.body-wrapper > div.content-wrapper > div > div.main-content > table')


railways_condition = '''
<a href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%811%E5%8F%B7%E7%BA%BF" target="_blank">北京地铁1号线</a>
<a target="_blank" href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%812%E5%8F%B7%E7%BA%BF">北京地铁2号线</a>
<a href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%814%E5%8F%B7%E7%BA%BF" target="_blank">北京地铁4号线</a>
<a href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%815%E5%8F%B7%E7%BA%BF" target="_blank">北京地铁5号线</a>
<a href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%816%E5%8F%B7%E7%BA%BF" target="_blank">北京地铁6号线</a>
<a target="_blank" href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%817%E5%8F%B7%E7%BA%BF">北京地铁7号线</a>
<a href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%818%E5%8F%B7%E7%BA%BF" target="_blank">北京地铁8号线</a>
<a href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%819%E5%8F%B7%E7%BA%BF" target="_blank">北京地铁9号线</a>
<a href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%8110%E5%8F%B7%E7%BA%BF" target="_blank">北京地铁10号线</a>
<a href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%8113%E5%8F%B7%E7%BA%BF" target="_blank">北京地铁13号线</a>
<a href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%8115%E5%8F%B7%E7%BA%BF" target="_blank">北京地铁15号线</a>
<a target="_blank" href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%8116%E5%8F%B7%E7%BA%BF">北京地铁16号线</a>
<a target="_blank" href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%81S1%E7%BA%BF">北京地铁S1线</a>
<a href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%81%E5%85%AB%E9%80%9A%E7%BA%BF" target="_blank">北京地铁八通线</a>
<a href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%81%E6%9C%BA%E5%9C%BA%E7%BA%BF" target="_blank">北京地铁机场线</a>
<a href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%81%E5%A4%A7%E5%85%B4%E7%BA%BF" target="_blank">北京地铁大兴线</a>
<a href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%81%E6%88%BF%E5%B1%B1%E7%BA%BF" target="_blank">北京地铁房山线</a>
<a href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%81%E4%BA%A6%E5%BA%84%E7%BA%BF" target="_blank">北京地铁亦庄线</a>
<a target="_blank" href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%81%E6%98%8C%E5%B9%B3%E7%BA%BF">北京地铁昌平线</a>
'''

print(href)









