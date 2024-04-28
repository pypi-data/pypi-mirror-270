from pyperclip import *
import re,os,json,os,clipboard,time
import pandas as pd
from abstract_utilities import *
from os.path import join,isfile,isdir,exists
from abstract_distances.word_compare import *
from datetime import datetime
from .contacts_directory import *
def get_closest_headers(list_1,headers):
    closest_js = {key:"" for key in list_1}
    for key,values in closest_js.items():
        for comp_key in headers:
            if comp_key.lower() == key:
                closest_js[key]=comp_key
                break
        if closest_js[key] == "":
            matches = {}
            for comp_key in headers:
                if comp_key not in list(closest_js.values()):
                    for char in key:
                        if char in comp_key.lower():
                            if comp_key not in matches:
                                matches[comp_key]=[]
                            if len(matches[comp_key])==0:
                                matches[comp_key].append('')
                            if matches[comp_key][-1]+char in comp_key.lower():
                                matches[comp_key][-1]+=char
                            else:
                                matches[comp_key].append(char)
            for header,values in matches.items():
                len_header = len(header)
                highest=[0,'']
                for val in values:
                    if len(val)>highest[0]:
                        highest=[len(val),val]
                matches[header]={'perc':highest[0]/len_header,'value':highest[1]}
            highest=[0,'']
            for header,val in matches.items():
                if val['perc']>highest[0]:
                    highest=[val['perc'],header]
            closest_js[key] = get_most_original_from_ls(highest[-1],headers, closest_js.values())
    return closest_js
def await_copy(prompt='awaiting clipboard action',clip='null'):
    """ Wait for the clipboard content to change and return the new content. """
    print(prompt)
    clipboard.copy(clip)
    spam = clipboard.paste()
    while True:
        time.sleep(1)
        if clipboard.paste() != spam:
            return clipboard.paste()
def is_about_page(url):
    for types in ['about','contact']:
        for dash in ['_','-','']:
            if f'{types}{dash}us' in url:
                return True
def get_all_names(company_name,dicts):
    names = []
    for i,name in enumerate(dicts['Full Name']):
        if dicts['Organization'][i] == company_name:
            names.append(name)
    return names
def extract_pattern(text, pattern):
    """
    Extracts email addresses from provided text using a list of regex patterns.
    """
    values = re.findall(pattern, text, re.IGNORECASE)
    if values:
        return values  # Returns list of emails as soon as any valid pattern matches
    return []  # Return an empty list if no patterns match
def list_and_set(list_obj):
    return list(set(list_obj))
def get_all_search_info(company_name,full_name):
    dict_=get_repository_data(company_name,full_name)
    for each in ["email address","phone number","cell phone","linkedin","resume"]:
        search = company_name+','+'california'+','+full_name+','+each
        url = f"https://www.google.com/search?q={search.replace(' ','+')}"
        print(url)
        html_file_path = get_html_data_file_path(company_name,full_name,each)
        j=0
        if not os.path.isfile(html_file_path):
            while True:
                if os.path.isfile(html_file_path):
                    html_file_path = get_html_data_file_path(company_name,full_name,f"{each}_{j}")
                if not os.path.isfile(html_file_path):
                    break
                j+=1
            get_url(url,html_file_path)
            dict_ = get_all_contact_info(read_from_file(html_file_path),dict_)
            save_repository_data(dict_,company_name,full_name)
    return dict_
def find_email_pattern(email,company_name,company_type):
    local_folder = make_local_folder(company_type)
    dicts = create_js_from_read(local_folder)
    names = get_all_names(company_name,dicts)
    for name in names:
        name_spl = name.split(' ')
        first,last = name_spl[0],name_spl[-1]
        pattern, domain = derive_email(first, last, email)
        if pattern != 'unknown':
            return pattern, domain
    return pattern, domain
def get_all_contact_info(string,dicts):
    info_types={"email":[r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b',r'^\S+@\S+\.\S+$'],
    "phones":[r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'],
    "city":[r'([A-Z\s]+)\s\d{5}(?:[-\s,]*\d{5})*']}
    #"urls":[r'\b(?:http|https):\/\/(?:www\.)?[a-zA-Z0-9\-_]+(?:\.[a-zA-Z]{2,})+(?::\d{2,5})?(?:\/[^\s]*)?\b']}
    for info_type,patterns in info_types.items():
        if info_type not in dicts:
            dicts[info_type]=[]
        for pattern in patterns:
            pat= extract_emails(string, pattern)
            dicts[info_type]+=pat
            dicts[info_type]= [obj for obj in list_and_set(dicts[info_type]) if ((not is_number(obj) and 'google.com' not in obj))]
    if "urls_js" not in dicts:
        dicts["urls_js"]={}
    urls = [url for url in list_and_set(extract_urls(string)) if 'google' not in url]
    for url in urls:
        url_pieces = url_to_pieces(url)
        domain =url_pieces[1].replace('www.','')
        if 'urls_js' not in dicts:
            dicts['urls_js'] = {}
        if domain not in dicts['urls_js']:
            dicts['urls_js'][domain]=[]
        if url not in dicts['urls_js'][domain]:
            dicts['urls_js'][domain].append(url)
    return dicts
def scrape_urls(company_name,full_name):
    dict_=get_contact_repository_data(company_name,full_name)
    business_dict =get_company_repository_data(company_name)
    list1 = list(dict_['urls_js'].keys())
    list2 = [company_name.replace(' ','').lower()]
    closest_site = list(get_closest_headers(list2,list1).values())[0]
    if closest_site:
        if 'urls' not in business_dict:
            business_dict['urls']={}
        if closest_site not in business_dict['urls']:
            business_dict['urls'][closest_site]=[]
        if 'scraped_list' not in business_dict:
            business_dict['scraped_list'] = []
        for url in dict_['urls_js'][closest_site]:
            if url not in business_dict['urls'][closest_site]:
                business_dict['urls'][closest_site].append(url)
                if url not in business_dict['scraped_list'] and is_about_page(url):
                    try:
                        print(f"getting {url}")
                        url_pieces = url_to_pieces(url)
                        domain_pieces = url_pieces[2].replace('/','_')
                        url_data_file_path=get_company_html_data_file_path(company_name,domain_pieces)
                        get_url(url,url_data_file_path)
                        dict_ = get_all_search_info(get_company_html_data(url_data_file_path),dict_)
                        save_contact_repository_data(dict_,company_name,full_name)
                        business_dict['scraped_list'].append(url)
                    except:
                        pass
        save_company_repository_data(business_dict,company_name)
def derive_email(first, last, email):
    """ Derive the email convention based on a first name, last name, and a sample email. """
    domain = email.split('@')[1]
    local_part = email.split('@')[0]
    pattern = ""
    if local_part == f"{first[0].lower()}{last.lower()}":
        pattern = "{f}{l}"
    elif local_part == f"{first.lower()}{last.lower()}":
        pattern = "{ff}{l}"
    elif local_part == f"{first.lower()}":
        pattern = "{ff}"
    elif local_part == f"{first.lower()}.{last.lower()}":
        pattern = "{ff}.{l}"
    elif local_part == f"{first.lower()}{last[0].lower()}":
        pattern = "{ff}{ll}"
    elif local_part == f"{first[0].lower()}.{last.lower()}":
        pattern = "{f}.{l}"
    else:
        pattern = "unknown"

    return pattern, domain

def get_company_emails(company_name,full_name,company_type):
    overall_data = get_overall_data()
    dict_=get_contact_repository_data(company_name,full_name)
    for email in dict_['email']:
        company_domain = os.path.splitext(email.split('@')[-1])[0]
        if email not in make_list(overall_data.get(company_name,{}).get('emails',{})):
            for part_name in company_name.split(' '):
                if part_name.lower() in company_domain or company_domain == '':
                    company_domain = company_domain.replace(part_name,'')
                    if company_name not in overall_data:
                        overall_data[company_name] = {"patterns":[],"emails":[]}
                    if email not in overall_data[company_name]["emails"]:
                        overall_data[company_name]["emails"].append(email)
                    if company_domain == '':
                        break
                    pattern, domain = find_email_pattern(email,company_name,company_type)
                    if pattern not in overall_data[company_name]["patterns"]:
                        overall_data[company_name]["patterns"].append(pattern)
                    print(f'found {company_name} email: {email} for {full_name}')
                    save_overall_data(overall_data)
