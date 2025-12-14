'''
Tuần 2 - Bài 8:
Viết chương trình kiểm tra số n có phải là số nguyên tố
(số nguyên tố là số chỉ chia hết cho 1 và chính nó).
'''
so= int(input('nhap va gia tri so:'))
if so <2 :
    print('so khong phai la so nguyen to')
elif so == 2:
     print('so  la so nguyen to duy nhat la 2')
else:
    for i in range (2, so):
      if so%i==0:
          print(' khong phai la so nguyen to ',so)
    else:   
        print('la so nguyen to ',so)

