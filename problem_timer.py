import time


soru = 0 

def log():
    print("coded by root@ebby:~#")
    time.sleep(2)
    
def solve():
    while True:
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


log()
solve()        
        
    
    
    