import requests
from bs4 import BeautifulSoup
from datetime import date
from send_cartoon import send_message

def get_latest_cartoon():
    url = 'http://corrigan.ca/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    cartoon_img = soup.find('img', {'alt': 'cartoon'})
    cartoon_url = url + cartoon_img['src'] if cartoon_img else None
    
    date_span = soup.find('span', style="font-weight: bold;")
    cartoon_date = date_span.text.strip() if date_span else None

    return cartoon_url, cartoon_date

def is_new_cartoon(cartoon_date):
    today = date.today().strftime("%B %d, %Y")
    return cartoon_date == today