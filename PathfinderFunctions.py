import zipfile
import io
from bs4 import BeautifulSoup


def soup_function(value_holder):
    page_data = value_holder.text
    inner_soup = BeautifulSoup(page_data, features="html.parser")
    return inner_soup


def format_book_title(title_with_tag):
    title_with_tag = title_with_tag.find('b').text
    title_with_tag = title_with_tag.replace('<b>', '')
    title_with_tag = title_with_tag.replace('</b>', '')
    title_with_tag = title_with_tag.replace(':', '')
    return title_with_tag


def unzip_file(content):
    unzip = zipfile.ZipFile(io.BytesIO(content))
    return unzip


def set_unzip_folder(zipbytes, folder_name):
    zipbytes.extractall('{}'.format(folder_name))


def change_crawler_session(login_path, user_credentials, account_files, current_session):
    current_session.get(login_path)
    current_session.post(login_path, user_credentials)
    return current_session.get(account_files)


def get_file(link_to_file, file_link, current_session):
    if link_to_file.get('href') is not None and file_link in link_to_file.get('href'):
        book_name = format_book_title(link_to_file)
        response = current_session.get(link_to_file.get('href'))
        zip_bin = unzip_file(response.content)
        set_unzip_folder(zip_bin, book_name)

