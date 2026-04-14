
import random
import requests
import time

Z = '\033[1;31m' #احمر
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
a1 = '\x1b[1;31m'  # أحمر
a2 = '\x1b[1;34m'  # أزرق
a3 = '\x1b[1;32m'  # أخضر
a4 = '\x1b[1;33m'  # أصفر
a5 = '\x1b[38;5;208m'  # برتقالي
a6 = '\x1b[38;5;5m'  # أرجواني
a7 = '\x1b[38;5;13m'  # وردي
a8 = '\x1b[1;30m'  # أسود
a9 = '\x1b[1;37m'  # أبيض
a10 = '\x1b[38;5;52m'  # بني
a11 = '\x1b[38;5;8m'  # رمادي
a12 = '\x1b[38;5;220m'  # ذهبي
a13 = '\x1b[38;5;7m'  # فضي
a14 = '\x1b[38;5;153m'  # أزرق فاتح
a15 = '\x1b[38;5;18m'  # أزرق داكن
a16 = '\x1b[38;5;48m'  # أخضر فاتح
a17 = '\x1b[38;5;22m'  # أخضر داكن
a18 = '\x1b[38;5;196m'  # أحمر فاتح
a19 = '\x1b[38;5;88m'  # أحمر داكن
a20 = '\x1b[38;5;226m'  # أصفر فاتح
a21 = '\x1b[38;5;136m'  # أصفر داكن
a22 = '\x1b[38;5;216m'  # برتقالي فات
a23 = '\x1b[38;5;166m'  # برتقالي داكن
a24 = '\x1b[38;5;234m'  # أرجواني فاتح
a25 = '\x1b[38;5;91m'  # أرجواني داكن
a26 = '\x1b[38;5;205m'  # وردي فاتح
a27 = '\x1b[38;5;161m'  # وردي داكن
a28 = '\x1b[38;5;236m'  # أسود فاتح
a29 = '\x1b[38;5;233m'  # أسود داكن
a30 = '\x1b[38;5;255m'  # أبيض فاتح
a31 = '\x1b[38;5;231m'  # أبيض داكن
a32 = '\x1b[38;5;180m'  # بني فاتح
a33 = '\x1b[38;5;94m'  # بني داكن
a34 = '\x1b[38;5;252m'  # رمادي فاتح
a35 = '\x1b[38;5;246m'  # رمادي داكن
a36 = '\x1b[38;5;228m'  # ذهبي فاتح
a37 = '\x1b[38;5;172m'  # ذهبي داكن
a38 = '\x1b[38;5;188m'  # فضي فاتح
a39 = '\x1b[38;5;247m'  # فضي داكن
a40 = '\x1b[0;34m'  # أزرق سماوي
print(f"""{a5} أهـلاً وسـهـلاً بـك الـمـطـور اداه SF حقوق SF
{F}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{Z}┃  {a22} كـلـكـم اخـوانـي/خـواتـي
{Z}┃ ---------------------
{Z}┃  {a23}𝚃𝙾𝙾𝙻 𝙰𝙲𝙲𝚄𝙾𝙽𝚃𝚂
{Z}┃ ----------------------
{Z}┃  {a37} CH : @SF7SF0
{Z}┃ ----------------------
{Z}┃  {a38}Me : @SF7SF0
{F}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
bot_token = input(a30+" َ𝗧𝙾𝙺َ𝙴َ𝙽ِ: خلي التوكن"+a14).strip()
chat_id = input(a30+" 𝗶َ𝘿: خلي الايدي"+a26).strip()


domains = ["gmail.com", "hotmail.com", "yahoo.com", "outlook.com","mohmal.in","yopmail.com",]


passwords = ["123456", "1234567890", "123456789", "11223344","aa11bb22","abc123","abcde12345","12344321","aa11bb22cc33","112233aabbcc",]
klisheh = """
حـسـاب مـرتـب مـن SF
┏━━━━━━━━━━━━━━━━━━
┊‌‎‌‎٭٭> 𝗜𝗗: {user}
┊‌‎‌‎٭٭> 𝗣𝗔𝗦𝗦: {password}
┊‌‎‌‎٭٭> 𝗧𝗥𝗨𝗘 𝗜𝗡𝗙𝗢 ✔
┗━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━
┊‌‎‌‎==> https://t.me/DEW_Pess
┊‌‎‌‎==> @SF7SF0
┗━━━━━━━━━━━━━━━━━━
"""

def generate_email():
    username = "".join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=8))
    domain = random.choice(domains)
    return f"{username}@{domain}"


def generate_phone():

    area_code = random.randint(100, 999)
    exchange_code = random.randint(100, 999)
    subscriber_number = random.randint(1000, 9999)
    return f"+1 ({area_code}) {exchange_code}-{subscriber_number}"


def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, data=payload)

print(Z+'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
print(a5+" اخـتـار الـطـريـقـة الـي تـريـدهـا")
print(Z+'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
print(a6+"1 - بريد إلكتروني + باسورد")
print(Z+'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
print(a19+"2 - رقم هاتف + باسورد")
print(Z+'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
choice = input(a12+"أدخل رقم الاختيار: "+a16).strip()

if choice == "1":
    method = "email"
elif choice == "2":
    method = "phone"
else:
    print("❌ اختيار غير صحيح!")
    exit()


print(a40+" جاري الصيد ادات مدفوعة SF SF"+a17)


counter = 0

while True:
    if method == "email":
        user = generate_email()
    else:
        user = generate_phone()

    password = random.choice(passwords)


    time.sleep(random.uniform(0.5, 2))


    if random.random() < 0.9:
        print(f"❌ {user} | {password}")
    else:
        counter += 1
        if counter == 50:
            counter = 0
            message = klisheh.format(user=user, password=password)
            send_to_telegram(message)
            print(f"✔✓✔: {user} | {password}")

