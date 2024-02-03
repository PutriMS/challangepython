num = int(input("Masukkan nilai Ganjil lebih dari 20\t="))
if num <= 20 :
    print("Bilangan salah!")
    num = int(input("Masukkan nilai Ganjil lebih dari 20\t="))
if num >= 21 :
    while num % 2 == 0:
        print("bilangan Salah!")
        num = int(input("Masukkan nilai Ganjil lebih dari 20\t="))
        
    else :
        print("Bilangan benar!")