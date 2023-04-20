def tinh_giai_thua(n):
    if n == 1:
        return 1
    else:
        return n * tinh_giai_thua(n - 1)
    
n=int(input('n='))
print(tinh_giai_thua(n)) 
