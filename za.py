import requests
import console
import time
from bottle import route, run, response
import warnings

# ------- SSL hata ayıklaması için
# Yani konsoldan gizlemek için 
def handle_warning(message, category, filename, lineno, file=None, line=None):
    if category == requests.packages.urllib3.exceptions.InsecureRequestWarning:
        pass

warnings.showwarning = handle_warning

with warnings.catch_warnings():
    warnings.simplefilter("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)
    
#---------- Gövde Gösterisi :D -----#
console.set_color(0.0, 0.6, 1.0)
print("""
________              ______              
___  __ \_____ __________  /__ 
__  / / /  __ `/_  ___/_  //_/ 
_  /_/ // /_/ /_  /   _  ,<   
/_____/ \__,_/ /_/    /_/|_|""")
print("")
console.set_color(1.0, 0.5, 0.0)
print("                        ENZA")
console.set_color(1.0, 0.0, 1.0)
print("    Gemiler battı diye")
console.set_color(0.6, 0.0, 0.8)
print("     Acırmı denizin canı..")
print("")
console.set_color()

console.set_color(0.6, 0.0, 0.8)
print("TG: @dark_enza")
print("")
console.set_color()

console.set_color(0.0, 0.6, 1.0)
print("Full Otomatik Yesim-Esim 500MB")
print("")
console.set_color()

# -------------------- eposta belirleme --------------------#
url1 = "https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1"
headers1 = {
    'Host': 'www.1secmail.com'
}
res1 = requests.get(url1, headers=headers1, verify=False)
sonuc1 = res1.json()
eposta = str(sonuc1).strip("['']")
console.set_color(0.0, 1.0, 0.0)
print("[+]Eposta belirlendi:",eposta)
login = eposta
isim, domain = login.split('@')

# ------- belirlenen epostayı isteğe işle ----#
url2 = "https://iweb.yesim.app//v1/auth_email?email=" + eposta + "&version=4.0.8&lang=en&platform=3"
headers2 = {
	'Host': 'iweb.yesim.app'
	}
res2 = requests.post(url2, headers=headers2)
try:
	sonuc2 = res2.json()
	console.set_color(0.0, 1.0, 0.0)
	print("[+]Kod Gönderildi")
except:
	print("[-]Bir Hata meydana Geldi")
	
	
#-------- kodu al ----------#
time.sleep(5)
url3 = "https://www.1secmail.com/api/v1/?action=getMessages&login="+isim+"&domain="+domain
headers3 = {
    'Host': 'www.1secmail.com'
}
res3 = requests.get(url3, headers=headers3, verify=False)
try:
	sonuc3 = res3.json()
	test = sonuc3[0]
	dogrula = test["subject"]
	kod = dogrula.replace('Your Yesim confirmation code: ', '')
	console.set_color(0.0, 1.0, 0.0)
	print("[*]Kod Alındı:",kod)
except:
	print("[-]Alınamadı Tekrar Dene")
	
	
	
#------- Alınan kodu işle ---------#
url4 = "https://iweb.yesim.app/v1/auth_code?code="+kod+"&email="+eposta+"&version=4.1.8&lang=en&platform=3"
headers4 = {
    'Host': 'iweb.yesim.app'
}
res4 = requests.post(url4, headers=headers4)
sonuc4 = res4.json()["sessionId"]




# ------------- Y Coin Çekme -----------#
url5 = "https://api2.yesim.app/code_apply?ref_code&web_key="+sonuc4+"&ref_code=NQVO420&lang=en"
headers5 = {
    'Host': 'iweb.yesim.app'
}

try:
	res5 = requests.get(url5, headers=headers5, verify=False)
	sonuc5 = res5.json() == ['success']
	console.set_color(0.0, 1.0, 0.0)
	print("[+]500MB Eklendi/Added")
except:
	print("Bir Sorun Var Admine Ulaş @dark_enza")
	raise SystemExit()


#--------------- Pay As You Go Aktifle -------#
try:
	dark = requests.get("https://iweb.yesim.app/v1/activate_pay_as_you_go?web_key="+sonuc4+"&lang=en", timeout=5)
	sonuc6 = dark.json() == "Ok"
	console.set_color(0.0, 1.0, 0.0)
	print("[+]KareKod istendi ")
except:
	console.set_color(1.0, 0.0, 0.0)
	print("[-]Karekod Alınamadı")
	print("Bir Sorun Var Admine Ulaş @dark_enza")
	raise SystemExit()


#---------- Kare Kodu Denetle --------#
try:
    dark1 = requests.get("https://iweb.yesim.app/v1/show_my_qrs?web_key="+sonuc4+"&lang=en", timeout=5)
    sonuc7 = dark1.json()["Qrs"]
    console.set_color(0.0, 1.0, 0.0)
    print("[+]KareKod Epostaya Gönderildi")
except:
    console.set_color(1.0, 0.0, 0.0)
    print("[-]KareKod Oluşturulamadı")
    print("Bir Sorun Var Admine Ulaş @dark_enza")
    raise SystemExit()
    
    
#----------- Maili kontrol et ----------#
time.sleep(3)
url8 = "https://www.1secmail.com/api/v1/?action=getMessages&login="+isim+"&domain="+domain
headers8 = {
    'Host': 'www.1secmail.com'
}
res8 = requests.get(url8, headers=headers8, verify=False)
sonuc8 = res8.json()
deger_ara = "Greetings from Yesim!"
for id in sonuc8:
    if id['subject'] == deger_ara:
        deger_id = id['id']
        break
else:
    deger_id = None
    print("[-]KareKod Gelmemiş Kodu Tekrar Çalıştır")
    raise SystemExit()
console.set_color(1.0, 0.5, 0.0)
print("[+]İLGİLİ Mesaj İD Alındı:", deger_id)
time.sleep(0.5)
console.set_color(1.0, 0.0, 1.0)
print("[+]Esim İçİn Tıkla: http://localhost:3169")


#-------- local sunucuda html çalıştır ------#
@route('/')
def generate_html_file():
    
    url9 = "https://www.1secmail.com/api/v1/?action=readMessage&login=" + isim + "&domain=" + domain + "&id=" + str(deger_id)
    res9 = requests.get(url9, verify=False)
    sonuc9 = res9.json()

    html_content = "<html><body>"
    html_content += "<h1>" + sonuc9["subject"] + "</h1>"
    html_content += "<p>" + sonuc9["body"] + "</p>"
    html_content += "</body></html>"

    return html_content

run(host='localhost', port=3169, quiet=True)
#------- Son -------#
