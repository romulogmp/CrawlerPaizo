import requests
import urllib3
from PathfinderFunctions import change_crawler_session, soup_function, get_file

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

path_to_download_tag = 'r=true'
file_link_tag = '.zip'
url_download_list = list()
url_login = 'https://paizo.com/cgi-bin/WebObjects/Store.woa/wa/DirectAction/signIn?path=paizo'
url_account_files = 'https://paizo.com/paizo/account/assets'
data = {'e': 'E-MAIL', 'zzz': 'PASSWORD'}

session = requests.Session()
holder = change_crawler_session(url_login, data, url_account_files, session)
soup = soup_function(holder)

for link in soup.find_all('a'):
    if link.get('href') is not None and path_to_download_tag in link.get('href'):
        url_download_list.append(link)

for link in url_download_list:
    new_holder = session.get(link.get('href'))
    soup_var = soup_function(new_holder)
    for inner_link in soup_var.find_all('a'):
        get_file(inner_link, file_link_tag, session)
