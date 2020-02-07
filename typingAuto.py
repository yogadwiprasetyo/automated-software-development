# SEBELUM MENGGUNAKAN #
# mempunyai browser firefox
# menginstall module splinter dengan webdriver firefox dan pyautogui
# lebih bagus jalankan pada folder venv

# CARA MENJALANKAN #
# arahkan bash/cmd ke tempat file typingAuto.py
# lalu ketik dibawah ini sesuai sistem operasi
# Windows = py typingAuto.py
# Mac/Linux = python3 typingAuto.py

# Import Module dan Packages
from splinter import Browser
import pyautogui as p
import time as t

# Inisialisai Class
browser = Browser()

# Mengunjungi link
browser.visit('http://ngetik.maya.id/')

# Insialisai variabel 
i = 1

# Looping
while True:
	# Waktu 
	# jika waktu = '0', lakukan pesan selesai
	# keluar browser dan keluar program
	waktu = browser.find_by_id('timer').text
	if waktu == '0':
		print('selesai')
		t.sleep(5)
		browser.quit()
		exit()

	# Kata
	# jika element id cocok dengan yang dicari
	# rubah element tersebut menjadi teks
	# lalu masukkan value elemen ke variabel kata
	# ketik teks dengan kata sebagai parameter
	# lalu tekan space
	# ulangi sampai waktu habis
	kata = browser.find_by_id('currentword').text
	p.typewrite(kata)
	p.press('space')
	
	i+=1

