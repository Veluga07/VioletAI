# dataset.py

import requests
from bs4 import BeautifulSoup
import re

def fetch_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    return preprocess_text(text)

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)  # 숫자 제거
    text = re.sub(r'\s+', ' ', text)  # 다중 공백 제거
    text = re.sub(r'[^\w\s]', '', text)  # 구두점 제거
    return text
