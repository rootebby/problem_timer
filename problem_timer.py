import time

soru = 0


print("coded by root@ebby:~#")
time.sleep(2)




while True:
    
    try:
            
        # Uyuma Süreleri # 
        print("Kalan Süre 60 !!!")
        time.sleep(10)
        print("Kalan Süre 50 !!!")
        time.sleep(10)
        print("Kalan Süre 40 !!!")
        time.sleep(10)
        print("Kalan Süre 30 !!!")
        time.sleep(10)
        print("Kalan Süre 20 !!!")
        time.sleep(10)
    

        
        
        
        # Soru Sayısı #
        print("Kalan Süre 10 !!!")
        time.sleep(10)
        print("Süre Bitti !")
        soru += 1
        time.sleep(0.8)
        print(f"{soru} soru çözdün !")
        time.sleep(0.8)
        print("Yeni Soruya Geç !!!")
        time.sleep(1)



    except KeyboardInterrupt:
        çözüldü = int(
            input("Çözülen Soru Sayısı : ")
            )
        if çözüldü <= 0:
            print("Dalga mı Geçiyorsun ??")
            
            break
            
        else:
            
        
            çözülen = çözüldü - soru
            if çözülen < 0 :
                print("Süreni Aştın , Kendini Geliştirmelisin !")
            
            elif çözülen > 0 : 
                print("Önde gidiyorsun , Harikasın !")
                
            else:
                print("Zamanın tam yetti , yine de çalışmalısın !!")
            
            break        
        


"""

soru = 0 

def log():
    print("coded by root@ebby:~#")
    time.sleep(2)
    
def solve():
    
    # Uyuma Süreleri # 
    print("Kalan Süre 60 !!!")
    time.sleep(10)
    print("Kalan Süre 50 !!!")
    time.sleep(10)
    print("Kalan Süre 40 !!!")
    time.sleep(10)
    print("Kalan Süre 30 !!!")
    time.sleep(10)
    print("Kalan Süre 20 !!!")
    time.sleep(10)
    # Soru Sayısı #
    print("Kalan Süre 10 !!!")
    time.sleep(10)
    print("Süre Bitti !")
    soru += 1
    time.sleep(0.8)
    print(f"{soru} soru çözdün !")
    time.sleep(0.8)
    print("Yeni Soruya Geç !!!")
    time.sleep(1)
        
def fark(çözüldü):
    çözülen = çözüldü - soru
    if çözülen < 0 :
        print("Kendini Geliştirmelisin !")
    
    elif çözülen > 0 : 
        print("Önde gidiyorsun , Harikasın !")
        
    else:
        print("Zamanın tam yetti , yine de çalışmalısın !!")
 
#def hesapla():
#    x = int(
#        input("Kaç soru çözdün ? : ")
#    )
#    
#    fark(x)


# __main__

log()
while True:
    try:
            
        solve()
    
    except:
        x = int(
            input("Çözülen Soru Sayısı : ")
        )               
        fark(x)

"""   
    
    
