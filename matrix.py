a=[[],[]]
for i in range(0,2):
    for j in range(0,2):
        print("array[",i,"],[",j,"]:=",end="")
        a[i].insert(j,int(input()))
        
for i in range(0,2):
    for j in range(0,2):
        print("array[",i,"],[",j,"]:=",a[i][j]);
        
