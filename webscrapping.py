import bs4
import requests

url  =input("Enter any url")

response = requests.get(url)

if response.status_code == 200:
    print("successful connection")
else:
    print("connection failed")

file2  = open(r"C:\Users\user\Desktop\flipkart_data.xls","a",encoding="utf-8")
filename ="flipkart.html"
bs = bs4.BeautifulSoup(response.text,"html.parser")
bs
len(bs)
formatted_new_data = bs.prettify()
print(formatted_new_data)

a1 = bs.find_all('a')
a1
len(a1)

a2 = bs.find_all('p')
a2
len(a2)

a3 = bs.find_all('span')
a3
len(a3)

a4 = bs.find_all(class_ = "_4rR01T")
a4
a4[0]
a4[0].text
len(a4)
mobile_phone_name = []
for x in range(len(a4)):
    print(a4[x].text)
    file2.write(a4[x].text)
    file2.write("\t")
    file2.write(a4[x].text)
    file2.write(" \n")
    file2.write(" \n")


a5 = bs.find_all(class_ = "_30jeq3 _1_WHN1")
a5
len(a5)

for x in range(len(a5)):
    print(a5[x].text)
    file2.write(a5[x].text)
    file2.write(" \n")

file2.close()
