from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random


driver = webdriver.Chrome()

user_amount = int(input("Enter amount of users: "))
usernames = []
all_movies = []
dup = []

for i in range(user_amount):
    username = str(input("Enter username: "))
    usernames.append(username)


for username in usernames:


    driver.get(f"https://letterboxd.com/{username}/watchlist/")

    while True:
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        movies = soup.find_all("span", attrs={"class": "frame-title"})

        for movie in movies:
            all_movies.append(movie.text)

        #Debug
        print(f"Scraping: https://letterboxd.com/{username}/watchlist/")

        try:
            next_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//a[@class="next"]'))
            )
            next_button.click()

            time.sleep(random.uniform(1, 3))
        except Exception as e:
            print("No more pages or error:", e)
            break



driver.quit()

s = set()

for n in all_movies:
    if n in s:
        dup.append(n)
    else:
        s.add(n)

print(dup)


