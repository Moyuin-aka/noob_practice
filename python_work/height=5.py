height=3
for i in range(1,height+1):
    for j in range(height-i):
        print(" ",end="")
    for l in range(i*2-1):
        print("*",end="")
    print()
        
for i in range(height-1,0,-1):
    for j in range(height-i):
        print(" ",end="")
    for l in range(i*2-1):
        print("*",end="")
    print()