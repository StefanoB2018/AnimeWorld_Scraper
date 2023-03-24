# AnimeWorld_Scraper
Italian anime website video extraction script.

Pubblished in 24/03/2023

## Setup

+ [Python](https://www.python.org/downloads/) needs to be installed

+ Clone the repository

+ Run "requirements.bat to automatically install the needed python libraries

   Otherwise install them manually via terminal:
  ```
  pip install wget
  pip install fake-useragent
  pip install beautifulsoup4
  ```
+ Retrieve working proxies from any source and put them in `http.txt` (proxies formatted as the image below):

    ![https.txt](https://i.imgur.com/CyXjBg8.png)
  
    [get proxies here (recommended)](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)
    
## How to use?
1. Run `webscraping.py`
2. Insert link
3. Insert Episode
4. Download
5. Retrieve the videos downloaded from `Scrap\folder`
