import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd

url = "https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query=%EC%86%8D%EB%B3%B4"

titleList = []
res = req.get(url)
soup = bs(res.text,"lxml")
title = soup.select("a.news_tit")
for i in title:
    titleList.append(i.text)

df = pd.DataFrame(titleList,columns=["제목"])
df.to_csv("data.csv",encoding="euc-kr", index=False)
