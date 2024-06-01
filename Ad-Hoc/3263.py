def converter(num, bits):
    inverso = bits
    count = 0
    while count < num:
        inverso = inverso.replace('1', '2')  
        inverso = inverso.replace('0', '1')
        inverso = inverso.replace('2', '0')
        count += 1
    return inverso

N = int(input())
bits1 = input()
bits2 = input()

conversao = converter(N, bits1)

if conversao == bits2:
    print("Deletion succeeded") 
else:
    print("Deletion failed")
