# IMPORT MODULE #
from selenium.webdriver import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base64 import b64decode
import time as t

# Insialisasi Class
# menjadikan variabel webdriver sebagai webdriver
webdriver = Firefox()
webdriver.get('http://apps.unas.ac.id:8080/login.do')

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

# START FUNGSI LOGIN #
# fungsi login
# melakukan pengisian form login
# lalu masuk ke website
def login():
	# Proses Login
	# jeda selama 10 detik
	# membuat variabel username dan password
	# untuk mengisi form login
	# ketik username dan password
	# lalu klik tombol login
    t.sleep(7)
    username = dec_un()
    password = dec_pw()
    webdriver.find_element_by_name("username").send_keys(username)
    webdriver.find_element_by_name("password").send_keys(password)
    webdriver.find_element_by_name("Submit").click()
# END FUNGSI LOGIN #


# START FUNGSI ALERT #
# Fungsi handling_alert
# menangani alert yang terdapat di browser 
def handling_alert():
	# Proses Handling Alert
	# membuat variabel wait sebgai, jeda/waktu
	# membuat variabel alert 
	# untuk mengambil objek alert ketika tampil
	# jika input user=b, terima alert lalu ke menu
	# selain syarat input diatas, beri pesan error
	wait = WebDriverWait(webdriver, 10)
	alert = wait.until(EC.alert_is_present())
	b = input('tekan b, ke menu: ')
	if str(b) is 'b':
		alert.accept()
		menu_utama()
	else:
		print('ERROR: input tidak diketahui')
# END FUNGSI ALERT #


# FUNGSI NEW WINDOW/TAB #
# Fungsi handling_wind_tab
# digunakan untuk menangani window baru yang tampil
# mempunyai parameter window
def handling_wind_tab(window):
	# Proses Handling Window
	# jeda waktu selama 1 detik
	# Looping
	# melakukan looping untuk mencari window baru
	# lalu berpindah ke window baru
	# jika input user=b, tutup window baru
	# dan pindah ke window utama
	# selain syarat input diatas, beri pesan error
	t.sleep(1)
	for window_handle in webdriver.window_handles:
	    if window_handle != window:
	        webdriver.switch_to.window(window_handle)
	        b = input('tekan b, ke menu: ')
	        if str(b) is 'b':
	        	webdriver.close()
	        	webdriver.switch_to.window(window)
	        	menu_utama()
	        else:
	        	print('ERROR: input tidak diketahui')
	        	exit()
# END FUNGSI NEW WINDOW/TAB #


# START FUNGSI MENU KIRI #
# Fungsi menu_kiri
# melakukan pilihan fungsi 1-7
# pada fungsi menu_utama
# mempunyai parameter user dan window
def menu_kiri(user,window):
	# Proses Menu Kiri
	# Element Xpath
	# menaruh xpath element pada variabel xpathMenu
	# mencari element lalu klik
	# jeda selama 1 detik
	# Kondisi Pertama
	# jika window ada yang baru
	# lakukan fungsi handling new window
	# Kondisi Kedua
	# jika alert tampil
	# lakukan fungsi handling alert
	# Element Xpath
	xpathMenu = '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr[{}]/td'.format(user)
	webdriver.find_element_by_xpath(xpathMenu).click()
	t.sleep(1)
	# Kondisi Pertama
	if len(window) != 1:
		handling_wind_tab(window)
	# Kondisi Kedua
	if EC.alert_is_present():
		handling_alert()
# END FUNGSI MENU PERTAMA #


# START FUNGSI MENU KANAN #
# Fungsi menu_kanan
# melakukan pilihan fungsi 8-14
# pada fungsi menu_utama
# mempunyai parameter user dan window
def menu_kanan(user,window):
	# Proses Menu Kanan
	# Looping
	# merubah input 8 - 15
	# menjadi 1 - 7,
	# karena xpath hanya bisa diakses 1 - 7
	# Element Xpath
	# menaruh xpath element pada variabel xpathMenu
	# mencari element lalu klik
	# jeda selama 1 detik
	# Kondisi Pertama
	# jika window ada yang baru
	# lakukan fungsi handling new window
	# Kondisi Kedua
	# jika alert tampil
	# lakukan fungsi handling alert
	# Looping
	i = 1
	for j in range(8, 15):
		if j == int(user):
			user = i
			break
		i += 1
	# Element Xpath
	xpathMenu = '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[{}]/td'.format(user)
	webdriver.find_element_by_xpath(xpathMenu).click()
	t.sleep(1)
	# Kondisi Pertama
	if len(window) != 1:
		handling_wind_tab(window)
	# Kondisi Kedua
	if EC.alert_is_present():
		handling_alert()
# END FUNGSI MENU KANAN #


# START FUNGSI PILIHAN MENU #
# Fungsi pilihan_menu
# menampilkan pilihan pada menu utama
def pilihan_menu():
	print('''
	############ ACADEMIC ONLINE SYSTEM ############

	1. Data Transkrip      8. Daftar Wisuda
	2. Histori Nilai       9. Kuesioner Dosen
	3. Jadwal Jurusan      10. Kehadiran Kuliah
	4. Jadwal Pribadi      11. Rencana Pembelajaran
	5. Mengisi KRS         12. Nilai Semester Aktif
	6. Jadwal PA           13. Data Keuangan
	7. Berita Acara PA     14. Ubah Password

		ketik DT untuk melihat Data Pribadi

			tekan 'q' keluar

	############ ACADEMIC ONLINE SYSTEM ############''')
# END FUNGSI PILIHAN MENU #


# START FUNGSI DATA PRIBADI #
# Fungsi data_pribadi
# menampilkan data pribadi
def data_pribadi():
	# Proses Data Pribadi
	# Element Xpath
	# menaruh xpath element pada variabel xpathData
	# mencari element lalu klik
	# Kondisi
	# jika input user=b, ke menu utama
	# selain syarat input diatas, beri pesan error
	# Element Xpath
	xpathData = '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/table'
	elementData = webdriver.find_element_by_xpath(xpathData).text
	tampilanData = '####### DATA PRIBADI #######\n\n{}\n\n####### DATA PRIBADI #######'.format(elementData)
	print(tampilanData)
	user = input('tekan b untuk kembali ke menu: ')
	# Kondisi
	if user == 'b':
		menu_utama()
	else:
		print('ERROR: input tidak diketahui')
# END FUNGSI DATA PRIBADI #


# START FUNGSI MENU UTAMA #
# Fungsi menu_utama #
# melakukan semua proses awal 
def menu_utama():
	# Proses Menu Utama
	# jeda waktu 1 detik
	# simpan ID window utama pada variabel original_window
	# Looping
	# mengulang tampilan menu
	# sampai keadaan False
	# Kondisi 
	# jika input user = 'q', keluar browser dan program
	# jika input user = 'DT', tampilkan Data Pribadi
	# jika input user = 1 - 8, masuk ke fungsi menu kiri
	# jika inpu user = 8 -14, masuk ke fungsi menu kanan
	# selain syarat input diatas, beri pesan error
	t.sleep(1)
	original_window = webdriver.current_window_handle
	# Looping
	while True:
		pilihan_menu()
		user = input('Pilih nomer: ')
		# Kondisi
		if str(user) == 'q':
			webdriver.quit()
			exit()
		elif str(user) == 'DT':
			data_pribadi()
		elif int(user) >= 1 and int(user) <= 7:
			menu_kiri(user,original_window)
		elif int(user) >= 8 and int(user) <= 14:
			menu_kanan(user,original_window)
		else:
			print('ERROR: input tidak diketahui')
# END FUNGSI MENU UTAMA #


# JALANKAN SCRIPT #
login()
handling_alert()
menu_utama()
# END JALANKAN SCRIPT #