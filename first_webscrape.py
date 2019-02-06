from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

my_url = "https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&IsNodeId=1&N=100007709%20600499109"

# opening up a connection and grabbing the page
uclient = ureq(my_url)
page_html = uclient.read()
uclient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs each product
containers = page_soup.find_all("div",{"class":"item-container"})
abrands = page_soup.find_all("a",{"class":"item-brand"})

filename = "Graphics Cards.csv"
f = open(filename, "w")

headers = "Make, Product_Name, Shipping\n"

f.write(headers)

for container in containers:
	for abrand in abrands:
		pass
	make = abrand.img["title"]
	
	title_container = container.find_all("a",{"class":"item-title"})
	product_name = title_container[0].text

	shipping_container = container.find_all("li",{"class":"price-ship"})
	shipping = shipping_container[0].text.strip()

	print("make: " + make)
	print("product_name: " + product_name)
	print("shipping: " + shipping, "\n")

	f.write(make + "," + product_name.replace(",", "|") + "," + shipping + "\n")

f.close()