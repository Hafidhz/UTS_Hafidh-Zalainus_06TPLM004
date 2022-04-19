print("Hafidh Zalainus Sahrul A")
print("191011400463")
print("UTS Kecerdasan Buatan \n")

print ("perulangan for \n")
ulang = 10 
for i in range(ulang):
    print(f"perulangan ke-{i}")

print("\n list")
item=['agramas','stj','haryanto']
for isi in item:
    print(isi)

print ("\n perulangan while")
jawab = 'ya'
hitung = 0

while(True):
    hitung += 1
    jawab = input("Ulang lagi? ")
    if jawab == 'tidak':
        break

print(f"Total perulagan: {hitung}")