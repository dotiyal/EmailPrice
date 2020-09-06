import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/Apple-iPhone-Pro-Max-64GB/dp/B07XLS5796?ref_=ast_sto_dp&th=1'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/85.0.4183.83 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup.prettify())

    title = soup.find(id="productTitle").get_text()
    print(title.strip())

    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = price[1:-3]

    print(converted_price)

    converted_price_int = ""
    for i in converted_price:
        if i != ',':
            converted_price_int += i

    print(converted_price_int)

    if int(converted_price_int) < 100000:
        send_mail()

    # if int(converted_price_int) > 100000:
    #    send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('forsoftwaredev@gmail.com', 'ffhbahmypzvxooba')

    subject = "Price fell down"
    body = "Check the amazone link: https://www.amazon.in/Apple-iPhone-Pro-Max-64GB/dp/B07XLS5796?ref_=ast_sto_dp&th=1"

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        "forsoftwaredev@gmail.com",
        "itssid143@gmail.com",
        msg
    )
    print("HEY EMAIL HAS BEEN SENT!")
    server.quit()


while True:
    check_price()
    time.sleep(24*3600)
