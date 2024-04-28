import os
from os.path import join,isfile,isdir,exists
def make_dir(directory_path):
    os.makedirs(directory_path,exist_ok=True)
    return directory_path
def join_path(*args):
    for i,arg in enumerate(args):
        if i==0:
            path = arg
        else:
            path = join(path,arg)
    return path
def join_make(*args):
    return make_dir(join_path(*args))
def get_data(file_path,default_data=None):
    if not os.path.isfile(file_path):
        safe_dump_to_file(data=default_data or {},file_path=file_path)
    return safe_read_from_json(file_path)
def save_data(data,file_path):
    safe_dump_to_file(data=data,file_path=file_path)
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
class directoryManager(metaclass=SingletonMeta):
    def __init__(self,parent_directory=None,companies_dir=None):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.abs_file = os.path.abspath(__file__)
            self.abs_dir = dirname(self.abs_file)
            self.parent_directory = parent_directory or os.getcwd()
            self.companies_dir =  make_dir(companies_dir or join_path(self.parent_directory,'companies'))
            

def get_companies_dir(parent_directory=None,companies_dir=None):
    if globals().get('dir_mgr') == None:
        dir_mgr = directoryManager(parent_directory=parent_directory,companies_dir=companies_dir)
    return dir_mgr.companies_dir
def get_overall_repository_file_path(parent_directory=None,companies_dir=None):
    return join_path(get_companies_dir(parent_directory=parent_directory,companies_dir=companies_dir),'repository.json')
def get_overall_data(parent_directory=None,companies_dir=None):
    return get_data(get_overall_repository_file_path(parent_directory=parent_directory,companies_dir=companies_dir))
def save_overall_data(overall_data,parent_directory=None,companies_dir=None):
    save_data(data=overall_data,file_path=get_overall_repository_file_path(parent_directory=parent_directory,companies_dir=companies_dir))

def get_company_dir(company_name,parent_directory=None,companies_dir=None):
    return join_make(get_companies_dir(parent_directory=parent_directory,companies_dir=companies_dir),company_name.replace(' ','_'))
def get_company_repository_file_path(company_name):
    return join_path(get_company_dir(company_name),'repository.json')
def get_company_repository_data(company_name):
    return get_data(get_company_repository_file_path(company_name))
def save_company_repository_data(repo_data,company_name):
    save_data(data=repo_data,file_path=get_company_repository_file_path(company_name))
    
def get_company_html_data_dir(company_name):
    return join_make(get_company_dir(company_name),'html_data')
def get_company_html_data_file_path(business_name,data_type=None):
    return join_path(get_company_html_data_dir(company_name),f'{data_type or ""}_html_data.txt')
def get_company_html_data(company_name,data_type=None):
    return get_data(get_company_html_data_file_path(company_name,data_typ=data_type))
def save_company_html_data(html_data,company_name,data_type=None):
    save_data(data=html_data,file_path=get_company_html_data_file_path(company_name,data_typ=data_type))

def get_contact_dir(company_name,contact_name):
    return join_make(get_company_dir(company_name),contact_name.replace(' ','_'))
def get_contact_repository_file_path(company_name,contact_name):
    return join_path(get_contact_dir(company_name,contact_name),'repository.json')
def get_contact_repository_data(company_name):
    return get_data(get_contact_repository_file_path(company_name,contact_name))
def save_contact_repository_data(repo_data,company_name):
    save_data(data=repo_data,file_path=get_contact_repository_file_path(company_name,contact_name))

def get_contact_html_data_dir(company_name,contact_name):
    return join_make(get_contact_dir(company_name,contact_name),'html_data')
def get_contact_html_data_file_path(company_name,contact_name,data_type=None):
    return join_path(get_contact_html_data_dir(company_name,contact_name),f'{data_type or ""}_html_data.txt')
def get_contact_html_data(company_name,contact_name,data_type=None):
    return get_data(get_contact_html_data_file_path(company_name,contact_name,data_type=data_type))
def save_contact_html_data(html_data,company_name,data_type=None):
    save_data(data=html_data,file_path=get_contact_html_data_file_path(company_name,contact_name,data_type=data_type))

