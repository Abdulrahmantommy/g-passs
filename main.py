from bs4 import BeautifulSoup

import string
import webbrowser
from random import *
import requests
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque
import re
from termcolor import *
tm=colored("""
    
    
##################################################
                                                 #
 ▄▀▀▀▀▄        ▄▀▀▄▀▀▀▄  ▄▀▀█▄   ▄▀▀▀▀▄  ▄▀▀▀▀▄  #
█             █   █   █ ▐ ▄▀ ▀▄ █ █   ▐ █ █   ▐  #
█    ▀▄▄      ▐  █▀▀▀▀    █▄▄▄█    ▀▄      ▀▄    #
█     █ █        █       ▄▀   █ ▀▄   █  ▀▄   █   #
▐▀▄▄▄▄▀ ▐      ▄▀       █   ▄▀   █▀▀▀    █▀▀▀    #
▐             █         ▐   ▐    ▐       ▐       #
MADY BY TOMMY ▐   "Abdulrahman Tohamy"  V.0.1    #                        
##################################################
    
    """, "red")
print(tm)
mixchars = string.ascii_letters+string.digits+string.punctuation


randompass = input("Gave me Name or Number: ").join(choice(mixchars) for i in range(randint(8, 20)))
print("Your Random Password is: ")
ps=colored(randompass, "blue")
print(ps)
# a queue of urls to be crawled
new_urls = deque(['http://ertu.org/1/friendsReg_frame.asp'])

#['http://ertu.org/1/friendsReg_frame.asp']
# a set of urls that we have already crawled
processed_urls = set()

# a set of crawled emails
emails = set()

# process urls one by one until we exhaust the queue
while len(new_urls):
	# move next url from the queue to the set of processed urls
	url = new_urls.popleft()
	processed_urls.add(url)

	# extract base url to resolve relative links
	parts = urlsplit(url)
	base_url = "{0.scheme}://{0.netloc}".format(parts)
	path = url[:url.rfind('/')+1] if '/' in parts.path else url

	# get url's content

	try:
		tommy = requests.get(url)
	except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
		# ignore pages with errors
		continue

	# extract all email addresses and add them into the resulting set
	new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", tommy.text, re.I,))
	emails.update(new_emails)
	pr=colored("By Tommy >>  %s"  % new_emails, 'green')

	print(pr)

	# create a beutiful soup for the html document
	soup = BeautifulSoup(tommy.text, 'html.parser')

	# find and process all the anchors in the document
	for anchor in soup.find_all("a"):
		# extract link url from the anchor
		link = anchor.attrs["href"] if "href" in anchor.attrs else ''
	# resolve relative links
	if link.startswith('/'):
		link = base_url + link
	elif not link.startswith('http'):
		link = path + link
	# add the new url to the queue if it was not enqueued nor processed yet
	if not link in new_urls and not link in processed_urls:
		new_urls.append(link)





