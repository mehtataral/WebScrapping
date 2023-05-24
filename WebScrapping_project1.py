# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 13:46:34 2022

@author: user
"""

# Beautiful Soup is a library that makes it easy to scrape information from web pages.
# Requests HTTP Library
# ~~~~~~~~~~~~~~~~~~~~~

# Requests is an HTTP library, written in Python, for human beings.
# Basic GET usage:    b

# .find() - it is used for searching first element 
# .find_all() - it gives all element from the HTML file    


import requests
import bs4
import pandas as pd

# url = input("Enter your url")
page =1

while page  !=11:
    path = f"https://books.toscrape.com/catalogue/category/books_1/page-{page}.html" 
    #used string format ...which passes page number in this link
    # https://books.toscrape.com/catalogue/category/books_1/page-2.html
    print("****link is {} {}****".format(page,path))
    respones =requests.get(path)
    print(respones)
    print(respones.status_code)
    page = page +1 
    if respones.status_code == 200:
        print("Connection Successfull")
    else:
        print("Connection Failed")
        
    filename ="web_scrap_project4.html"
    bs =bs4.BeautifulSoup(respones.text,"html.parser")
    print(bs)
    print(bs.text)
    formatted_data =bs.prettify()
    print(formatted_data)

    ol = bs.find('ol')
    articles = ol.find_all('article', class_='product_pod')
    articles
    articles[0].text
    articles[1].text
    articles[2].text
    articles[3].text
    books = []

    for article in articles:
        image = article.find('img')
        # print(image)
        # print(image.text)
        title = image.attrs['alt']
        print(title)
        # print(title.text)
        starTag = article.find('p')
        print(starTag)
        print(starTag.text)
        star = starTag['class'][1]
        star
        price = article.find('p', class_='price_color').text
        price
        price = float(price[2:])
        price
        books.append([title, star, price])
        

df = pd.DataFrame(books, columns=['Title', 'Star Rating', 'Price'])
df.to_csv('books.csv')

df

#******************************************************************************

import requests
import bs4
import pandas as pd
import scrapy


# # url = input("Enter your url")
# page =2

# while page  !=11:
#     path = f"https://www.amazon.in/s?k=mixer+grinder&page={page}&qid=1671004628&sprefix=mixer%2Caps%2C709&ref=sr_pg_{page}" 
#     #used string format ...which passes page number in this link
#     # https://www.amazon.in/s?k=mixer+grinder&page=4&qid=1671004628&sprefix=mixer%2Caps%2C709&ref=sr_pg_4
#     print("****link is {} {}****".format(page,path))
#     respones =requests.get(path)
#     print(respones)
#     print(respones.status_code)
#     page = page +1 
#     if respones.status_code == 200:
#         print("Connection Successfull")
#     else:
#         print("Connection Failed")


#     filename ="web_scrap_project3.html"
#     bs =bs4.BeautifulSoup(respones.text,"html.parser")
#     print(bs)
#     print(bs.text)
#     formatted_data =bs.prettify()
#     print(formatted_data)

#     Title = bs.find_all("span",class_ = "a-size-medium a-color-base a-text-normal")
#     print(Title)

url = input("Enter your url")
path = "https://www.amazon.in/s?k=washing+machine&crid=KN32DTPODVT5&sprefix=wash%2Caps%2C236&ref=nb_sb_ss_ts-doa-p_2_4"
# https://www.cricbuzz.com/cricket-series/3961/icc-mens-t20-world-cup-2022/stats
respones =requests.get(path)
print(respones)
print(respones.status_code)

if respones.status_code == 200:
    print("Connection Successfull")
else:
    print("Connection Failed")
    
    
filename ="web_scrap_project3.html"
bs =bs4.BeautifulSoup(respones.text,"html.parser")
print(bs)
print(bs.text)
formatted_data =bs.prettify()
print(formatted_data)

#------------------------------ Basic Tag ------------------------------------
heading = bs.find_all("span")
print(heading)
print(len(heading))

heading = bs.find("span")
print(heading)
print(heading.text)
print(len(heading))

heading = bs.find_all("div")
print(heading)
print(len(heading))

heading = bs.find("div")
print(heading)
print(heading.text)
print(len(heading))

heading = bs.find_all("tr")
print(heading)
print(len(heading))
#------------------------------ Most Runs ----------------------------
row = bs.find_all(class_ ="cb-srs-stats-td text-right")
print(row)
print(len(row))

row = bs.find_all("tr" ,{"class" :"cb-srs-stats-tr"})
print(row)
print(len(row))

print(row[0].text)
print(row[1].text)
print(row[2].text)
print(row[3].text)
print(row[4].text)

col = bs.find_all("td",{"class":"cb-srs-stats-td text-right"})
print(col)
print(len(col))

print(col[0].text)
print(col[1].text)
print(col[2].text)
print(col[3].text)
print(col[4].text)
print(col[5].text)
print(col[6].text)
print(col[7].text)
print(col[8].text)
print(col[9].text)  

#Higest Score

row1 = bs.find_all("a",{"href ng-class":" cb-stats-lft-tab-active"})
print(row1)

bs.find('a', {'href ng-class':"cb-stats-lft-tab-active"})['href']


data_list =[]
for tr in row:
    td = tr.find_all("td")
    rows=[i.text for i in td]
    data_list.append(rows)

df = pd.DataFrame(data_list,columns =["POS","PLAYER","MATCHES","INNS","RUNS","AVG","SR","4s","6s"])
df
df.drop(0,inplace=True)
df.reset_index(drop=True)
df.to_csv(r"C:\Users\user\Documents\Taral\AI\WebScrapping\data_cricket1.csv")






























#*****************************************************************************
import requests
import bs4
import pandas as pd


url = input("Enter your url")
path = "https://www.cricbuzz.com/cricket-series/3961/icc-mens-t20-world-cup-2022/stats"
# https://www.cricbuzz.com/cricket-series/3961/icc-mens-t20-world-cup-2022/stats
respones =requests.get(path)
print(respones)
print(respones.status_code)

if respones.status_code == 200:
    print("Connection Successfull")
else:
    print("Connection Failed")
    
    
filename ="web_scrap_project3.html"
bs =bs4.BeautifulSoup(respones.text,"html.parser")
print(bs)
print(bs.text)
formatted_data =bs.prettify()
print(formatted_data)

#------------------------------ Basic Tag ------------------------------------
heading = bs.find_all("span")
print(heading)
print(len(heading))

heading = bs.find("span")
print(heading)
print(heading.text)
print(len(heading))

heading = bs.find_all("div")
print(heading)
print(len(heading))

heading = bs.find("div")
print(heading)
print(heading.text)
print(len(heading))

heading = bs.find_all("tr")
print(heading)
print(len(heading))
#------------------------------ Most Runs ----------------------------
row = bs.find_all(class_ ="cb-srs-stats-td text-right")
print(row)
print(len(row))

row = bs.find_all("tr" ,{"class" :"cb-srs-stats-tr"})
print(row)
print(len(row))

print(row[0].text)
print(row[1].text)
print(row[2].text)
print(row[3].text)
print(row[4].text)

col = bs.find_all("td",{"class":"cb-srs-stats-td text-right"})
print(col)
print(len(col))

print(col[0].text)
print(col[1].text)
print(col[2].text)
print(col[3].text)
print(col[4].text)
print(col[5].text)
print(col[6].text)
print(col[7].text)
print(col[8].text)
print(col[9].text)  

#Higest Score

row1 = bs.find_all("a",{"href ng-class":" cb-stats-lft-tab-active"})
print(row1)

bs.find('a', {'href ng-class':"cb-stats-lft-tab-active"})['href']


data_list =[]
for tr in row:
    td = tr.find_all("td")
    rows=[i.text for i in td]
    data_list.append(rows)

df = pd.DataFrame(data_list,columns =["POS","PLAYER","MATCHES","INNS","RUNS","AVG","SR","4s","6s"])
df
df.drop(0,inplace=True)
df.reset_index(drop=True)
df.to_csv(r"C:\Users\user\Documents\Taral\AI\WebScrapping\data_cricket1.csv")

#HIGHEST RUN SCORE
if respones.status_code == 200:
    print("Connection Successfull")
else:
    print("Connection Failed")
    
highes_score =bs.find_all("tr",{"class":"cb-srs-stats-tr"})
highes_score
highes_score[].text

# data_list
# data =open(r"C:\Users\user\Documents\Taral\AI\WebScrapping\data_cricket1.csv","a")
# print(data)

# data_list =[]
# for x in range(len(rank)):
#     print(rank[x].text)
#     data.write(rank[x].text)
#     data.write("\n")
    
#     data_list.append(rank[x].text)

# data.close()
# df =pd.read_csv(r"C:\Users\user\Documents\Taral\AI\WebScrapping\data_cricket1.csv")
# df




import pandas as pd    
df = pd.DataFrame({"Data":data_list})
df[["a","b","c"]] =df["Order ID"].str.split('-',2,expand = True)

print(df)
df[["POS","PLAYER","MATCHES","INNS","RUNS","AVG","SR","4s","6s"]] =df.Data.str.split(9)

df[["POS","PLAYER","NAME","MATCHES","INNS","RUNS","AVG","SR","4s","6s"]] =df[" POS PLAYER MATCHES INNS RUNS AVG SR 4s 6s "].str.split(' ',9,expand = True)
df.info()
df
df.drop(0,inplace =True)
df
df.drop("Data",axis ="columns",inplace= True)
df




























import requests
import bs4

url = input("Enter your url")
path = "https://www.google.com/search?rlz=1C1CHBF_enIN987IN987&tbs=lf:1,lf_ui:14&tbm=lcl&q=list+of+python+course+in+mumbai&rflfq=1&num=10&sa=X&ved=2ahUKEwjBoPm06OT7AhVzVXwKHc5CCtUQjGp6BAhEEAI&biw=1600&bih=789#rlfi=hd:;si:;mv:[[19.5091110210946,74.15438603925779],[18.686373192276214,72.53390264082029],null,[19.098253427746624,73.34414434003904],10]"
# https://www.google.com/search?rlz=1C1CHBF_enIN987IN987&tbs=lf:1,lf_ui:14&tbm=lcl&q=list+of+python+course+in+mumbai&rflfq=1&num=10&sa=X&ved=2ahUKEwjBoPm06OT7AhVzVXwKHc5CCtUQjGp6BAhEEAI&biw=1600&bih=789#rlfi=hd:;si:;mv:[[19.5091110210946,74.15438603925779],[18.686373192276214,72.53390264082029],null,[19.098253427746624,73.34414434003904],10]response = requests.get(url)
respones =requests.get(path)
print(respones)
print(respones.status_code)

if respones.status_code == 200:
    print("Connection Successfull")
else:
    print("Connection Failed")
    
    
filename ="web_scrap_project2.html"
bs =bs4.BeautifulSoup(respones.text,"html.parser")
print(bs)
print(bs.text)
formatted_data =bs.prettify()
print(formatted_data)

#------------------------------ Title Tag ------------------------------------
heading = bs.find_all("span",class_ = "RDApEe YrbPuc")
print(heading)

heading = bs.find("span")
print(heading)
print(heading.text)




#------------------------------ Institute Name Tag ----------------------------

class_name =bs.find_all(class_="rllt__details")
print(class_name)

class_name =bs.find("div", {"class": "b_factrow"})
print(class_name)

class_name =bs.find_all(class_="rllt__details")
print(class_name)

print(class_name[0].text)
print(class_name[1])
print(class_name[2])
print(class_name[3])
print(class_name[4])

list_institute =[]
print(len(class_name))

for x in range(len(class_name)):
    print(class_name[x].text)
    print("****************************")


# *****************************************************************************

import requests
import bs4

url = input("Enter your url")
# https://www.sulekha.com/python-programming-training/mumbai
response = requests.get(url)
print(response)
print(response.status_code)

if response.status_code == 200:
    print("Connection Successfull")
else:
    print("Connection Failed")
    
    
filename ="web_scrap_project1.html"
bs =bs4.BeautifulSoup(response.text,"html.parser")
print(bs)
print(bs.text)
formatted_data =bs.prettify()
print(formatted_data)

#------------------------------ Title Tag ------------------------------------
heading = bs.find("h1")
print(heading)
print(heading.text)

#------------------------------ Institute Name Tag ----------------------------
class_name =bs.find_all(class_ ="title-xlarge") #not useful
class_name =bs.find_all("h3", {"class": "title-xlarge"})
class_name =bs.find_all("div", {"class": "name"})
class_name =bs.find_all("h3", {"class": "title-xlarge"})
print(class_name)
print(class_name[0].text)
print(class_name[1])
print(class_name[2])
print(class_name[3])
print(class_name[4])

list_institute =[]
print(len(class_name))

for x in range(len(class_name)):
    print(class_name[x].text)
    print("****************************")


#------------------------------Business Institute Name ----------------------------

class_name =bs.find_all(class_ ="business")
print(class_name)
print(class_name[0].text)
print(class_name[1].text)
print(class_name[2].text)
print(class_name[3].text)
print(class_name[4].text)

list_institute =[]
print(len(class_name))

for x in range(len(class_name)):
    print(class_name[x].text.strip())
    print("****************************")
    

#------------------------------ Get Institute Card ----------------------------

class_name =bs.find_all(class_ ="sk-card")
print(class_name)
print(class_name[0].text)
print(class_name[1].text)
print(class_name[2].text)
print(class_name[3].text)
print(class_name[4].text)

list_institute =[]
print(len(class_name))

for x in range(len(class_name)):
    print(class_name[x].text)
    print("****************************")