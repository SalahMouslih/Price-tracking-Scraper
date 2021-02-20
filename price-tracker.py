from bs4 import BeautifulSoup
import requests
import smtplib
import time

# a scrapper needs The URL, RESPONSE & CONTENT

# The URL is simply a string that contains the address of the HTML page we intend to scrape.
# The RESPONSE is the result of a GET request. We’ll actually use the URL variable in the GET request here.
# CONTENT is the content of the response. If we print the entire response content, we’ll get all the content on the entire page of the url we’ve requested.

url = 'https://brahimnasiri.com/wp-content/uploads/macbook-pro-2020-13inch-2/'
# gives infos about the browser
headers = {
            "User-Agent" : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/85.0.4183.102 Safari/537.36'}


def check_price():
    response = requests.get(url, timeout=5)
    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.find('h1', attrs= {'class': "product_title entry-title"}).text   
    price = soup.find('span', attrs= {'class': "woocommerce-Price-amount amount"}).text
    converted_price= price[0:6]
    reconverted_price = converted_price.replace(",",'.')
    if (float(reconverted_price) < 18.000) :
        send_mail()

def send_mail():
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('insea.signup@gmail.com','***')

    subject = "Price just dropped!"
    body="check out the link quickly https://brahimnasiri.com/wp-content/uploads/macbook-pro-2020-13inch-2/"

    # formatting the message   
    msg= f" Subject: {subject}\n\n{body}"
    server.sendmail(
        'insea.signup@gmail.com',
        'salahddin11@gmail.com',
        msg
    )
    print("Email Sent")

    server.quit()

while(True):
    check_price()
    time.sleep(3600*24*15)

    