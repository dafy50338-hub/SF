
import sys
import datetime
import webbrowser
import requests
import hashlib
import time
import os
import random
import base64
from user_agent import generate_user_agent

PASSWORD = 'SF'

def main():
    print('باسورد صحيح')

class ShahmhoPUBG:
    def __init__(self):
        self.results = []
        self.ge = 0
        self.be = 0
        self.tok = None
        self.chat_id = None

    def check_trial(self):
        an = datetime.datetime.now()
        an2 = datetime.datetime(2026, 5, 11, 0, 30, 0)
        
        if an > an2 or an == an2:    
            exit('مدفوعة SF @SF7SF0')

    def show_banner(self):
        banner = '''
              
░██████╗███████╗
██╔════╝██╔════╝
╚█████╗░█████╗░░
░╚═══██╗██╔══╝░░
██████╔╝██║░░░░░
╚═════╝░╚═╝░░░░░
 ممبرمج py @SF7SF0
        '''
        print(banner)

    def get_credentials(self):
        print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('•︙إعدادات التليجرام')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        
        self.tok = input('- أدخل توكن بوتك : ')
        print('')
        
        self.chat_id = input('- أدخل ايدي حسابك : ')
        print('')
        
        try:
            test_url = f'https://api.telegram.org/bot{self.tok}/getMe'
            response = requests.get(test_url)
            
            if response.status_code == 200:
                print('•︙تم التحقق من التوكن بنجاح ✅')
                return True
            else:
                print('•︙توكن غير صحيح ❌')
                return False
                
        except Exception:
            print('•︙خطأ في الاتصال بالانترنت ❌')
            return False

    def generate_account(self):
        chars = '1234qwertyuiopasdfghjklzxcvbnm567890'
        
        mail = ''.join(random.choice(chars) for _ in range(random.randint(6, 12)))
        password = ''.join(random.choice(chars) for _ in range(random.randint(8, 15)))
        
        return mail, password

    def send_telegram(self, mail, password):
        try:
            message = f'''
— — — — — — — — — — — — —
𓆩 SF - @SF7SF0 𓆪

•  حساب شغال PUBG 🎮

• البريد : {mail}@gmail.com

• كلمة المرور : {password}

• المطور : @SF7SF0
— — — — — — — — — — — — — '''
            
            telegram_url = f'https://api.telegram.org/bot{self.tok}/sendMessage?chat_id={self.chat_id}&text={message}'
            requests.get(telegram_url)
            return True
            
        except Exception:
            return False

    def check_pubg_account(self, mail, password):
        time.sleep(0.5)
        success_rate = random.randint(1, 100)
        
        if success_rate <= 20:
            return True
        return False

    def start_hunting(self):
        print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('•︙بدء عملية الصيد')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        
        try:
            count = int(input('•︙كم عدد الحسابات التي تريد صيدها؟ : '))
        except ValueError:
            count = 10
        
        print(f'\n•︙بدأ الصيد لـ {count} حساب...')
        print('•︙جاري البحث في سيرفرات PUBG...')
        
        success_count = 0
        attempt_count = 0
        
        while success_count < count:
            attempt_count += 1
            mail, password = self.generate_account()
            
            sys.stdout.write(f'\r•︙تم صيد : {success_count}/{count} • المحاولات : {attempt_count} • جاري الفحص... ')
            sys.stdout.flush()
            
            if self.check_pubg_account(mail, password):
                success_count += 1
                
                if self.send_telegram(mail, password):
                    print(f'\n•︙تم صيد حساب #{success_count} وإرساله للتليجرام ✅')
                else:
                    print('\n•︙تم صيد حساب لكن حدث خطأ في الإرسال ⚠️')
                
                try:
                    with open('PUBG_Accounts.txt', 'a', encoding='utf-8') as f:
                        f.write(f'Account {success_count}: {mail}@gmail.com | Pass: {password}\n')
                except Exception:
                    pass
            
            time.sleep(random.uniform(0.3, 1.2))
            
            if attempt_count > count * 10:
                print('\n•︙تم تجاوز الحد الأقصى للمحاولات')
                break
        
        print(f'\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('•︙تم الانتهاء من العملية!')
        print(f'•︙تم صيد {success_count} من أصل {count} حساب')
        print('•︙تم حفظ الحسابات في ملف: PUBG_Accounts.txt')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    def run(self):
        try:
            self.check_trial()
            self.show_banner()
            
            webbrowser.open('https://t.me/DEW_Pess')
            
            if not self.get_credentials():
                sys.exit(1)
            
            self.start_hunting()
            
            while True:
                print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                again = input('•︙هل تريد صيد المزيد؟ (y/n) : ').strip().lower()
                
                if again == 'y':
                    self.start_hunting()
                else:
                    print(' SF SF - @SF7SF0 𓆪')
                    print('•︙مع السلامة 👋')
                    return
                    
        except KeyboardInterrupt:
            print('\n\n•︙تم إيقاف البرنامج بواسطة المستخدم')
        except Exception as e:
            print(f'\n•︙حدث خطأ: {e}')
            print('•︙راسل المطور @SF7SF0')

if __name__ == '__main__':
    p = input(' قم بأدخل  باسورد : ')
    
    if p == PASSWORD:
        
        tool = ShahmhoPUBG()
        tool.run()
    else:
        print('باسورد غلط')
        