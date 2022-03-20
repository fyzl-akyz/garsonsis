masa1 = 0
masa2 = 0
masa3 = 0

#masaların bakiyeleri sıfırladım

while(True):

    print("1 - Masa 1 Hesabı :", masa1, "\n2 - Masa 2 Hesabı :", masa2, "\n3 - Masa 3 Hesabı :", masa3 ,"\n4 - Çıkış ")
    # masaların hesaplarını yükledim
    x = int(input("Lütfen Seçim Yapın : "))
    if(x ==1):
        print("Masa 1 Hesabı :",masa1,"TL\n 1 - Sipariş Kaydı Oluştur \n 2 - Masanın Hesabını Sıfırla \n 3 - Ana Menüye Dön ")
        x1 = int(input("Seçim yapınız : "))
        if x1 == 1:
            print("Garsonsis v1.0 Menü Listesi \n ---- KEBAPLAR ---- \n 1 - Adana Kebap  20 TL \n 2 - Urfa Kebap 20 TL \n ----   Çorbalar ---- \n 3 - Mercimek Çorbası  10 TL \n 4 - Yayla Çorbası 10 TL\n ---- İçecekler -- \n 5 - 330 ml Pepsi Teneke Kola 9 TL \n 6 - 200 ml Sütaş Ayran 5 TL \n 7 - Doğanay 300 ml Şalgam 6 TL  \n 0 - Ana Menüye Dön  ")
            y = int(input("Seçim Yapınız : "))
            if(y == 1):
                z1 = int(input("Kaç tane istendi : "))
                z1 = z1 * 20
                masa1 = z1 + masa1

            elif( y == 2):
                z2 = int(input("Kaç tane istendi : "))
                z2 = z2 * 20
                masa1 = z2 + masa1

            elif (y == 3):
                z3 = int(input("Kaç tane istendi : "))
                z3 = z3 * 10
                masa1 = z3 + masa1

            elif (y == 4):
                z4 = int(input("Kaç tane istendi : "))
                z4 = z4 * 10
                masa1 = z4 + masa1

            elif (y == 5):
                z5 = int(input("Kaç tane istendi : "))
                z5 = z5 * 9
                masa1 = z5 + masa1

            elif (y == 6):
                z6 = int(input("Kaç tane istendi : "))
                z6 = z6 * 5
                masa1 = z6 + masa1

            elif (y == 7):
                z7 = int(input("Kaç tane istendi : "))
                z7 = z7 * 6
                masa1 = z7 + masa1


            elif (y == 0):
                continue
        elif x1 == 2:
            masa1 = 0
        elif x1 == 3:
            continue
    elif(x == 2):
        print("Masa 2 Hesabı :", masa2,
              "TL\n 1 - Sipariş Kaydı Oluştur \n 2 - Masanın Hesabını Sıfırla \n 3 - Ana Menüye Dön ")
        x2 = int(input("Seçim yapınız : "))
        if x2 == 1:
            print("Garsonsis v1.0 Menü Listesi \n ---- KEBAPLAR ---- \n 1 - Adana Kebap  20 TL \n 2 - Urfa Kebap 20 TL \n ----   Çorbalar ---- \n 3 - Mercimek Çorbası  10 TL \n 4 - Yayla Çorbası 10 TL\n ---- İçecekler -- \n 5 - 330 ml Pepsi Teneke Kola 9 TL \n 6 - 200 ml Sütaş Ayran 5 TL \n 7 - Doğanay 300 ml Şalgam 6 TL  \n 0 - Ana Menüye Dön  ")
            y = int(input("Seçim Yapınız : "))
            if (y == 1):
                z1 = int(input("Kaç tane istendi : "))
                z1 = z1 * 20
                masa2 = z1 + masa2

            elif (y == 2):
                z2 = int(input("Kaç tane istendi : "))
                z2 = z2 * 20
                masa2 = z2 + masa2

            elif (y == 3):
                z3 = int(input("Kaç tane istendi : "))
                z3 = z3 * 10
                masa2 = z3 + masa2

            elif (y == 4):
                z4 = int(input("Kaç tane istendi : "))
                z4 = z4 * 10
                masa2 = z4 + masa2

            elif (y == 5):
                z5 = int(input("Kaç tane istendi : "))
                z5 = z5 * 9
                masa2 = z5 + masa2

            elif (y == 6):
                z6 = int(input("Kaç tane istendi : "))
                z6 = z6 * 5
                masa2 = z6 + masa2

            elif (y == 7):
                z7 = int(input("Kaç tane istendi : "))
                z7 = z7 * 6
                masa2 = z7 + masa2


            elif (y == 0):
                continue
        elif x2 == 2:
            masa2 = 0
        elif x2 == 3:
            continue
    elif (x == 3):
        print("Masa 3 Hesabı :", masa3,
              "TL\n 1 - Sipariş Kaydı Oluştur \n 2 - Masanın Hesabını Sıfırla \n 3 - Ana Menüye Dön ")
        x3 = int(input("Seçim yapınız : "))
        if x3 == 1:
            print(
                "Garsonsis v1.0 Menü Listesi \n ---- KEBAPLAR ---- \n 1 - Adana Kebap  20 TL \n 2 - Urfa Kebap 20 TL \n ----   Çorbalar ---- \n 3 - Mercimek Çorbası  10 TL \n 4 - Yayla Çorbası 10 TL\n ---- İçecekler -- \n 5 - 330 ml Pepsi Teneke Kola 9 TL \n 6 - 200 ml Sütaş Ayran 5 TL \n 7 - Doğanay 300 ml Şalgam 6 TL  \n 0 - Ana Menüye Dön  ")
            y = int(input("Seçim Yapınız : "))
            if (y == 1):
                z1 = int(input("Kaç tane istendi : "))
                z1 = z1 * 20
                masa3 = z1 + masa3

            elif (y == 2):
                z2 = int(input("Kaç tane istendi : "))
                z2 = z2 * 20
                masa3 = z2 + masa3

            elif (y == 3):
                z3 = int(input("Kaç tane istendi : "))
                z3 = z3 * 10
                masa3 = z3 + masa3

            elif (y == 4):
                z4 = int(input("Kaç tane istendi : "))
                z4 = z4 * 10
                masa3 = z4 + masa3

            elif (y == 5):
                z5 = int(input("Kaç tane istendi : "))
                z5 = z5 * 9
                masa3 = z5 + masa3

            elif (y == 6):
                z6 = int(input("Kaç tane istendi : "))
                z6 = z6 * 5
                masa3 = z6 + masa3

            elif (y == 7):
                z7 = int(input("Kaç tane istendi : "))
                z7 = z7 * 6
                masa3 = z7 + masa3


            elif (y == 0):
                continue
        elif x3 == 2:
            masa3 = 0
        elif x3 == 3:
            continue


    elif (x == 4):
        break

