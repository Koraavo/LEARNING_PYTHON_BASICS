from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.nytimes.com/').text
soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())
#<h2 class="css-14byr0y esl82me0">New U.S. Jobless Claims Bring 9-Week Total to Over 38 Million</h2>
#"css-8atqhb"
article = soup.find('article')
print(article.prettify())
headline = article.find('div', class_='css-gs67ux e1n8kpyg0').text

#<div class="css-1ez5fsm esl82me1"><div class="css-1rczz1p">LIVE</div><h2 class="css-14byr0y esl82me0">New U.S. Jobless Claims Bring 9-Week Total to Over 38 Million</h2></div>