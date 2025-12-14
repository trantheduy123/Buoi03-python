'''
Viết chương trình kiểm tra xem số N 
có phải là số hoàn hảo hay không? 
Biết số hoàn hảo là một số nguyên dương 
mà tổng các ước nguyên dương chính thức của nó bằng chính nó.
Ví dụ: 6 là số hoàn hảo vì 1+2+3=6 (1,2,3 là các ước)

'''
while True:
    n = int(input('nhap va gia tri n: '))
    if n > 0:
        break
tonguoc = 0
print(f'\n cac uoc {n}')
for i in range (1,n):
    if n%i== 0:
        print(i, end=',')
        tonguoc += i
print(f'\nTong cac uoc {tonguoc}')
if tonguoc == n:
     print(f' {n} la so hoan hao ')
else:
     print(f' {n}khong phai la so hoan hao')