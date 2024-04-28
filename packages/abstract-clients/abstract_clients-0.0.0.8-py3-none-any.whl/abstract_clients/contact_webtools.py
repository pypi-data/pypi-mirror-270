from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re,requests,os
from abstract_utilities import *
def extract_urls(text):
    # Initialize BeautifulSoup object with the content of the web page
    soup = BeautifulSoup(text, 'lxml')
    # Find all 'a' tags, then extract the 'href' attribute
    urls = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith('http')]
    return urls
def get_source(url):
    if 'https://' not in url:
        url = f"https://{url}"
    response = requests.get(url)
    return response.text
def url_to_pieces(url):
    try:
        match = re.match(r'^(https?)?://?([^/]+)(/[^?]+)?(\?.+)?', url)
        if match:
            protocol = match.group(1) if match.group(1) else None
            domain = match.group(2) if match.group(1) else None
            path = match.group(3) if match.group(3) else ""  # Handle None
            query = match.group(4) if match.group(4) else ""  # Handle None
    except:
        print(f'the url {url} was not reachable')
        protocol,domain,path,query=None,None,"",""
    return protocol, domain, path, query
def get_all_links(domain):
    href_list = set([domain])  # Use a set to avoid duplicates
    to_visit = set([domain])
    while to_visit:
        current_url = to_visit.pop()
    
        soup = BeautifulSoup(get_source(current_url), 'html.parser')
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            if href.startswith('/'):
                href = f"{domain.rstrip('/')}/{href.lstrip('/')}"
            if href.startswith(domain) and href not in href_list and 'google' not in href:
                href_list.add(href)
                to_visit.add(href)  # Add new URLs to visit
        
    return list(href_list)
def get_url(url,html_file_path=None):
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    def main():
        # Setup Chrome WebDriver
        driver = webdriver.Chrome(options=chrome_options)
        try:
          # Initialize WebDriver
            # Open the webpage
            driver.get(url)
            # Get page source
            page_source = driver.page_source
            if html_file_path:
                write_to_file(contents=str(page_source),file_path=html_file_path)
            # Print the page source
        finally:
            # Close the browser
            driver.quit()
        return page_source
    return main()
def open_get_source(url):
    os.system(f"firefox view-source:{url}")
def get_inners(content):
    track_js =  {'<':-1,'>':1}
    char_ls=['']
    char_count=0
    for char in content:
        
        if char in list(track_js.keys()):
            char_count += track_js[char]
            if char_ls[-1] !='':
                char_ls[-1] = eatAll(char_ls[-1],[' ','',','])
                char_ls.append('')
        elif char_count ==0:
            char_ls[-1]+=char
    return clean_list(char_ls)
