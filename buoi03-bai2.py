fullname = input('nhap ho va ten cua ban: ')
for char in fullname:
    print(char, end=',')
print(' in ra cac ki tu co trong ten')
for char in fullname:
    if char == ' ':
        break
    print(char, end=',')
print(' in ra cac ki tu co trong ten ngoai tru khoang trang') 
for char in fullname:
    if char == '':
        continue
    print(char, end=',')
print(' in ra cac ki tu co trong ten co ki tu a/A')
for char in fullname:
    if char == 'a' or char == 'A':
        print('co ky tu a trong ten break')
        break
else:
    print('trong ten khong co ky tu a/A') 