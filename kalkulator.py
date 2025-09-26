def tambah (a, b):
	return a + b
	
def kurang (a, b):
	return a - b

def kali (a, b):
	return a * b
	
def bagi (a, b):
	try:
		return a / b
	except ZeroDivisionError:
		return "Error: Tidak bisa dibagi 0"
		
def main():
	print("=== Kalkulator Sederhana ===")
	print("Pilih operasi:")
	print("1. Tambah")
	print("2. Kurang")
	print("3. Kali")
	print("4. Bagi")
	
	pilihan = input("Masukkan pilihan (1/2/3/4): ")
	
	try:
		x=float(input("Masukkan angka pertama: "))
		y=float(input("Masukkan angka kedua: "))
		
		if pilihan == "1":
			print("Hasil =", tambah(x,y))
		elif pilihan == "2":
			print("Hasil =", kurang(x,y))
		elif pilihan == "3":
			print("Hasil =", kali(x,y))
		elif pilihan == "4":
			print("Hasil =", bagi(x,y))
		else:
			print("Pilihan tidak valid.")
	except ValueError:
		print("Error: Input harus angka.")
		
if __name__ == "__main__":
    main() 