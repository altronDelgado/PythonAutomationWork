import email
import imp
import os
import requests
import bs4
import smtplib
import os


email_add = os.environ.get('EMAIL_ADD')
password = os.environ.get('EMAIL_PASS')



def send_email():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(email_add, password)
    subject = "!!!!!! 100 days of devops site is down"
    body = "Check the status of 100 days of devops"
    message = f'Subject: {subject}\n\n {body}'
    # s.sendmail("sender_email", "reciever_email", message)
    s.sendmail(email_add, email_add, message)
    s.quit()

producturl = "https://www.101daysofdevops.com/"

res = requests.get(producturl, timeout=5)
if res.status_code != 200:
    send_email()

soup = bs4.BeautifulSoup(res.text,'html.parser')

elems = soup.select("#main-home-content > div > div > div > section.elementor-section.elementor-top-section.elementor-element.elementor-element-bc498db.elementor-section-full_width.elementor-section-height-default.elementor-section-height-default > div > div > div > div > div > div.elementor-element.elementor-element-834e8ba.elementor-widget.elementor-widget-thim-heading > div > div > div > h3")
try:
    if elems[0].text != "Popular Courses":
        send_email()
except Exception as err:
    send_email()