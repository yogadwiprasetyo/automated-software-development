# IMPORT MODULE
import pyautogui as p
import time as t
from base64 import b64decode

# membuka browser
def membuka_browser():
    t.sleep(1)
    # p.press("win", interval=0.3)
    p.click(x=360, y=749,duration=1)
    # p.typewrite("firefox", interval=0.2)
    # p.press("enter")

# membuka tab baru
def tab_baru():
    t.sleep(5)
    p.hotkey("ctrl","t")

# membuka website
def membuka_website(website):
    tab_baru()
    t.sleep(1) 
    # p.hotkey("ctrl", "e")
    p.typewrite(website,interval=0.05)
    p.press("enter")

# decode username
def dec_un():
    f = open("u.txt", "r")
    enc_un = b64decode(f.read())
    un = enc_un.decode()
    f.close()

    return str(un)

# decode password
def dec_pw():
    f = open("p.txt", "r")
    enc_pw = b64decode(f.read())
    pw = enc_pw.decode()
    f.close()

    return str(pw)

# masuk website
def login(pUsrnm,pPw,pLgn):
    t.sleep(5)
    username = dec_un()
    password = dec_pw()
    p.click(pUsrnm,duration=0.25)
    p.typewrite(username,interval=0.1)
    p.click(pUsrnm,duration=0.25)
    p.click(pPw,duration=0.25)
    p.typewrite(password,interval=0.1)
    p.click(pLgn,duration=0.25)

# di dalam website sedang dalam pengembangan
def in_website(user):
    t.sleep(5)
    if int(user) == 1:
        pass
    elif int(user) == 2:
        nilaiSemesterAktif = 766,418
        p.click(x=756, y=448, duration=0.50)
        p.click(nilaiSemesterAktif,duration=0.25)
        t.sleep(20)
        p.click(x=64, y=162,duration=0.25)
    else:
        print('ERROR: user tidak diketahui')

# keluar website dan browser dalam pengembangan
def close(user):
    t.sleep(1)
    if int(user) == 1:
        profile = 882, 165
        keluarWeb = 729, 452
        p.click(profile,duration=1)
        p.click(keluarWeb,duration=1)
    elif int(user) == 2:
        keluarApss = 738,544
        keluarBrowser = 11,10
        p.click(keluarApss,duration=1)
        p.click(keluarBrowser, duration=1)
        p.click(x=737, y=464,duration=1)
    else:
        print('ERROR: user tidak diketahui')
   
# memilih untuk membuka webkuliah atau appsunas
def web_apps():
    to = input("WebKuliah=1, AppsUnas=2: ")
    membuka_browser()
    if int(to) == 1:
        website = "https://webkuliah.unas.ac.id/login/index.php"
        posUsername = 673, 487
        posPassword = 674, 539
        posLogin = 775, 620
        membuka_website(website)
        login(posUsername,posPassword,posLogin)
        in_website(to)
        close(to)
    elif int(to) == 2:
        website = "apps.unas.ac.id"
        posUsername = 536, 311
        posPassword = 531, 346
        posLogin = 486, 401
        membuka_website(website)
        login(posUsername,posPassword,posLogin)
        in_website(to)
        close(to)

# menjalankan script
web_apps()



                    # DALAM MASA BUILDING #

# ALGORITMA ATAU TUJUAN WEB KULIAH
# klik dashboard
# klik myCourse
# memilih pelajaran
# klik pelajaran yang dipilih
# ke tempat forum berada
# klik forum dengan membuat tab baru
# klik dashboard

# KEBUTUHAN FUNGSI #
# FUNGSI MENU UTAMA
# mempunyai dua pilihan
# pelajaran atau exit
# pelajaran = MENU MATA KULIAH
# exit = logout


# FUNGSI MENU MATA KULIAH
# memilih mata kuliah
# masuk MENU FORUM

# FUNGSI MENU FORUM
# memilih forum minggu ke-n
# membuka forum dengan tab baru
# kembali ke MENU UTAMA

# POSISI YANG DIBUTUHKAN
#dashboard = x=82, y=381
#my course = x=82, y=377
# 1 = x=201, y=440
# 2 = x=187, y=481
# 3 = x=200, y=522
# 4 = x=197, y=564
# 5 = x=190, y=598
# 6 = x=199, y=641
# 7 = x=212, y=706
# 8 = x=172, y=753
# keforum = x=1014, y=530
# forumGanjil1 = x=274, y=279
# openForumNewTab =
# dashboard = x=82, y=381
# forum3 = x=274, y=345
# openForumNewTab =
# dashboard = x=82, y=381
# forum5 = x=274, y=413
# openForumNewTab =
# dashboard = x=82, y=381
# forum10 = x=274, y=479
# openForumNewTab = 
# dashboard = x=82, y=381
# forum12 = x=274, y=544
# openForumNewTab =
# dashboard = x=82, y=381 
# forum14 = x=274, y=611
# openForumNewTab = 
# dashboard = x=82, y=381
# forum15 = x=274, y=677
# openForumNewTab = 
#dashboard = x=82, y=381
# profile = x=882, y=165
# logout = x=729, y=452

# TESTNG   
# p.click(,duration=1)
# # p.rightClick()
# p.drag(1015,520, duration=5)
# p.scroll(10,x=1015,y=800)
print(p.position())

                    # AKHIR DALAM MASA BUILDING #

# APPS UNAS
# POSISI MENU APPS UNAS
# transkrip = 264,250
# historiNilai = 256,293
# jadwalPribadi = 249,376
# mengisiKrs = 254,417
# kehadiranKuliah = 763,335
# nilaiSemesterAktif = 766,418
# dataKeuangan = 767,462
# keluar = 765,547
# dataPosisi = [transkrip,historiNilai,jadwalPribadi,mengisiKrs,kehadiranKuliah,nilaiSemesterAktif,dataKeuangan,keluar]