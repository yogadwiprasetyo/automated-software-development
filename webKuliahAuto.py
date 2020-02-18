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
    isiFile = b64decode(file.read())
    un = isiFile.decode()
    file.close()
    return str(un)

# decode password
def dec_pw():
    file = open("p.txt", "r")
    isiFile = b64decode(file.read())
    pw = isiFile.decode()
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
# AWAL Fungsi tampilan_matkul | DALAM MASA PENGEMBANGAN
# menampilkan pilihan pada matkul
def tampilan_matkul():
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
# AKHIR Fungsi tampilan_matkul | DALAM MASA PENGEMBANGAN

# AWAL Fungsi tampilan_forum
# menampilkan pilihan pada forum
def tampilan_forum(namaMatkul):
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

            # Forum {} #'''.format(namaMatkul,namaMatkul))
# AKHIR Fungsi tampilan_forum

# AWAL Fungsi warning
# memberi pesan error input
def warning():
    print('WARNING: input tidak diketahui, silahkan isi kembali!')
# AKHIR Fungsi warning

# AWAL Fungsi matkul | DALAM MASA PENGEMBANGAN
# memproses pilihan user pada mata kuliah
def matkul():
    # Inisialisasi Variabel
    # awal link dari mata kuliah
    linkCourse = 'https://webkuliah.unas.ac.id/course/view.php?'

    # Data List | DALAM MASA PENGEMBANGAN
    # data key mata kuliah 
    DataKeyMatkul = [
    'id=153898','id=153909','id=154719',
    'id=153924','id=154067','id=154079',
    'id=151110','id=154115','id=154126','id=150274']

    # looping 
    # agar menampilkan tampilan_matkul terus menerus
    # sampai keadaan False
    while True:
        tampilan_matkul()

        # Input User
        # menyimpan value dari input pada variabel userMatkul
        userMatkul = input('pilih nomer mata kuliah: ')
        
        # Kondisi
        # jika userMatkul = 'q', lakukan logout
        # selain syarat diatas, abaikan lalu beri pesan warning
        # kembali ke input user
        if userMatkul >= 'a' and userMatkul <= 'z':
            if userMatkul == 'q':
                logout()
            warning()
            continue
        elif userMatkul >= 'A' and userMatkul <= 'Z':
            warning()
            continue
        elif int(userMatkul) == 0 or int(userMatkul) > 10:
            warning()
            continue
        elif userMatkul == '':
            warning()
            continue

        # Proses 
        # mengambil DataKeyMatkul dengan indeks, input user dikurang satu
        # lalu simpan ke dalam variabel keyMatkulUser
        # lakukan penggabungan antara linkCourse dengan keyMatkulUser
        # lalu simpan hasil penggabungan pada variabel linkReadyMatkul
        # mencari link yang cocok dengan linkReadyMatkul, lalu klik
        # ambil nama mata kuliah
        # lalu masuk ke fungsi forum 
        keyMatkulUser = DataKeyMatkul[int(userMatkul)-1]
        linkReadyMatkul = linkCourse + keyMatkulUser
        browser.links.find_by_href(linkReadyMatkul).click()
        namaMatkul = browser.find_by_css('.page-header-headings > h1:nth-child(1)').text
        forum(linkReadyMatkul,namaMatkul)
# AKHIR Fungsi matkul | DALAM MASA PENGEMBANGAN

# AWAL Fungsi forum
# memproses pilihan user pada forum
def forum(linkMatkul,namaMatkul):
    # Data List
    # Key forum pada mata kuliah
    DataKeySection = [
    '#section-3', '#section-4', '#section-5',
    '#section-6','#section-8','#section-9','#section-10'
    ]

    # looping
    # agar menampilkan tampilan_forum terus menerus
    # sampai keadaan False
    while True:
        tampilan_forum(namaMatkul)

        # Input User
        # menaruh value input ke dalam variabel userForum
        userForum = input('pilih nomer forum: ')

        # Kondisi
        # jika userForum == 'b', masuk ke fungsi matkul 
        # jika userForum == 'q', masuk ke fungsi logout 
        # selain syarat diatas, abaikan lalu beri pesan warning
        # kembali ke input user
        if userForum >= 'a' and userForum <= 'z':
            if userForum == 'b':
                dashboard = 'ul.list-group:nth-child(2) > li:nth-child(1) > a:nth-child(1)'
                browser.find_by_css(dashboard).click()
                matkul()
            elif userForum == 'q':
                logout()
            warning()
            continue
        elif userForum >= 'A' and userForum <= 'Z':
            warning()
            continue
        elif int(userForum) == 0 or int(userForum) > 7:
            warning()
            continue
        elif userForum == '':
            warning()
            continue

        # Proses 
        # mengambil Datakeysection dengan indeks input user dikurang satu
        # lalu simpan ke dalam variabel KeySectionUser
        # lakukan penggabungan antara link parameter dengan keySectionUser
        # lalu simpan hasil penggabungan pada variabel linkReady
        # mencari link yang cocok dengan linkReadyForum, lalu klik
        keySectionUser = DataKeySection[int(userForum)-1]
        linkReadyForum = linkMatkul + keySectionUser
        browser.links.find_by_href(linkReadyForum).click()
# AKHIR Fungsi forum
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
matkul()
# AKHIR MENJALANKAN SCRIPT #

######################################### FINISH ##########################################

# DALAM MASA PENGEMBANGAN # 
# FUNGSI MENU WEB KULIAH
# FUNGSI ON WEB KULIAH