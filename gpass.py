#!/usr/bin/python
# -*- coding: UTF-8 -*-

import string
import requests.exceptions
import re
import time
import sys
#from pip._vendor.distlib.compat import raw_input
from bs4 import BeautifulSoup
from urllib.parse import urlsplit
from collections import deque
from termcolor import *

#    logo

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
v3 = colored('\033[1m'+"]", 'red')
#      input randompass
mixchars = string.ascii_letters + string.digits + string.punctuation

randompass = input(colored('\033[1m'+'Enter Your Code :  ', "yellow"))



lod=colored('\033[1m'+"Loading Tools :)\n ", 'green')



#here is the animation
chek=colored('\033[1m'+"Check Code :", 'yellow')
print(chek)
animation = ('\033[1m'+"[■□□□□□□□□□]\n","[■■□□□□□□□□]\n", "[■■■□□□□□□□]\n", "[■■■■□□□□□□]\n", "[■■■■■□□□□□]\n", "[■■■■■■□□□□]\n", "[■■■■■■■□□□]\n", "[■■■■■■■■□□]\n", "[■■■■■■■■■□]\n", "[■■■■■■■■■■]\n")

for i in range(len(animation)):

            time.sleep(0.4)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()

#       password login

if not randompass != 'tommy':
    done = colored('\033[1m' + "\rDONE !", 'green')

    print(done) == True
    animationdone = ('\033[1m' + "[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]",
                 "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]")
    time.sleep(1)
    hi = colored(("Hi " + randompass+ " Loading Tool!"), 'green')
    print(hi)
    for i in range(len(animationdone)):
        time.sleep(0.4)
        sys.stdout.write("\r" + animationdone[i % len(animationdone)])
        sys.stdout.flush()
else:
    OHH = colored('\033[1m' + "\rOhh !", 'red')
    print(OHH)
    False  == print(colored('\033[1m'+'Sorry ! your code not True\nPlease Try Again!', "red")), exit()



#long process here

#      websites links
new_urls = deque(['http://ertu.org/1/friendsReg_frame.asp'])

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

#          random emails

    new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", tommy.text, re.I, ))
    emails.update(new_emails)

    # print(pr)



    for new_emails in new_emails:
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

        by = colored('\033[1m'+"OK", 'green',)
        pr = colored((" %s" % '\033[1m' + new_emails), 'yellow')
        if (re.search(regex, new_emails)):
           v = colored('\033[1m'+"    Valid Email", 'green')
           print(v)
        else:
            f = colored('\033[1m'+"    Invalid Email", 'red')
            print(f)

            if __name__ == '__main__':
                # Enter the email
                new_emails = new_emails

        error = print('')

        data = print(v1, by, v3, pr, end='\n')
        srl = float("009")

        time.sleep(0.4)




    #     seach mails

    soup = BeautifulSoup(tommy.text, 'html.parser')

    for anchor in soup.find_all("a"):
        link = anchor.attrs["href"] if "href" in anchor.attrs else ''
    if link.startswith('/'):
        link = base_url + link
    elif not link.startswith('http'):
        link = path + link
    if not link in new_urls and not link in processed_urls:
        new_urls.append(link)

