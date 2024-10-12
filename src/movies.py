from bs4 import BeautifulSoup
import requests
from playwright.sync_api import sync_playwright
import time
import json

# store target url
url = "https://www.imdb.com/chart/top/"  # IMDB Top 250 Movies


def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)

    # Wait for the movie list to load
    page.wait_for_selector("ul.ipc-metadata-list")

    # Extract movie information
    movies = page.query_selector_all("li.ipc-metadata-list-summary-item")

    movie_list = []

    for movie in movies:
        title = movie.query_selector(".ipc-title__text").inner_text()
        year = movie.query_selector(".cli-title-metadata-item").inner_text()
        rating = movie.query_selector(".ipc-rating-star--imdb").inner_text()

        # Create a dictionary for each movie
        movie_data = {"title": title, "year": year, "rating": rating}

        movie_list.append(movie_data)

        print(f"Title: {title}")
        print(f"Year: {year}")
        print(f"Rating: {rating}")
        print("---")

    # Write the movie list to a JSON file
    with open("movies.json", "w", encoding="utf-8") as f:
        json.dump(movie_list, f, ensure_ascii=False, indent=4)

    print(f"Movie data has been written to movies.json")

    time.sleep(5)  # Keep the browser open for 5 seconds so you can see the result
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
