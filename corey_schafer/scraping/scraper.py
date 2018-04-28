from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://yo-movies.com/movies/1').text

soup = BeautifulSoup( source , 'lxml' )

csv_file = open('cms_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['movie_name', 'movie_link' ])

main_container_div = soup.find('div' , class_='main-content')
#each_container_div = main_container_div.find('div',class_='ml-item')
for each_container_div in main_container_div.find_all('div',class_='ml-item'):

	movie_name = each_container_div.find('span' , class_='mli-info').h2.text
	movie_name = u''.join(movie_name).encode('utf-8').strip()
	print(movie_name)

	movie_slug_url = each_container_div.a['href']
	movie_link = f'https://yo-movies.com{movie_slug_url}'
	movie_link = u''.join(movie_link).encode('utf-8').strip()
	print(movie_link)

	print()

	csv_writer.writerow([movie_name, movie_link ])

csv_file.close()