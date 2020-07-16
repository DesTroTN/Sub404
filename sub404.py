import os
import sys
import threading
import subprocess
#Coding By ./DesTroTN
#Github:./DesTroTN
if sys.platform.startswith('win'):
    os.system('cls')

    try:
        import colorama
        colorama.init()

    except:
        print('[!] Color module not found!!!\n[*] Try to run "pip install colorama"')
        sys.exit()


banner = """\033[1m\033[91m
\t\t     ____        _       _  _    ___  _  _
\t\t    / ___| _   _| |__   | || |  / _ \| || |
\t\t    \___ \| | | | '_ \  | || |_| | | | || |_
\t\t     ___) | |_| | |_) | |__   _| |_| |__   _|
\t\t    |____/ \__,_|_.__/     |_|  \___/   |_|

                       \t\t\t\033[93m- By ./DesTroTN

    """
print(banner)


try:
    import argparse
    import dns.resolver
    import aiohttp
    import asyncio
    from aiohttp import *

except:
    print('\033[1m[\033[93m!]\033[91m Modules are not found..!!\n\033[92m[-] Try to run "pip3 install -r requirements.txt"\n')
    sys.exit()

try:
    import time
except:
    print('[!] Time module not found!!!')
    sys.exit()


uniqueDomain = []
url_404 = []
inputURL = []


class Spinner:
    busy = False
    delay = 0.1

    @staticmethod
    def spinning_cursor():
        while 1:
            for cursor in '|/-\\':
                yield cursor

    def __init__(self, delay=None):
        self.spinner_generator = self.spinning_cursor()
        if delay and float(delay):
            self.delay = delay

    def spinner_task(self):
        while self.busy:
            sys.stdout.write(next(self.spinner_generator))
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write('\b')
            sys.stdout.flush()

    def __enter__(self):
        self.busy = True
        threading.Thread(target=self.spinner_task).start()

    def __exit__(self, exception, value, tb):
        self.busy = False
        time.sleep(self.delay)
        if exception is not None:
            return False


def main():

    # G = '\033[92m'
    # Y = '\033[93m'
    # B='\033[94m'
    # C = '\033[96m'
    # R = '\033[91m'

    parser = argparse.ArgumentParser(description='A python tool to check for subdomain takeover.')
    parser.add_argument('-f', '--file', help='Provide location of subdomain file to check for takeover if subfinder is not installed. [ex: --file /path/of/subdomain/file]')
    parser.add_argument('-o', '--output', help='Output unique subdomains of sublist3r and subfinder to text file [ex: --output uniqueURL.txt]', default='uniqueURL.txt')
    parser.add_argument('-p', '--protocol', help='Set protocol for requests. Default is "http" [ex: --protocol https]', default='http')
    args = parser.parse_args()

    
    # Get url which has 404 respose code

    def getResponseCode(inputFile):

        try:
            data = open(inputFile, "r")
            print('\033[96m[-] Reading file '+'\033[94m'+inputFile)
            print('\033[92m[-] Gathering Information...')

            time.sleep(2)
            print('\033[93m[-] Total Unique Subdomain Found: '+" "+str(sum(1 for line in open(inputFile, 'r'))))
            time.sleep(1)
            print('\033[92m[-] Default http [use -p https] ')
            time.sleep(1)
            print('\033[92m[-] Checking response code...')

        except NameError:
            print("\n\033[91m[!] "+inputFile+" File not found...!!!\n\033[92m[-] Check filename and path.")
            sys.exit()

        except IOError:
            print("\n\033[91m[!] "+inputFile+" File not found...!!!\n\033[92m[-]Check filename and path.")
            sys.exit()

        subdomain = data.readlines()

        for line in subdomain:
            if 'http://' and 'https://' not in line:
                inputURL.append(args.protocol+"://"+line.strip())

            else:
                inputURL.append(line.strip())

        with Spinner():
            asyncio.run(urlCode())

        if len(url_404) == 0:
            print('\033[94m[*] Task Completed :)')
            print('\033[91m[!] Target is not vulnerable!!!')
            sys.exit()

        cnameExtract(url_404)

    # Extract CNAME records

    def cnameExtract(invalidURLs):

        print('\033[92m[-] Checking CNAME records...\n')

        for x in invalidURLs:
            if 'http://' or 'https://' in x:
                data = x.replace('https://', '')
                data = x.replace('http://', '')

            else:
                pass

            try:

                resolve = dns.resolver.query(data.strip(), 'CNAME')

                for rdata in resolve:
                    cdata = (rdata.to_text()).strip()
                    targetDomain = data.strip()

                    if targetDomain[-8:] not in cdata:
                        print('\n\033[96m[-] Vulnerability Possible on: '+'\033[92m'+str(data)+"\n\t"+'\033[94mCNAME: '+'\033[93m'+str(rdata.to_text()))

                    else:
                        print('\n\033[92m[-] '+str(data)+'\n'+'\033[91m \tNot Vulnerable')

            except:
                print('\n\033[92m[-] '+str(data)+'\n'+'\033[91m \tNot Vulnerable')

        print('\033[94m[*] Task Completed :)')
        sys.exit()

    if args.file:

        getResponseCode(args.file)

    else:
        print('usage: sub404.py [-h] [-f FILE] [-o OUTPUT] [-p PROTOCOL]')

    # check response code


async def getCode():
    async with aiohttp.ClientSession() as session:
        await gen_tasks(session, 'random.txt')


async def urlCode():
    async with aiohttp.ClientSession() as session:
        await gen_input_tasks(session, 'random.txt')


async def fetch_url(session, url):
    count = 0
    try:
        async with session.get(url) as response:
            reason = response.reason
            status = response.status

            if status == 404:
                url_404.append(url)
                pass
            else:
                pass

    except ClientConnectionError:
        return (url, 500)
    except ClientOSError:
        return (url, 500)
    except ServerDisconnectedError:
        return (url, 500)
    except asyncio.TimeoutError:
        return (url, 500)
    except UnicodeDecodeError:
        return (url, 500)
    except TooManyRedirects:
        return (url, 500)
    except ServerTimeoutError:
        return (url, 500)
    except ServerConnectionError:
        return (url, 500)
    except RuntimeError:
        pass
    except OSError:
        pass
    except Exception as err:
        pass


async def gen_input_tasks(session, url_list):

    tasks = []
    print('\033[92m[-] Getting URL\'s of 404 status code...')

    for url in inputURL:
        task = asyncio.ensure_future(fetch_url(session, url))
        tasks.append(task)

    result = await asyncio.gather(*tasks)
    print('\033[93m[-] URL Checked: '+str(len(inputURL)))
    time.sleep(1)
    return result


async def gen_tasks(session, url_list):

    tasks = []
    print('\033[92m[-] Getting URL\'s of 404 status code...')

    for url in uniqueDomain:
        task = asyncio.ensure_future(fetch_url(session, url))
        tasks.append(task)

    result = await asyncio.gather(*tasks)
    print('\033[93m[-] URL Checked: '+str(len(uniqueDomain)))
    time.sleep(1)
    return result

if __name__ == "__main__":
    main()
