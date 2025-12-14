'''
Tuần 2 - 
Bài 6:Viết chương trình tìm ước chung lớn nhất 
của 2 số a,b nhâp từ bàn phím;
'''
while True:
    a = int(input('nhap va gia tri a: '))
    b = int(input('nhap va gia tri b: '))
    if a > 0 and b > 0 and a!=b:
         break
temp1,temp2 = a,b
while temp1 != temp2:
    if temp1>temp2:
        temp1 -= temp2
    else:
        temp2 -= temp1
print(f'UCLN a{a}vab{b} la {temp1}')
        