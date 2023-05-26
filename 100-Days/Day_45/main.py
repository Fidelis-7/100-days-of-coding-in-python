from bs4 import BeautifulSoup
import requests

hacker_news = requests.get("https://news.ycombinator.com/")
yc_webpage = hacker_news.text

soup = BeautifulSoup(yc_webpage, "html.parser")
math_heading = soup.find(class_="titleline")
math_heading_link = soup.getText("href")
math_heading_upvote = soup.find(name="span", class_="score").getText()
print(math_heading.text)
print(math_heading_link)
print(math_heading_upvote)


























# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()


# soup = BeautifulSoup(contents, "html.parser")
# anchor_tags = soup.find_all(name="a")
# for anchor in anchor_tags:
#     print(anchor.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading.text)

# heading = soup.find(name="h3", class_= "heading")
# print(heading.getText())

# company_url = soup.select_one(selector="p a")
# print(company_url)