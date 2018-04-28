from urllib.request import urlopen
content = urlopen("http://testing-ground.scraping.pro/blocks")
print(content.read())