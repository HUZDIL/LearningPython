import random
import time



uretilensayi = random.randint(1,50)
print(uretilensayi)

girilen_sayi = print(int(input("bir sayi giriniz")))

if(uretilensayi == girilen_sayi):
    print("dogru sayiyi buldunuz")
else:
    print("dogru sayiyi bulamadiniz")


