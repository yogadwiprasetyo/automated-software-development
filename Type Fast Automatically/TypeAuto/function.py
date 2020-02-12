# Import modules dan packages
from splinter import Browser
import pyautogui as p
import time as t

# Inisialisai Class
# dilakukan untuk berinteraksi dengan webpage
browser = Browser()

# # FUNGSI WEB 10 FAST FINGERS #
# # Fungsi fast_fingers
# # membuka web 10fastfingers
# def fast_fingers(user):
# 	# Mengunjungi Link
# 	# link yang diberikan dari argument=user
# 	# Pesan
# 	# memberi pesan untuk memilih bahasa
# 	# lalu menjeda 40 detik
# 	browser.visit(user)
# 	print('\n\tWAKTU PILIH BAHASA 30 DETIK')
# 	print('\t\ttunggu sebentar')
# 	t.sleep(40)
# 	print('\t\tmulai mengetik')

# 	# Looping
# 	# melakukan proses waktu dan mengetik kata
# 	while True:
# 		# Waktu 
# 		# jika waktu = '0:00', lakukan looping
# 		# looping bertujuan memproses pertanyaan yang diberikan
# 		# jika pada pertanyaan tekan 'y', keluar
# 		# namun jika tekan 'n', ketik kembali
# 		# selain syarat diatas, beri pesan error
# 		# lalu keluar browser dan program
# 		waktu = browser.find_by_id('timer').text
# 		if waktu == '0:00':
# 			# while True:
# 			print('\t\tselesai mengetik')
# 			iUser2 = input('Keluar? (y/n): ')
# 			if iUser2 is 'y':
# 				print('\t\tkeluar')
# 				t.sleep(5)
# 				browser.quit()
# 				exit()
# 			elif iUser2 is 'n':
# 				iUser3 = input('Ketik lagi? (y): ')
# 				if iUser3 is 'y':
# 					browser.find_by_id('reload-btn').click()
# 					t.sleep(2)
# 					# break
# 				else:
# 					print('\t\tERROR: input tidak cocok')
# 					browser.quit()
# 					exit()

# 		# Kata
# 		# jika element id cocok dengan yang dicari
# 		# rubah element tersebut menjadi teks
# 		# lalu masukkan value elemen ke variabel kata
# 		# ketik value variabel kata
# 		# lalu tekan space
# 		# ulangi sampai waktu habis
# 		kata = browser.find_by_css('.highlight').text
# 		p.typewrite(kata)
# 		p.press('space')
# # END FUNGSI WEB 10 FAST FINGERS #


# FUNGSI WEB NGETIK MAYA #
# Fungsi ngetik_maya
# membuka web Ngetik Maya
def ngetik_maya(link):
	# Mengunjungi Link
	# link yang diberikan dari argument=user
	# memberi pesan mulai mengetik
	browser.visit(link)
	print('mulai mengetik')

	# Looping
	# melakukan proses waktu dan mengetik kata
	while True:
		# Waktu 
		# jika waktu = '0', lakukan looping
		# looping bertujuan memproses pertanyaan yang diberikan
		# jika pada pertanyaan tekan 'y', keluar
		# namun jika tekan 'n', ketik kembali
		# selain syarat diatas, beri pesan error
		# lalu keluar browser dan program
		waktu = browser.find_by_id('timer').text
		if waktu == '0':
			# while True:
			print('selesai mengetik')
			iUser2 = input('Keluar? (y/n): ')
			if iUser2 is 'y':
				print('keluar')
				t.sleep(5)
				browser.quit()
				exit()
			elif iUser2 is 'n':
				iUser3 = input('Ketik lagi? (y): ')
				if iUser3 is 'y':
					browser.reload()
					t.sleep(3)
				else:
					print('ERROR: input tidak cocok')
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
# END FUNGSI WEB NGETIK MAYA #


# # FUNGSI MENU PILIHAN #
# # Fungsi menu
# # memberikan pilihan menu awal
# def menu(link1,link2):
# 	# Looping
# 	# melakukan proses pilihan menu
# 	while True:
# 		print('''
# 			DAFTAR LINK

# 			1. 10 Fast Fingers
# 			2. Ngetik Maya

# 			tekan 'q' untuk keluar
# 			''')

# 		# Input User
# 		# value dari input user
# 		# dimasukkan ke dalam variabel iUser
# 		iUser = input('Masukkan nomer link: ')

# 		# Kondisi
# 		# jika iUser = 1,
# 		# pindah ke fungsi fast_fingers,
# 		# dengan parameter link, dari argument fungsi menu
# 		# jika iUser = 2, 
# 		# pindah ke fungsi ngetik_maya,
# 		# dengan parameter link, dari argument fungsi menu
# 		# jika iUser = 'q', keluar browser dan program
# 		# selain syarat diatas, beri pesan error
# 		# lalu keluar browser dan program
# 		if int(iUser) == 1:
# 			fast_fingers(link1)
# 		elif int(iUser) == 2:
# 			ngetik_maya(link2)
# 		elif str(iUser) is 'q':
# 			browser.quit()
# 			exit()
# 		else:
# 			print('ERROR: input tidak cocok')
# 			browser.quit()
# 			exit()
# # END FUNGSI MENU PILIHAN #