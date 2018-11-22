from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'

uClient=uReq(my_url)

page_html=uClient.read()


uClient.close()
page_soup =soup(page_html, "html.parser")
containers = page_soup.findAll("div", {"class": "_3O0U0u"})
container = containers[0]

# print(len(containers))

# print(soup.prettify(containers[23])) 
price = container.findAll("div", {"class": "col col-5-12 _2o7WAb"})
print(price[0].text)

#for name
print(container.div.img["alt"])
ratings = container.findAll("div", {"class": "niH0FQ"})

# # container=containers[0]
print(ratings[0].text)


# creating file
filename="products1.csv"
f=open(filename,"w")

headers="Product_Name, Pricing, Rating\n"
f.write(headers)

for container in containers:
    product_name=container.div.img["alt"]

    price_container = container.findAll(
        "div", {"class": "col col-5-12 _2o7WAb"})
    price=price_container[0].text.strip()

    rating_container = container.findAll("div", {"class": "niH0FQ"})
    rating=rating_container[0].text


    print("product_name:" + product_name)
    print("price:"+ price)

    print("ratings:" + rating)

