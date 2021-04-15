MTSN = input().split()
M = int(MTSN[0])    #M종류 기계
T = int(MTSN[1])    #T종류 토큰
S = int(MTSN[2])
N = int(MTSN[3])
machine = []

nexttoken = 1       #1번토큰시작
nextmachine = S
#첫번째 방문 = S
curt = 1
curm = S
cnt = 0 
compute_list = []
residx = 0
is_tosolve = 0
token = 1
meCha = S
lst = []
for x in range(M*T):
    num = [eval(x) for x in input().split()]
    lst.append(num)

new_lst = [lst[i:i+T] for i in range(0, len(lst), T)]


while(True):
    compute_list.append((meCha,token))   #기계 토큰 순

    cnt += 1
    if cnt == N:
        break
    next_meCha = new_lst[meCha - 1][token - 1][1]
    next_token = new_lst[meCha - 1][token - 1][0]

    meCha, token = next_meCha, next_token
    if (meCha,token) in compute_list:
        residx = compute_list.index((meCha,token))
        is_tosolve = 1
        break
    else:
        o =1
if is_tosolve == 1: 
    real = cnt - residx #시작부터 얼마나 뒤에서부터 루프시작인지
    realN = N - cnt     #얼마나 남았는지
    oh = realN % real   
    curm = compute_list[oh+residx-1][0]





print(curm)