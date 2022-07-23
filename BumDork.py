import requests, argparse, random
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from bs4 import BeautifulSoup as bsoup
from colorama import init, Fore, Back, Style

# Created by Ayhuuu
init(autoreset=True)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

user_agents = [
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
'Mozilla/5.0 (Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'
'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko'
'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'
'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 7.0; InfoPath.3; .NET CLR 3.1.40767; Trident/6.0; en-IN)'
'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)'
'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)'
'Mozilla/4.0 (Compatible; MSIE 8.0; Windows NT 5.2; Trident/6.0)'
'Mozilla/4.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)'
'Mozilla/1.22 (compatible; MSIE 10.0; Windows 3.1)'
'Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))'
'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)'
'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 7.1; Trident/5.0)'
]

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dork', dest='dork', help='Enter your dork terms in quotes seperated by a space. Ex: "intext:@gmail.com filetype:log"')
    parser.add_argument('-n', '--num_results', dest='num_results', help='Enter the number of results to obtain. Default: 10. Google will cap results at a maximum of 100 per query.')
    parser.add_argument('-o', '--output', dest='filename', help='Output results to specified path/file')
    parser.add_argument('-c', '--check_result', dest='check_result', nargs='?', const=1, help='Check link result for HTTP 200 response code')
    options = parser.parse_args()
    return options

def do_dorks(dorks, num_res):
    total_scraped = 0
    print(Fore.YELLOW + "[:] Submitting dork search request: " + dorks)
    if options.check_result:
        print(Fore.CYAN + "[:] Check results for status enabled, this may take some time.")
    google = ''
    headers  = { 'User-Agent': random.choice(user_agents) }
    params   = { 'q': dorks, 'num': num_res }
    resp = requests.get("https://www.google.com/search", params=params, headers=headers)
    soup = bsoup(resp.text, 'html.parser')
    links = []
    raw  = soup.findAll("div", {"class": "yuRUbf"})       
       
    for r in raw:
        if r.find("a") not in links:
            links.append(r.find("a"))
            total_scraped = total_scraped + 1
    
    for link in links:
        if options.check_result:
            try:
                check_link = requests.get(link.get('href'), headers=headers, verify=False, timeout=5)
                if check_link.status_code == 200:
                    print(Fore.GREEN + "[+] " + link.get('href'))
                    if options.filename:
                        print(link.text, file=open(options.filename, "a"))        
                else:
                    print(Fore.RED + "[- " + str(check_link.status_code) + "] " + link.get('href')) 
                    if options.filename:
                        print(link.text, file=open(options.filename, "a"))     
            except:
                print(Fore.RED + "[- 408] " + link.get('href'))        
        else:
            print(Fore.GREEN + "[+] " + link.get('href'))
            if options.filename:
                print(link.text, file=open(options.filename, "a"))        
    return total_scraped             


banner = '''
 CyberDork v1.0                                                            
 Author: tecknoh19
 github: github.com/tecknoh19
 gists:  gist.github.com/tecknoh19

'''

def main():
    print(Fore.CYAN + banner)
    
    if not options.dork:
        dork = input('Enter your dork(s): ')
    else:
        dork = options.dork
    
    if not options.num_results:
        num_results = 10
    else:
        num_results = options.num_results

    total_scraped = do_dorks(dork,num_results)
    
    print(Fore.YELLOW + "[:] Execution complete. Scraped " + str(total_scraped) + " results.")
    if options.filename:
        print(Fore.GREEN + "[+] Output file saved: " + options.filename)
    
try:
    options = get_args()
    main()
except KeyboardInterrupt:
    print(Fore.YELLOW + 'Clean exit by user.')
    exit()
except TimeoutError:
    print(RED + '\n[-] Google got pissed, wait 15 minutes and try again.')
    exit()
