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


############################ AWAL WEBKULIAH ###############################
# AWAL Fungsi menu_web_kuliah 
# menampilkan pilihan pada on_web_kuliah
def menu_web_kuliah():
    print('''
            ############# MATA KULIAH ############
            # 1. Algoritma II                    #
            # 2. Kalkulus II                     #
            # 3. Matematika Diskrit              #
            # 4. Pemrograman Visual              #
            # 5. Pendidikan Agama                #
            # 6. Pendidikan Pancasila            #
            # 7. Praktikum Algo II               #
            # 8. Praktikum Pemrograman Visual    #
            # 9. Praktikum Sistem Digital        #
            # 10. Praktikum Struktur Data        #
            # 11. Sistem Digital                 #
            # 12. Struktur Data                  #

            # tekan 'q' untuk Log out            #
            ######################################''')
# AKHIR Fungsi menu_web_kuliah

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

# AWAL Fungsi on_web_kuliah Utama
# menampilkan pilihan on_web_kuliah
def on_web_kuliah():
    # Inisialisasi Variabel
    # awal link dari mata kuliah
    linkCourse = 'https://webkuliah.unas.ac.id/course/view.php?'

    # Data List
    # data links dengan key mata kuliah masing-masing
    DataKeyMataKuliah = [
    'id=158588','id=158626','id=158648',
    'id=158677','id=158091','id=158170',
    'id=158697','id=158709','id=158721',
    'id=158729','id=158739','id=158756']

    # looping 
    # agar menampilkan menu_web_kuliah terus menerus
    # sampai keadaan False
    while True:
        menu_web_kuliah()

        # Input User
        # menyimpan value dari input user
        userOnWeb = input('''pilih mata kuliah: ''')
        
        # Kondisi
        # jika user tekan 'q', lakukan logout
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
        elif int(userOnWeb) == 0 or int(userOnWeb) > 12:
            warning()
            continue
        elif userOnWeb == '':
            warning()
            continue

        # Proses 
        # mengambil data key dari DataKeyMataKuliah dengan index userOnWeb
        # lakukan penggabungan data dengan key mata kuliah, 
        # sebagai link untuk masuk kedalam halaman mata kuliah
        # ambil judul mata kuliah, sebagai pemberitahuan posisi saat ini 
        keyPilihanUser = DataKeyMataKuliah[int(userOnWeb)-1]
        linkReady = linkCourse + keyPilihanUser
        browser.links.find_by_href(linkReady).click()
        judul = browser.find_by_css('.page-header-headings > h1:nth-child(1)').text
        in_one_lesson(linkReady,judul)
# AKHIR Fungsi on_web_kuliah Utama

# AWAL Fungsi Di Dalam Satu Mata Kuliah | DALAM MASA PENGEMBANGAN
# menampilkan menu pada satu mata kuliah
def in_one_lesson(link,judul):
    # Data List
    # DataKeySection sebagai link forum dari mata kuliah
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
        # menyimpan value dari input user
        userInLesson = input('pilih nomer forum: ')

        # Kondisi
        # jika user tekan 'b', masuk ke fungsi on_web_kuliah 
        # jika user tekan 'q', masuk ke fungsi logout 
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
        # mengambil data key dari DataKeySection dengan index userInLesson
        # lakukan penggabungan data dengan key section, sebagai link forum 
        keySectionUser = DataKeySection[int(userInLesson)-1]
        linkReady = link + keySectionUser
        browser.links.find_by_href(linkReady).click()
# AKHIR Fungsi Di Dalam Satu Mata Kuliah | DALAM MASA PENGEMBANGAN
############################ AKHIR WEBKULIAH ###############################


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

# CATATAN #
# FUNGSI MENU WEB KULIAH | SELESAI DIPERBARUI
# FUNGSI ON WEB KULIAH | SELESAI DIPERBARUI

# PROBLEM CHROME #
# PROBLEM IN ONE LESSON YAITU HANYA BISA MEMILIH SECTION KE BAWAH
# KETIKA MEMIILIH SECTION KE ATAS, ELEMENT YANG DICARI/DIKLIK TIDAK DITEMUKAN

# PENGEMBANGAN #
# FUNGSI IN ONE LESSON, MENAMBAHKAN FITUR UNTUK MASUK KE DALAM FORUM SECTION