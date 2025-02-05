from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from collections import Counter

driver = webdriver.Chrome()

user_amount = int(input("Enter amount of users: "))
usernames = []
dup = []
all_movies = []

for i in range(user_amount):
    username = str(input("Enter username: "))
    usernames.append(username)

for username in usernames:

    driver.get(f"https://letterboxd.com/{username}/watchlist/")

    while True:
        time.sleep(3)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        movies = soup.find_all("span", attrs={"class": "frame-title"})

        for movie in movies:
            all_movies.append(movie.text)

        #Debug
        print(f"Scraping: https://letterboxd.com/{username}/watchlist/")

        try:
            next_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//a[@class="next"]'))
            )
            next_button.click()

            time.sleep(random.uniform(1, 3))
        except:
            print("No more pages or error:")
            break

driver.quit()

counts = Counter(all_movies)

movie_amount = max(counts.values())

while movie_amount > 1:
    for movie, count in counts.items():
        if count == movie_amount:
            print(f"{movie} - {count}")
    movie_amount -= 1