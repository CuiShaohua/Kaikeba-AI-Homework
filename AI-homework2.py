# -*- coding: utf-8 -*c-
"""
Created on Tue Jul  9 11:26:49 2019

@author: c00495232
"""

import requests
import re
from bs4 import BeautifulSoup

railways_condition = '''
<a href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%811%E5%8F%B7%E7%BA%BF" target="_blank">北京地铁1号线</a>
<a href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%814%E5%8F%B7%E7%BA%BF" target="_blank">北京地铁4号线</a>
<a href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%815%E5%8F%B7%E7%BA%BF" target="_blank">北京地铁5号线</a>
<a href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%816%E5%8F%B7%E7%BA%BF" target="_blank">北京地铁6号线</a>
<a href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%818%E5%8F%B7%E7%BA%BF" target="_blank">北京地铁8号线</a>
<a href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%819%E5%8F%B7%E7%BA%BF" target="_blank">北京地铁9号线</a>
<a href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%8110%E5%8F%B7%E7%BA%BF" target="_blank">北京地铁10号线</a>
<a href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%8113%E5%8F%B7%E7%BA%BF" target="_blank">北京地铁13号线</a>
<a href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%8115%E5%8F%B7%E7%BA%BF" target="_blank">北京地铁15号线</a>
<a href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%81%E5%85%AB%E9%80%9A%E7%BA%BF" target="_blank">北京地铁八通线</a>
<a href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%81%E6%9C%BA%E5%9C%BA%E7%BA%BF" target="_blank">北京地铁机场线</a>
<a href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%81%E5%A4%A7%E5%85%B4%E7%BA%BF" target="_blank">北京地铁大兴线</a>
<a href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%81%E6%88%BF%E5%B1%B1%E7%BA%BF" target="_blank">北京地铁房山线</a>
<a href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%81%E4%BA%A6%E5%BA%84%E7%BA%BF" target="_blank">北京地铁亦庄线</a>
<a target="_blank" href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%81%E6%98%8C%E5%B9%B3%E7%BA%BF">北京地铁昌平线</a>
<a target="_blank" href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%8116%E5%8F%B7%E7%BA%BF">北京地铁16号线</a>
<a target="_blank" href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%81S1%E7%BA%BF">北京地铁S1线</a>
<a target="_blank" href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%812%E5%8F%B7%E7%BA%BF">北京地铁2号线</a>
<a target="_blank" href="/item/%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%817%E5%8F%B7%E7%BA%BF">北京地铁7号线</a>
'''

pattern1  = r"/.+%BF"
pattern2  = r"北京地铁\w+"

rails_url_sets = {}
for line in railways_condition.split("\n"):
    if not line: continue
    rail = re.findall(pattern2, line)[0]
    #print(rail)
    rail_url = "https://baike.baidu.com" + re.findall(pattern1, line)[0]
    rails_url_sets[rail] =  rail_url
#print(rails_url_sets)

"""
扒地铁站数据
"""

user_agent ='Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
headers = {'User_Agent': user_agent}
sessions = requests.session()
sessions.headers = headers

i =0

for rail in rails_url_sets:
    Rails_url = rails_url_sets[rail]
    content = sessions.get(Rails_url,allow_redirects=True)
    content.encoding ='utf-8'
    soup = BeautifulSoup(content.text, 'lxml')
    print("-"*80)
    ret = soup.select('body > div.body-wrapper > div.content-wrapper > div > div.main-content > table')
    if ret:
        print(ret)
    else:
        i += 1
print(i)









