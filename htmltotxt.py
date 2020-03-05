from selectolax.parser import HTMLParser
import requests
import re

HREF_REGEX = re.compile(r'href=([\'\"])(.*?)\1', re.IGNORECASE)

def isUrlNa(str):
	if str.startswith('javascript:'): return 1
	if str.startswith('mailto:'): return 1
	if str.startswith('#'): return 1
	if str.endswith('.png'): return 1
	if str.endswith('.jpeg'): return 1
	if str.endswith('.jpg'): return 1
	if str == '': return 1
	if str == '/': return 1
	return 0

def prepareUrl(parenturl, childurl):
	url = parenturl+childurl if childurl.startswith('/') else childurl
	return url

def htmltotxt(url):
	# html = urlopen(url).read()
	html = requests.get(url).text
	tree = HTMLParser(html)
	for tag in tree.css('script') + tree.css('style'): tag.decompose()
	text = re.sub(" +", " ", tree.body.text().replace("\n", ""))
	title = tree.css_first('title').text().strip()
	hrefs = set(prepareUrl(url, match[1]) for match in HREF_REGEX.findall(html) if not isUrlNa(match[1]))
	return title, text, hrefs

url = "https://danskebank.com"
title, text, hrefs  = htmltotxt(url)

hrefs
