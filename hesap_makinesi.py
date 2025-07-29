def hesap_makinesi():
    print("✨ Sanal Hesap Makinesi ✨")
    print("İşlem girin (örnek: 2+2, 10/5, 3*4)")
    print("Çıkmak için q yaz.\n")

    while True:
        islem = input("İşleminiz: ")

        if islem.lower() == 'q':
            print("Hesap makinesi kapatıldı. 👋")
            break

        try:

            # Sadece izin verilen karakterleri kontrol et
            izinli_karakterler = "0123456789+-*/(). "
            if all(char in izinli_karakterler for char in islem):
                sonuc = eval(islem)
                print("Sonuç =", sonuc)
            else:
                print("❌ Geçersiz karakter kullandın! Sadece + - * / ( ) ve sayılar kullanabilirsin.")
        except Exception as e:
            print("❌ Hata:", e)

hesap_makinesi()
