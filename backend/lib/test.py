l = str(input("enter votre CNI"))

cni = 203012

while(len(l)<6):
    l = "0"+l
print(str(cni)+l)
u = str(cni)+l


l = str(input("ajouter un autre "))


print(int(u) + 1)
