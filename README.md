# Sub404: A Fast Tool To Check Subdomain Takeover Vulnerability

````
     ____        _       _  _    ___  _  _
    / ___| _   _| |__   | || |  / _ \| || |
    \___ \| | | | '_ \  | || |_| | | | || |_
     ___) | |_| | |_) | |__   _| |_| |__   _|
    |____/ \__,_|_.__/     |_|  \___/   |_|

                       - By ./DesTroTN
````
					   
## What is Sub 404
Sub 404 is a tool written in python which is used to check possibility of subdomain takeover vulnerabilty and it is fast as it is Asynchronous.

## Why
During recon process you might get a lot of subdomains(e.g more than 10k). It is not possible to test each manually or with traditional requests or urllib method as it is very slow. Using <b>Sub 404</b> you can automate this task in much faster way. Sub 404 uses <b>aiohttp/asyncio</b> which makes this tool asynchronous and faster.

## How it works
Sub 404 uses subdomains list from text file and checks for url of <b>404 Not Found</b> status code and in addition it fetches <b>CNAME</b>(Canonical name) and removes those URL which have target domain name in CNAME.</b>(subdomain enumeration tool) if you don't have target subdomains as two is better than one. Sub 404 is able to check <b>7K</b> subdomains in less than 5 minutes.

## Key Features:
```
- Fast( as it is Asynchronous)
- Uses two more tool to increase efficiency
- Saves result in a text file for future reference
- Umm thats it, nothing much !
```
## How to use:
<b>Note: Only works on Python3.7+</b>

- git clone https://github.com/DesTroTN/sub404.git
- Install dependencies: pip install -r requirements.txt
- python3 sub404.py -h 

## Note:
<b>This tool is mostly tested in linux but should works on other OS too.</b>
## Usage options:
```

 * <img src="https://github.com/DesTroTN/Sub404/blob/master/404.png">

$ python3 sub404.py -h
```
This will display help for the tool. Here are all the switches it supports.


|Flag |                Description                                             |                       Example                                         |
|-----|------------------------------------------------------------------------|-----------------------------------------------------------------------|
| -f  | Provide location of subdomain file to check for takeover               | python3 sub404.py -f subdomain.txt                                    |
| -p  | Set protocol for requests. Default is "http".| python3 sub404.py -f subdomain.txt -p https or python3 sub404.py -d noobarmy.tech -p https      |
| -o  | Output unique subdomains of sublist3r and subfinder to text file. Default is "uniqueURL.txt" | python3 sub404.py -d noobarmy.tech -o output.txt|
| -h  | show this help message and exit                                        | python3 sub404.py -h                                                  |

## Note:
```
This tool fetches CNAME of 404 response code URL and removes all URL which have target domain in CNAME. So chances of false positives are high.
```

## My Instagram:
<b>Say Hello [DesTroTN](https://www.facebook.com/DesTroTN/)

