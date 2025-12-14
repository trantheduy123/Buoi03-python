'''
 Nhập vào một số nguyên n (n>0), tính các biểu thức sau đây:
§  A = tổng các số lẻ nhỏ hơn hay bằng n. 
§  B = tổng các số chẵn nhỏ hơn hay bằng n
§  C = tích các số từ 1 đến n
§  D = tích các số chia hết cho 3 nhỏ hơn hay bằng n

'''
while True: 
    n = int(input('Nhap vao so nguyen n: '))
    if n > 0:
        break
tongle = 0
str_tongle= 'A='

for i in range(1,n+1,2):
    tongle+=i
    str_tongle+=str(i)+'+'
print(str_tongle)
kq_tongle=str_tongle.rstrip('+')+'='+str(tongle)
print('Ket qua cua tong le la: ', kq_tongle)

tongchan = 0
str_tongchan= 'B='

for i in range(0,n+1,2):
    tongchan+=i
    str_tongchan+=str(i)+'+'
print(str_tongchan)
kq_tongchan=str_tongchan.rstrip('+')+'='+str(tongchan)
print('Ket qua cua tong chan la: ', kq_tongchan)

tongtich = 1
str_tongtich= 'C='

for i in range(1,n+1):
    tongtich*=i
    str_tongtich+=str(i)+'x'
print(str_tongtich)
kq_tongtich=str_tongtich.rstrip('x')+'='+str(tongtich)
print('Ket qua cua tong tich la: ', kq_tongtich)

tongchiahet3 = 1
str_tongchiahet3= 'D='

for i in range(1,n+1,3):
    tongchiahet3*=i
    str_tongchiahet3+=str(i)+'+'
if tongchiahet3 == 0:
    print("Khong ton tai D")
else:
    kq_tongchiahet3=str_tongchiahet3.rstrip('+')+'='+str(tongchiahet3)
    print('Ket qua cua tong chia het 3 la: ', kq_tongchiahet3)