n = int(input("Please enter the Value of n: "))

arr = [ 100, 20, 10 , 5 , 1]
out = 0


for i in range(len(arr)):
    Floor = n // arr[i]
    n = n - (Floor * arr[i])
    out = out + Floor
    if n:
        pass
    else:
        break

print ("The minimum number of bills is :" + str(out))
