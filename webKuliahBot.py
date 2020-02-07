from splinter import Browser
from base64 import b64decode
import pyautogui as p
# import time as t

############## START ###################
# Membuat Instance dari class Browser
# digunakan untuk berinteraksi dengan web
browser = Browser()

############################ LOGIN ###############################
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

# login
def login():
	# mengunjungi web kuliah
	browser.visit('https://webkuliah.unas.ac.id/login/index.php')
	# mengisi username
	username = dec_un()
	browser.find_by_id('username').fill(username)
	# mengisi password
	password = dec_pw()
	browser.find_by_id('password').fill(password)
	# submit/masuk web kuliah
	browser.find_by_id('loginbtn').click()

############################ LOGIN ###############################

############################ DALAM MASA PENGEMBANGAN | WEBKULIAH ###############################

# Inisialisasi Variabel
# awalan link dari mata kuliah
links = 'https://webkuliah.unas.ac.id/course/view.php?'

# Fungsi on_web_kuliah Utama
# menampilkan pilihan on_web_kuliah
def on_web_kuliah(link):
	# Data List | DALAM MASA PENGEMBANGAN
	# data links dengan key mata kuliah masing-masing
	DataKeyMataKuliah = [
	'id=153898','id=153898','id=153898',
	'id=153898','id=153898','id=153898',
	'id=153898','id=153898','id=153898','id=153898']

	# looping | DALAM MASA PENGEMBANGAN
	# agar menampilkan on_web_kuliah terus menerus
	# sampai keadaan False
	while True:
		print('''
			####### MATA KULIAH #######
			# 1. Algoritma            #
			# 2. namamatakuliah       #
			# 3. namamatakuliah       #
			# 4. namamatakuliah       #
			# 5. namamatakuliah       #
			# 6. namamatakuliah       #
			# 7. namamatakuliah       #
			# 8. namamatakuliah       #
			# 9. namamatakuliah       #
			# 10. namamatakuliah      #

			# tekan 'q' untuk Log out #
			###########################
			''')

		# Input User
		# menyimpan value dari input pada variabel userPilihan
		userPilihan = input('Masukkan nomer mata kuliah: ')
		
		# Pengambil Keputusan
		# jika userpilihan = 'q', lakukan logout
		# jika userpilihan = '0' atau userpilihan '' atau userpilihan > 10
		# lakukan loncat ke input user
		if userPilihan == 'q':
			logout()
		elif userPilihan == '0' or userPilihan == '' or int(userPilihan) > 10:
			continue

		# Proses 
		# mengambil datakeymatakuliah dengan indeks input user - 1
		# lalu simpan ke dalam variabel linkPilihan
		# lakukan penggabungan antara link parameter dengan variabel linkPilihan
		# lalu simpan hasil penggabungan pada variabel linkReady
		# klik link dengan parameter variabel linkReady
		# lalu masuk ke fungsi in_one_lesson dengan variabel linkReady sebagai parameter
		linkPilihan = DataKeyMataKuliah[int(userPilihan)-1]
		linkReady = link+linkPilihan
		browser.links.find_by_href(linkReady).click()
		in_one_lesson(linkReady)

# Fungsi Di Dalam Satu Mata Kuliah
# menampilkan menu pada satu mata kuliah
def in_one_lesson(link):
	# Data List
	# menaruh keysection
	# untuk dipakai link parameter
	KeySection = [
	'#section-3', '#section-4', '#section-5',
	'#section-6','#section-8','#section-9','#section-10'
	]

	# looping
	# agar menampilkan on_web_kuliah terus menerus
	# sampai keadaan False
	while True:
		print('''
			######## FORUM MATA KULIAH #######

			 1. Materi Kuliah Dokumen           
			 2. Materi Video E-learning
			 3. Tugas Kuliah-1
			 4. Tugas Kuliah-2
			 5. Perkuliahan Online
			 6. UTS
			 7. UAS    

			 tekan 'b' untuk ke Dashboard/on_web_kuliah
			 tekan 'q' untuk Logout/Keluar
			##################################
			''')

		# Input User
		# menaruh value input ke dalam variabel userPilihan
		userPilihan = input('Masukkan nomer mata kuliah: ')

		# Pengambil Keputusan
		# jika userPilihan == 'b', masuk ke fungsi on_web_kuliah 
		# jika userPilihan == 'q', masuk ke fungsi logout 
		# jika userPilihan == '0' atau userPilihan == '' atau userPilihan > 7
		# lakukan loncat ke input user
		if userPilihan == 'b':
			# browser.reload()
			# browser.back()
			on_web_kuliah('https://webkuliah.unas.ac.id/course/view.php?')
		elif userPilihan == 'q':
			logout()
		elif userPilihan == '0' or userPilihan == '' or int(userPilihan) > 7:
			continue

		# P# Proses 
		# mengambil keysection dengan indeks input user - 1
		# lalu simpan ke dalam variabel linkPilihan
		# lakukan penggabungan antara link parameter dengan variabel linkPilihan
		# lalu simpan hasil penggabungan pada variabel linkReady
		# klik link dengan parameter variabel linkReady
		linkPilihan = KeySection[int(userPilihan)-1]
		linkReady = link+linkPilihan
		browser.links.find_by_href(linkReady).click()

############################ DALAM MASA PENGEMBANGAN | WEBKULIAH ###############################

############################ LOGOUT ##################################

# Fungsi Logout
# melakukan logout dari webkuliah maupun webbrowser
def logout():
	# Inisalisasi Variabel
	# menaruh posisi profile pada variabel profile
	# menaruh posisi logout pada variabel keluarWeb
	# lalu lakukan klik, pada kedua variabel tersebut
	# keluar webkuliah
	# keluar browser
	# keluar program
    profile = 882, 165
    keluarWeb = 729, 452
    p.click(profile,duration=1)
    p.click(keluarWeb,duration=1)
    browser.quit()
    exit()

############################ LOGOUT ##################################

# MENJALANKAN SCRIPT #

login()
on_web_kuliah(links)
logout()

# MENJALANKAN SCRIPT #
