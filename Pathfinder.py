import requests
import urllib3
from PathfinderFunctions import requests_steps, soup_function, get_file

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

path_to_download_tag = 'r=true'
file_link_tag = '.zip'
url_download_list = list()
url_login = 'https://paizo.com/cgi-bin/WebObjects/Store.woa/wa/DirectAction/signIn?path=paizo'
url_account_files = 'https://paizo.com/paizo/account/assets'
data = {'e': 'E-MAIL', 'z': 'PASSWORD'}

s = requests.Session()
holder = requests_steps(url_login, data, url_account_files, s)
soup = soup_function(holder)

for link in soup.find_all('a'):
    if link.get('href') is not None and path_to_download_tag in link.get('href'):
        url_download_list.append(link)

for link in url_download_list:
    new_holder = s.get(link.get('href'))
    soup = soup_function(new_holder)
    for inner_link in soup.find_all('a'):
        get_file(inner_link, file_link_tag, s)
