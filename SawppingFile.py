def Swapfiledata():
    f1=input("Enter file name")
    f2=input("Enter file name")
    with open(f1,"r") as A:
     data_A=A.read()
    with open(f2,"r") as B:
         data_B=B.read()
    with open(f1,"w") as A:
        A.write(data_B)
    with open(f2,"w") as B:
        B.write(data_A)             
Swapfiledata()