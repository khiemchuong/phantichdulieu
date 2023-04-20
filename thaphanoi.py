def ThapHanoi(n , nguon, dich, phu):
    if n==1:
        print ("di chuyển 1 đĩa từ nguồn",nguon,"đến đích",dich)
        return
    ThapHanoi(n-1, nguon, phu, dich)
    print ("di chuyển đĩa",n,"từ nguồn",nguon,"đến đích",dich)
    ThapHanoi(n-1, phu, dich, nguon)
         

n =int(input('n='))
ThapHanoi(n,'A','B','C')