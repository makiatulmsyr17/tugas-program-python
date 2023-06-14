print ("========================\n")
print ("menghitung luas bangun datar")
print ("==========================")
print ("code rumus luas ")
print ("================")
print ("pp = persegi panjang")
print ("sgt = segitiga")
print ("lkrn = lingkran ")
print ("\n")

bangun = input ("masukan code rumus luas yang ingin dicari  : ")

#percabangan
if bangun == "pp" :
	p = input ("masukan panjang : ")
	l = input ("masukan lebar : ")
	luas = int (p) * int (l)
	print ("luas persegi panjang nya adaah ",luas)
elif bangun == "sgt" :
	a = input (" masukan alas : ")
	t = input (" masukan tinggi : ")
	luas = (int (a) * int (t))/2
	print ("luas segitiga nya adalah : ",luas )
elif bangun =="lkrn":
	r = input ("masukan jari jari : ")
	luas = 3.14 * int (r) * int (r)
	print ("luas lingkrannya adalah : " , luas )	
else :
	print ("kode yang anda masukan salah\nmohon ulangi " )	