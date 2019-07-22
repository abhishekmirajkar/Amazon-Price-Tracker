from django.shortcuts import render
import requests
import request
from bs4 import BeautifulSoup
import smtplib
import time
import unicodedata
import math


from amazon_track_app.models import trackdata
# Create your views here.
def index(request):
    registered = False


    if request.method=="POST":
        registered = True
        print("HELLO")
        # URL = 'https://www.amazon.de/Sony-Digitalkamera-Touch-Display-Vollformatsensor-Kartenslots/dp/B07B4R8QGM/ref=sr_1_5?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=sony+alpha+ILCE&qid=1563110763&s=gateway&sr=8-5'
        p_name1 = request.POST.get('p_name', 'NULL')
        p_email1 = request.POST.get('user_email', 'NULL')
        p_url1 = request.POST.get('p_url', 'NULL')
        p_status1 = registered

        data=trackdata()
        data.p_name = p_name1
        data.p_email=p_email1
        data.p_status=p_status1
        data.p_url = p_url1
        data.save()


        URL = p_url1
        # headers = {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
        # headers = request.headers.get('User-Agent')
        # request.headers.get('User-Agent')




        def check_price():
            page = requests.get(URL)

            soup = BeautifulSoup(page.content,'html.parser')

            print(soup.prettify())

            title_half = soup.find(id="productTitle")
            print(title_half)
            title = title_half.get_text()
            # print(title.strip())
            print(title)

            price_half = soup.find(id="priceblock_ourprice")
            print(price_half)
            price = price_half.get_text()
            price1 = unicodedata.normalize('NFKD', price).encode('ascii','ignore')
            converted_price1 = int(filter(str.isdigit, price1))
            converted_price = math.floor(converted_price1)/100
            print(price)
            print("__________")
            print(converted_price)

            if(converted_price > 17):
                print("inside the mail calling function")
                send_mail()
                return render(request,'index.html',{'registered':registered})

        def send_mail():
            print("MAIL")
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.ehlo()
            server.starttls()
            server.ehlo()

            server.login('pricetrackerforall@gmail.com','jjkwdlygrmmraatg')

            subject = "Price Fell Down"
            body = " Hello \n\n Thank you for subscribing at Amazon Price Tracker \n\n The product price is in your budget now \n Check the Amazon link \n " + URL

            # msg = subject + body

            message = 'Subject: {}\n\n{}'.format(subject, body)

            server.sendmail(
                'pricetrackerforall@gmail.com',
                'abhishekmirajkar03@gmail.com',
                message,
            )

            print("Hey Email Has Been Sent")
            # print(msg)

            server.quit()
        while(True):
            check_price()
            time.sleep(60)

            return render(request,'index.html',{'registered':registered})
    return render(request,'index.html',{'registered':registered})
