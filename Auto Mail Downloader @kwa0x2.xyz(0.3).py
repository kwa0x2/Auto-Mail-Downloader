from imbox import Imbox
import colorama
colorama.init()
from colorama import Fore, Style, Back
colorama.init()
import os
import ssl
import traceback
import requests
import sys
from getpass import getuser

class ConsoleColors: 
        PURPLE    = '\033[95m'
        CYAN      = '\033[96m'
        DARKCYAN  = '\033[36m'
        BLUE      = '\033[94m'
        GREEN     = '\033[92m'
        YELLOW    = '\033[93m'
        RED       = '\033[91m'
        BOLD      = '\033[1m'
        DEFAULT   = '\033[0m'
        WHITE     = '\033[37m'

color = ConsoleColors() 

local_version_path = f"C:/Users/{getuser()}/Documents/Auto_Mail_Downloader_local_version.txt"

if not os.path.exists(local_version_path): 
            with open(local_version_path,"w") as f: 
                f.write("0.2") 

try:
                os.system("cls") 
                version_link = "https://raw.githubusercontent.com/kwa0x2/Auto-Mail-Downloader/main/version.txt" 
                r = requests.get(version_link) 
                response_version = r.content.decode() 
                with open(local_version_path,"r") as g: 
                    local_vers = g.read() 
                    if float(local_vers) < float(response_version): 
                            guncel_version = input(f"{color.BOLD}{color.GREEN}Güncel Değil Güncel Versiyonu İndirmek İstermisiniz Y/N: {color.DEFAULT}")
                            if  guncel_version=="Y" or guncel_version=="y":
                                print(f"{color.BOLD}{color.PURPLE}Güncelleniyor...")
                                with open(local_version_path,"w") as f: 
                                    f.write(str(response_version)) 
                                new_dowload_link = "https://github.com/kwa0x2/Auto-Mail-Downloader/raw/main/Auto_Mail_Downloader_by_kwa.exe" 
                                r = requests.get(new_dowload_link, allow_redirects=True) 
                                with open(f"Auto Mail Downloader @kwa0x2.xyz (0.3).exe","wb") as exe: 
                                    exe.write(r.content)
                                print(f"{color.BOLD}{color.YELLOW}Başarıyla Güncellendi{color.DEFAULT}")
                                os.startfile(f"Auto Mail Downloader @kwa0x2.xyz (0.3).exe")
                                sys.exit(0) 

                    elif float(local_vers) > float(response_version):
                        
                        raise TypeError(input(f"{color.RED}HATA! Local Version Değeri Github Repositories Version Değerinden Büyük Olamaz {color.BOLD}{color.DARKCYAN}" + local_version_path + f"{color.DEFAULT}{color.RED} Konumundaki TXT Dosyasının İçindeki Metini 0.1 Yap"))
    
                    else: 
                            os.system("cls")
                            print(f"{color.BOLD}{color.WHITE}Durum: " f"{color.BOLD}{color.CYAN}Güncel!{color.DEFAULT}")
                            print()
except FileNotFoundError: 
                        version_error = input(f"{color.PURPLE}Program açıldıktan sonra "+ local_version_path +f" silme!\nTekrar Oluşturmak İstermisin: {color.DEFAULT}")
                        if version_error=="Y" or version_error=="y":
                            with open(local_version_path,"w") as f:
                                    f.write("0.2")


colorama.init()
host1 = "imap.gmail.com"

print(Fore.MAGENTA + f"{color.BOLD}Code by kwa")

print(f"""{color.RED}{color.BOLD}
!!!
Program sadece gmail ile çalışır.
Girilecek şifrenin uygulama şifresi olması gerekmektedir aksi halde çalışmaz!
Uygulama şifresi almak için :
https://www.youtube.com/watch?v=h_NP3pcvkAg
bu videonun 04:22 dakikasına kadar izleyebilirsiniz
!!!
""")
tekrar = "y"
while tekrar=="Y" or tekrar=="y":
    print(Fore.WHITE)
    nameMail=input(f"{color.BOLD}{color.BLUE}Mail Giriniz: {color.BOLD}{color.WHITE}") 
    passMail=input(f"{color.BOLD}{color.BLUE}Mail Şifre Giriniz: {color.BOLD}{color.WHITE}") 


    colorama.init()
    print(Fore.WHITE)

    print("""

    \033[94m[\033[97m01\033[94m] SPAM
    \033[94m[\033[97m02\033[94m] GENEL

    """)
    print(Fore.WHITE)
    spam_genel=input(f"{color.BOLD}{color.DARKCYAN}[" + nameMail + f"]{color.BOLD}{color.BLUE} İndirilecek Kategori Seçin 01/02: {color.BOLD}{color.WHITE}") 
    downLoct=input(f"{color.BOLD}{color.BLUE}İndirilen Maillerin Toplanacağı Dosya Adı Yazınız: {color.BOLD}{color.WHITE}")
    download_folder = f"C:/Users/{getuser()}/Documents/Auto Mail Downloads/" + downLoct
    if not os.path.isdir(download_folder):
            os.makedirs(download_folder, exist_ok=True)

    if spam_genel=="1" or spam_genel=="01":

    
        bilgi=input(f"{color.BOLD}{color.DARKCYAN}[" + nameMail + f"{color.BOLD}{color.BLUE}] Mailindeki {color.BOLD}{color.DARKCYAN}'Spam' {color.BOLD}{color.BLUE}Bölümüne Gelen Dosyalar {color.BOLD}{color.DARKCYAN}'" + downLoct + f"'{color.BOLD}{color.BLUE} Adlı Dosyaya İndirilsin mi Y/N: {color.BOLD}{color.WHITE}") 
        colorama.init(autoreset=True)

        if bilgi=="Y" or bilgi=="yes" or bilgi=="Yes" or bilgi=="evet" or bilgi=="y" or bilgi=="YES" or bilgi=="yEs" or bilgi=="YEs" or bilgi=="yES" or bilgi=="yeS" or bilgi=="YeS":
            print(Fore.RED + f"{color.BOLD}İndiriliyor..")
            mail = Imbox(host1, username=nameMail, password=passMail, ssl=True, ssl_context=None, starttls=False)
            messages = mail.messages(folder='Spam')

            for (uid, message) in messages:
                mail.mark_seen(uid) 

                for idx, attachment in enumerate(message.attachments):
                        att_fn = attachment.get('filename')
                        download_path = f"{download_folder}/{att_fn}"
                        colorama.init()
                        print(f"{color.BOLD}{color.DARKCYAN}[" + nameMail + f"]{color.BOLD}{color.WHITE} Başarıyla İndirildi: {color.BOLD}{color.DARKCYAN}" +download_path)
                        with open(download_path, "wb") as fp:
                            fp.write(attachment.get('content').read())

            print(F"{color.BOLD}{color.PURPLE}Spam Kutusundaki Tüm Dosyalar Başarıyla İndirildi" + Style.RESET_ALL)
            tekrar = input(f"{color.BOLD}{color.BLUE}Tekrar Yapmak İstermisiniz Y/N: {color.WHITE}")

    if spam_genel=="2" or spam_genel=="02":

        bilgi=input(f"{color.BOLD}{color.DARKCYAN}[" + nameMail + f"{color.BOLD}{color.BLUE}] Mailindeki {color.BOLD}{color.DARKCYAN}'Genel' {color.BOLD}{color.BLUE}Bölümüne Gelen Dosyalar {color.BOLD}{color.DARKCYAN}'" + downLoct + f"'{color.BOLD}{color.BLUE} Adlı Dosyaya İndirilsin mi Y/N: {color.BOLD}{color.WHITE}") 
        colorama.init(autoreset=True)

        if bilgi=="Y" or bilgi=="yes" or bilgi=="Yes" or bilgi=="evet" or bilgi=="y" or bilgi=="YES" or bilgi=="yEs" or bilgi=="YEs" or bilgi=="yES" or bilgi=="yeS" or bilgi=="YeS":
        
            print(Fore.RED + f"{color.BOLD}İndiriliyor..")
            mail = Imbox(host1, username=nameMail, password=passMail, ssl=True, ssl_context=None, starttls=False)
            messages = mail.messages(folder='Inbox')

            for (uid, message) in messages:
                mail.mark_seen(uid) 

                for idx, attachment in enumerate(message.attachments):
                    
                        att_fn = attachment.get('filename')
                        download_path = f"{download_folder}/{att_fn}"
                        colorama.init()
                        print(f"{color.BOLD}{color.DARKCYAN}[" + nameMail + f"]{color.BOLD}{color.WHITE} Başarıyla İndirildi: {color.BOLD}{color.DARKCYAN}" +download_path)
                        with open(download_path, "wb") as fp:
                            fp.write(attachment.get('content').read())

            print(F"{color.BOLD}{color.PURPLE}Genel Kutusundaki Tüm Dosyalar Başarıyla İndirildi" + Style.RESET_ALL)
            tekrar = input(f"{color.BOLD}{color.BLUE}Tekrar Yapmak İstermisiniz Y/N: {color.WHITE}")


