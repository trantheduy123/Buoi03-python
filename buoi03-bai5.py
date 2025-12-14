'''
Tuần 2 - Bài 5:Viết chương trình in bảng cửu chương 
từ 2 đến n (xuất ra theo cột);
'''
while True:
    n = int(input('nhap bang cuu chuong voi n>2: '))
    if n > 2:
        break
for i in range (1,11):
    for j in range (1, n+1):
        print(f'{j}x{i}={j*i}',end='\t')
    print('\n')
    