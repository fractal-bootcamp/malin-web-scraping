from bs4 import BeautifulSoup
import requests

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"  # IMDB Top 250 Movies
response = requests.get(url)
soup = BeautifulSoup(response.content, "lxml")
