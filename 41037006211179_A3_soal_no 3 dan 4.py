print("=============================")
print("program mengolah nilai soal no 3 dan 4")
print("============================\n")

no=[]
nama=[]
tugas=[]
uts=[]
uas=[]
na=[]
ket =[]
#mengimput banyak data yang diiginkan 
banyak=int(input("jumlah mahasiswa : "))
for i in range(banyak):
  print()
  print("data ke- ", str(i+1))
  nama.append(input("masukan nama\t: "))
  tugas.append(int(input("masukan tugas\t: ")))
  uts.append(int(input("masukan uts \t: ")))
  uas.append(int(input("masukan uas \t:  ")))
  print()

# perhitungan nilai akhir  sebanyak jumlah mahasiswa
for i in range(banyak):
  no.append(str(i+1))
  na.append(((tugas[i])*30/100)+((uts[i])*30/100)+((uas[i])*40/100))
 
#tabel hasil perhitungan 
print("="*70)
print("\t no \t nama \t\t tugas \t uts \t uas\t na")
print ("="*70)
for i in range(banyak):
  print ("\t",no[i], "\t", nama[i],"\t", tugas[i], "\t",uts[i], "\t", uas[i], "\t", na[i])
  print ("_"*70)

#proses perhitugan nilai rata rata 
ratana =  (sum(na)/(banyak))
ratatugas = (sum(tugas)/(banyak))
ratauts = (sum(uts)/(banyak))
ratauas= (sum(uas)/(banyak))    
print ("rata rata \t\t",ratatugas, "\t",ratauts, "\t", ratauas, "\t", ratana)


print ("soal no 4")  
print ("=========\n")

#memanggil variabel nama dan nilai akhir yang sudah di input tadi
for i in range (banyak):
  no.append(str(i+1))
  print ("masukan nama : ",nama[i])
  print ("masukan nilai : ",na[i])
  print("\n")

#percabangan untuk yng lulus dan tidak lulus
for j in na:
  if j >= 60 :
    ket.append("Lulus")
  elif j < 60 :
    ket.append("Tidak Lulus")

#tabel hasil nilai dan peyeleksian luulus dan tidak
print("\t no \t nama \t\t nilai \t\t\t keterangan ")
print ("="*70)

for i in range(banyak):
  no.append(str(i+1))
  print ("\t",no[i], "\t", nama[i],"\t\t", na[i],"\t","\t\t", ket[i])
  print ("_"*70)

print ("\nJumlah Mahasiswa\t:", banyak )
print ("Rata-rata nilai\t\t:", ratana)
print ("Nilai tertinggi\t\t:", max(na))
print ("Nilai terendah\t\t:", min(na))
print ("Jumlah lulus\t\t: " + str (ket.count('Lulus')))
print ("Jumlah tidak lulus\t: " + str (ket.count('Tidak Lulus')))
