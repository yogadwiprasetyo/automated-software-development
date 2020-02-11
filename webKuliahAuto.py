######################################### START ##########################################

########### AWAL MODULE ###########
# Import Module
from splinter import Browser
from base64 import b64decode
########### AKHIR MODULE ###########

# Membuat Instance dari class Browser
# digunakan untuk berinteraksi dengan web
browser = Browser()

############################ AWAL LOGIN ###############################
# decode username
def dec_un():
    file = open("u.txt", "r")
    enc_un = b64decode(file.read())
    un = enc_un.decode()
    file.close()
    return str(un)

# decode password
def dec_pw():
    file = open("p.txt", "r")
    enc_pw = b64decode(file.read())
    pw = enc_pw.decode()
    file.close()
    return str(pw)

# login
def login():
    # mengunjungi web kuliah
    # mengisi username
    # mengisi password
    # login
    browser.visit('https://webkuliah.unas.ac.id/login/index.php')
    username = dec_un()
    password = dec_pw()
    browser.find_by_id('username').fill(username)
    browser.find_by_id('password').fill(password)
    browser.find_by_id('loginbtn').click()
############################ AKHIR LOGIN ###############################


############################ DALAM MASA PENGEMBANGAN | AWAL WEBKULIAH ###############################
# AWAL Fungsi menu_web_kuliah | DALAM MASA PENGEMBANGAN
# menampilkan pilihan pada on_web_kuliah
def menu_web_kuliah():
    print('''
            ####### MATA KULIAH #######
            # 1. Algoritma            #
            # 2. Aljabar              #
            # 3. Bahasa Indonesia     #
            # 4. Bahasa Inggris       #
            # 5. Fisika               #
            # 6. Kalkulus I           #
            # 7. PKN                  #
            # 8. PTKI                 #
            # 9. Praktikum Algo       #
            # 10. Praktikum Fisika    #

            # tekan 'q' untuk Log out #
            ###########################''')
# AKHIR Fungsi menu_web_kuliah | DALAM MASA PENGEMBANGAN

# AWAL Fungsi menu_one_lesson
# menampilkan pilihan pada in_one_lesson
def menu_one_lesson(judul):
    print('''
            # Forum {} #

                1. Materi Kuliah Dokumen           
                2. Materi Video E-learning
                3. Tugas Kuliah-1
                4. Tugas Kuliah-2
                5. Perkuliahan Online
                6. UTS
                7. UAS    

                tekan 'b' ke Dashboard
                tekan 'q' Keluar Browser/Logout

            # Forum {} #'''.format(judul,judul))
# AKHIR Fungsi menu_one_lesson

# AWAL Fungsi error_input
# memberi pesan error input
def warning():
    print('WARNING: input tidak diketahui, silahkan isi kembali!')
# AKHIR Fungsi error_input

# AWAL Fungsi on_web_kuliah Utama | DALAM MASA PENGEMBANGAN
# menampilkan pilihan on_web_kuliah
def on_web_kuliah():
    # Inisialisasi Variabel
    # awal link dari mata kuliah
    linkCourse = 'https://webkuliah.unas.ac.id/course/view.php?'

    # Data List | DALAM MASA PENGEMBANGAN
    # data links dengan key mata kuliah masing-masing
    DataKeyMataKuliah = [
    'id=153898','id=153909','id=154719',
    'id=153924','id=154067','id=154079',
    'id=151110','id=154115','id=154126','id=150274']

    # looping 
    # agar menampilkan menu_web_kuliah terus menerus
    # sampai keadaan False
    while True:
        menu_web_kuliah()

        # Input User
        # menyimpan value dari input pada variabel userInLesson
        userOnWeb = input('''pilih nomer mata kuliah: ''')
        
        # Kondisi
        # jika userOnWeb = 'q', lakukan logout
        # selain syarat diatas, abaikan lalu beri pesan warning
        # kembali ke input user
        if userOnWeb >= 'a' and userOnWeb <= 'z':
            if userOnWeb == 'q':
                logout()
            warning()
            continue
        elif userOnWeb >= 'A' and userOnWeb <= 'Z':
            warning()
            continue
        elif int(userOnWeb) == 0 or int(userOnWeb) > 10:
            warning()
            continue
        elif userOnWeb == '':
            warning()
            continue

        # Proses 
        # mengambil datakeymatakuliah dengan indeks, input user dikurang satu
        # lalu simpan ke dalam variabel linkPilihan
        # lakukan penggabungan antara link parameter dengan variabel linkPilihan
        # lalu simpan hasil penggabungan pada variabel linkReady
        # klik link dengan parameter variabel linkReady
        # ambil judul mata kuliah
        # lalu masuk ke fungsi in_one_lesson 
        keyPilihanUser = DataKeyMataKuliah[int(userOnWeb)-1]
        linkReady = linkCourse + keyPilihanUser
        browser.links.find_by_href(linkReady).click()
        judul = browser.find_by_css('.page-header-headings > h1:nth-child(1)').text
        in_one_lesson(linkReady,judul)
# AKHIR Fungsi on_web_kuliah Utama | DALAM MASA PENGEMBANGAN

# AWAL Fungsi Di Dalam Satu Mata Kuliah
# menampilkan menu pada satu mata kuliah
def in_one_lesson(link,judul):
    # Data List
    # menaruh Datakeysection
    # untuk dipakai link parameter
    DataKeySection = [
    '#section-3', '#section-4', '#section-5',
    '#section-6','#section-8','#section-9','#section-10'
    ]

    # looping
    # agar menampilkan on_web_kuliah terus menerus
    # sampai keadaan False
    while True:
        menu_one_lesson(judul)

        # Input User
        # menaruh value input ke dalam variabel userInLesson
        userInLesson = input('pilih nomer forum: ')

        # Kondisi
        # jika userInLesson == 'b', masuk ke fungsi on_web_kuliah 
        # jika userInLesson == 'q', masuk ke fungsi logout 
        # selain syarat diatas, abaikan lalu beri pesan warning
        # kembali ke input user
        if userInLesson >= 'a' and userInLesson <= 'z':
            if userInLesson == 'b':
                dashboard = 'ul.list-group:nth-child(2) > li:nth-child(1) > a:nth-child(1)'
                browser.find_by_css(dashboard).click()
                on_web_kuliah()
            elif userInLesson == 'q':
                logout()
            warning()
            continue
        elif userInLesson >= 'A' and userInLesson <= 'Z':
            warning()
            continue
        elif int(userInLesson) == 0 or int(userInLesson) > 7:
            warning()
            continue
        elif userInLesson == '':
            warning()
            continue

        # Proses 
        # mengambil Datakeysection dengan indeks input user - 1
        # lalu simpan ke dalam variabel linkPilihan
        # lakukan penggabungan antara link parameter dengan variabel linkPilihan
        # lalu simpan hasil penggabungan pada variabel linkReady
        # klik link dengan parameter variabel linkReady
        keySectionUser = DataKeySection[int(userInLesson)-1]
        linkReady = link + keySectionUser
        browser.links.find_by_href(linkReady).click()
# AKHIR Fungsi Di Dalam Satu Mata Kuliah
############################ DALAM MASA PENGEMBANGAN | AKHIR WEBKULIAH ###############################


############################ AWAL LOGOUT ##################################
# Fungsi Logout 
# melakukan logout dari webkuliah maupun webbrowser
def logout():
    browser.quit()
    exit()
############################ AKHIR LOGOUT ##################################


# AWAL MENJALANKAN SCRIPT #
login()
on_web_kuliah()
logout()
# AKHIR MENJALANKAN SCRIPT #

######################################### FINISH ##########################################

# DALAM MASA PENGEMBANGAN # 
# FUNGSI MENU WEB KULIAH
# FUNGSI ON WEB KULIAH