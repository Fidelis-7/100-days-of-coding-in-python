import requests
from bs4 import BeautifulSoup

url = "https://www.empireonline.com/movies/features/best-movies-century/"

# Send a GET request to the URL
response = requests.get(url)
website_html = response.text

# Create BeautifulSoup object from the response content
soup = BeautifulSoup(website_html, 'html.parser')

# container = soup.find_all('div', class_="jsx-3523802742 listicle-item")
# Extract all the movie titles
empire_website = soup.select_one(selector="div", name="h3", class_="jsx-3523802742 listicle-item")

all_movies = empire_website.find_all(class_="jsx-4245974604")
# Print the movie titles
movie_titles = []
for movie in all_movies:
    movie_titles.append(movie.text)
    for n in range(len(movie_titles) -1, 0, -1):
        print(movie_titles[n])


with open("top_movies.txt", mode="w") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")