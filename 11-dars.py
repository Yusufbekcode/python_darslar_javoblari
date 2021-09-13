# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
f_soni=float(input("Biror raqam kiriting;"))
if f_soni%2:
    print("Bu juft son emas")
else:
    print("Rahmat!")

f_yosh=int(input("Yoshingiz nechchida?"))
if f_yosh<=4 or f_yosh>=60:
    print("Siz uchun kirish bepul")
elif f_yosh<18:
    print("Siz uchun kirish chiptasi 10000 so'm")
else:
    print("Siz uchun kirish chiptasi 20000 so'm")



print("Ikkita raqam kiriting!")
num1=float(input("Birinchi raqam:"))
num2=float(input("Ikkinchi raqam:"))
if num1<num2:
    print(num1, "<", num2)
elif num1>num2:
    print(num1, ">", num2)
elif num1==num2:
    print(num1, "=", num2)


mahsulotlar=['shaftoli', 'qovun', 'yogurt', 'non', 'sabzi', 'bodring', 'piyoz', 'go\'sht', 'kartoshka']
savat=[]
for mahsulot in range(5):
    savat.append(input(f"{mahsulot+1}- mahsulotni kiriting:"))
if mahsulotlar:
    for mahsulot in savat:
        if mahsulot in mahsulotlar:
            print(f"Do'konimizda {mahsulot} bor")
        else:
            print(f"Do'konmizda {mahsulot} yo'q")


mahsulotlar2=['qoshiq', 'stul', 'dazmol', 'qozon', 'choynak', 'tova', ]
savat=[]
for m in range(5):
    savat.append(input(f"{m+1}-mahsulot kiriting;"))
bor_mahsulotlar=[]
mavjud_emas=[]
for mahsulot2 in savat:
    if mahsulot2 in mahsulotlar2:
        bor_mahsulotlar.append(mahsulot2)
    else:
        mavjud_emas.append(mahsulot2)
if mavjud_emas:
    print("Do'konimizda quyidagi mahsulot yo'q:")
    for mahsulot2 in mavjud_emas:
        print(mahsulot2)
else:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")


foydalanuvchilar=['said', 'temur', 'wolf', 'burgut', 'telba']
login=input("Marhamat login yarating:\n>>>")
if login.lower() in foydalanuvchilar:
    print("Login band, yangi login tanlang!")
else:
    print("Xush Kelibsiz!🥳")


raqam2=int(input("Istalgan butun son kiriting:"))
bolinuvchilar=list(range(2,11))
for bolinuvchi in bolinuvchilar:
    if not raqam2%bolinuvchi:
        print(f"{raqam2} soni {bolinuvchi} ga qoldiqsiz bo'linadi")

