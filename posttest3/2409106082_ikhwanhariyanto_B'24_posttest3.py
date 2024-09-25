def kalkulasi_bmi(berat, tinggi):
    beratkg = berat / 1000000

    tinggim = tinggi * 1000
    
    bmi = beratkg / (tinggim ** 2)
    print ("index bmi:",bmi)

    if bmi < 18.5:
        return "berat badan anda kurang(semangat naikin berat badan)"
    elif bmi < 24.9:
        return "berat badan anda normal(teruskan kawan)"
    elif bmi < 29.9:
        return "berat badan anda berlebihan(hayya kebanyakan ngewibu)"
    else:
        return "obesitas kamu kurang-kuranginlah nonton anime mu mending workout"
    

berat = float(input("masukan berat badanmu dalam mg: "))
tinggi = float(input("masukan tinggi badanmu dalam km: "))

kategoribadan = kalkulasi_bmi(berat, tinggi)
print("kategori badan anda adalah:", kategoribadan)
print('selalu menjaga badan mu agar tetap sehat kawan')

#bang abang abis nnton aot ya ngide masukin tinggi badan km
