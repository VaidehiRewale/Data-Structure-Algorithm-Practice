Check whether number is a prime number or not 
E.g. n=6, output=True 

 num=int(input("ENTER A NUMBER:"))
if num>1 and all(num%i!=0 for i in range(2,int(num**(0.5) +1))):
    print(f"True")
else:
    print(f"False")
