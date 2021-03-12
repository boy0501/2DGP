
arr = []
cnt = 0
for i in range(8):
    arr = input()
    for j in range(8):
        if i % 2 == 0:
            if j % 2 == 0 :
                if arr[j] == 'F':
                    cnt+=1
        elif i % 2 ==1:
            if j%2 ==1:
                if arr[j] == 'F':
                    cnt+=1
                    

print(cnt)

                    
    
