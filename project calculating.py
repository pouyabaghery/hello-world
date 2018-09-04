#this project is about calculating several numbers
from sys import exit

#this part is about intro
print("1 : Shapes")
print("2 : Numbers")
print("0 : Exit")

#this part is about inputs of intro
vorudi = input("Enter the option number you choosed : ")
vorudi = int(vorudi)
pi = 3.14
#this part is about conditions of part "Shapes"
if vorudi ==1:
    print("1 = manshoor")
    print("2 = heram")
    print("3 = kore")
    print("4 = mokab mostatil")
    print("5 = mokab")
    vorudi1 = input("Choose your shape : ")
    vorudi1 = int(vorudi1)
    if vorudi1 ==1:
       a = input("Enter a : ")
       b = input("Enter b : ")
       h = input("Enter h : ")
       a = float(a)
       b = float(b)
       h = float(h)
       manshoor = 1/2 * a * b * h
       print("Hajm manshoor : ",manshoor)
    elif vorudi1 ==2:
        a = input("Enter a : ")
        b = input("Enter b : ")
        h = input("Enter h : ")
        a = float(a)
        b = float(b)
        h = float(h)
        heram = 1/3 * a * b * h
        print("Hajm heram : " , heram)
        masahat_ghaede = (a * h)/2
        print("Masahat ghaede : " , masahat_ghaede)

    elif vorudi1 ==3:
        r = input("Enter r : ")
        r = float(r)
        kore = pi * r**3 * 4/3
        print("Hajm kore : ",kore)
        masahat_dayre = pi * r**2
        print("masahat dayre : ",masahat_dayre)
        mohit = 2 * r * pi
        print("mohit dayre = ",mohit)

    elif vorudi1 ==4:
        a = input("Enter a : ")
        b = input("Enter b : ")
        h = input("Enter h : ")
        a = float(a)
        b = float(b)
        h = float(h)
        masahat = a**2
        print("Masahat mokab : ",masahat)
        mokab_mostatil = a * b * h
        print("hajm mokab mostatil : ",mokab_mostatil)
        mohit = (a + b)*2
        print("mohit : ",mohit)

    elif vorudi1 ==5:
        a = input("Enter a : ")
        a = float(a)
        mokab = a**3
        print("hajm mokab : ",mokab)
        masahat = a**2
        print("masahat moraba : ",masahat)
        mohit = a * 4
        print = ("mohit : ",mohit)

elif vorudi ==2:
    a = input("Enter a : ")
    b = input("Enter b : ")
    baze = input("Enter baze : ")
    baze = int(baze)
    a = float(a)
    b = float(b)
    
    jam = a + b
    tafrigh = a - b
    zarb = a * b
    taghsim = a / b
    print("hasel jam : ",jam)
    print("hasel tafrigh : ",tafrigh)
    print("hasel zarb : ",zarb)
    print("hasel taghsim : ",taghsim)

    flag = 0
    guess = a/2
    while abs(a - guess **2)>0.02:
        m = a/guess
        guess = (m + guess)/2
        flag = flag + 1
        print("jazr a : ",guess)
        print("flag : ",flag)

    guess = b/2
    while abs(b - guess **2)>0.02:
        m = b/guess
        guess = (m + guess)/2
        flag = flag + 1
        print("jazr b : ",guess)
        print("flag : ",flag)


    

    flag = 2

    while flag <= baze:
        prime = True
        counter = 2
    
        while counter < flag-1:
            if (flag % counter) ==0:
                prime = False        
            counter = counter + 1

        if (prime) :
            print(flag)

    
        flag = flag + 1
        
 
elif vorudi == 0 :
   exit(0)
        
        
        
    
