from bs4 import BeautifulSoup
import string
from random import *
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque
import re
from termcolor import *

tm = colored('\033[1m'+"""
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
""", "yellow")
print(tm)
gt = colored(">>", 'blue')
v1 = colored('\033[1m'+"[", 'red' )
#v2 = colored('\033[1m'+">", 'cyan', 'on_red')
v3 = colored('\033[1m'+"]", 'red')
#all= print(v1, v2, v3)
mixchars = string.ascii_letters + string.digits + string.punctuation

randompass = input(colored('\033[1m'+"Enter your Code : ", 'yellow', 'on_blue')).join(choice(mixchars) for i in range(randint(8, 20)))
print('\033[1m'+"Yor Code Login To Tool Is : ")
ps = colored('\033[1m'+randompass, "blue", "on_yellow")
print(ps)
lod=colored('\033[1m'+"Loading Tools.... :) ", 'green')
print(lod)
new_urls = deque(['http://google.com/', 'http://ertu.org/1/friendsReg_frame.asp'])

# ['http://ertu.org/1/friendsReg_frame.asp']
processed_urls = set()

emails = set()

while len(new_urls):
    url = new_urls.popleft()
    processed_urls.add(url)

    parts = urlsplit(url)
    base_url = "{0.scheme}://{0.netloc}".format(parts)
    path = url[:url.rfind('/') + 1] if '/' in parts.path else url


    try:
        tommy = requests.get(url)
    except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
        continue



    new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", tommy.text, re.I, ))
    emails.update(new_emails)

    # print(pr)

    for new_emails in new_emails:

        by = colored('\033[1m'+"OK", 'green',)
        pr = colored(" %s"% '\033[1m'+new_emails,  'yellow')

        error = print('')



        print(v1, by,v3, pr,  end='\n')

#------

    soup = BeautifulSoup(tommy.text, 'html.parser')

    for anchor in soup.find_all("a"):
        link = anchor.attrs["href"] if "href" in anchor.attrs else ''
    if link.startswith('/'):
        link = base_url + link
    elif not link.startswith('http'):
        link = path + link
    if not link in new_urls and not link in processed_urls:
        new_urls.append(link)
