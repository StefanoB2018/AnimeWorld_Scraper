
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import urllib.request
import re
import wget
import os
import os.path
import random


# check if the folder exists, cd to that folder, otherwise create it and then cd.

def makeDir(temp_dir):
    if (os.path.isdir(temp_dir)):
        os.chdir(temp_dir)
    else:
        os.mkdir(temp_dir)
        os.chdir(temp_dir)

# input number, returns the digit of number.

def countDigit(i):
    num = i
    count = 0
    while num > 0:
        count += 1
        num = num//10
    return count

# input number, returns formatted number from 00 to 99.

def format(i):
    digit = countDigit(i)
    if (digit == 2):
        strNum = str(i)
    else:
        strNum = "0" + str(i)
    return strNum


# set proxy

def set_http_proxy(proxy, randIndex):

    proxy_support = urllib.request.ProxyHandler(
        {'http': '%s' % proxy[randIndex]})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
    return "Proxy installed.\n"

# return random number > list length.
def random_proxy(proxies):
    return random.randint(0, len(proxies) - 1)

defaultPath = os.getcwd()
proxies = []
maxProxies = 0
ua = UserAgent()
url = ""
count = 0
numEp = 0
isFirst = True
exit = "0"
while(exit != '1'):
    proxy_attempts = 0
    #proxy list txt
    with open('http.txt') as f:
        proxies = f.read().splitlines()
        maxProxies += 1
    req = urllib.request.Request(url=input('Insert link: '), headers={'User-Agent': ua.random})
    numEp = int(input("Type episode number to download: "))
    times = int(input("Type the number of episodes you want to download: "))
    makeDir('folder')

    for n in range(times+1):
        if n % 10 == 0:
            randIndex = random_proxy(proxies)
            set_http_proxy(proxies, randIndex)
        try:
            proxy_attempts += 1
            # first execution -> get video link
            if (isFirst):
                with urllib.request.urlopen(req) as html_page:
                    print('# proxy request ' + str(proxy_attempts))
                    soup = BeautifulSoup(html_page, "html.parser")
                    for link in soup.findAll('a', attrs={'href': re.compile("^https://")}):
                        if (count == 27):
                            url = link.get('href')
                        count += 1
                    isFirst = False
            else:
                # link iteration
                url = url.split('_Ep_')[0] + '_Ep_' + \
                    format(numEp) + '_SUB_' + url.split('_SUB_')[1]
                print("\nEp" + str(numEp) + ": ")
                # download from url - video destination
                wget.download(url,'folder')
                numEp += 1

        except:  # If error, delete this proxy and find another one
            print('\nProxy ' + proxies[randIndex] + '  deleted.')
            del proxies[randIndex]
            randIndex = random_proxy(proxies)
    os.chdir(defaultPath)
    exit = input('Enter 1 to end, any other key to continue.\n')
    isFirst = True
print('\nProgram ended.')
