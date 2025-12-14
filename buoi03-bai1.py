'''
Bài 1: Viết chương trình countdown từ n về 1 (n>0) theo 2 cách.
'''
import time


n = int(input('nhap so nguyen n: '))
print(" bat dau dem nguoc")
while n > 0:
    print(n)
    time.sleep(1)
    n-=1
    
n = int(input('nhap so nguyen n:'))
print(" bat dau dem nguoc")
for i in range(n,0,-1):
    print(i)
    time.sleep(1)
    n-=1