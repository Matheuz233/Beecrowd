while(True):
    a, b = input().split()
    
    if((a == '0') and (b == '0')):
        break

    carry, eleva = 0, 0
    
    if len(a) < len(b):
      while len(a) < len(b): 
        a = '0' + a
    if len(b) < len(a):
      while len(b) < len(a):
        b = '0' + b
    
    a = a[::-1]
    b = b[::-1]

    for i in range(0, len(a)):
        if (int(a[i]) + int(b[i]) > 9) or ((int(a[i]) + int(b[i]) + eleva)) > 9:
            carry += 1
            eleva = 1
        else:
            eleva = 0
            
    if(carry == 0):
        print("No carry operation.")
    elif(carry == 1):
        print("1 carry operation.")
    else:
        print(f"{carry} carry operations.")
