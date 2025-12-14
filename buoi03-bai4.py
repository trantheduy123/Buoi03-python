'''
Tuần 2 - Bài 4: Nhập 2 số nguyên x và y. 
Viết chương trình tính tổng bình phương các số từ x đến y.
'''
x = int(input('nhap va gia tri x: '))
y = int(input('nhap va gia tri y: '))
while True:
    if x > y:
        print('Nhap sai x > y')
        break
    elif x < y:
        break
tong = 0
for i in range (x,y+1):
    tong += i**2
print(f'tong binh phuong tu {x} den {y} la {tong}')
