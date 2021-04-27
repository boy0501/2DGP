import copy

K = eval(input())
lst1 = [eval(i) for i in input().split()]
cnt = 0 
answer = copy.deepcopy(lst1)
answer.sort()
check = 0
goj = []
while True:
    if cnt == len(lst1):
        break
    if lst1 == answer:
        break
    dest = 0 
    i = cnt - 1
    for i in range(len(lst1)-1):
        if lst1[i]>lst1[i+1]:
            dest = i
    tmp = lst1[cnt]
    del lst1[cnt]
    lst1.insert(dest,tmp)
    #cnt += 1
    check += 1

print(check)
# import copy

# K = eval(input())
# lst1 = [eval(i) for i in input().split()]
# cnt = 0 
# answer = copy.deepcopy(lst1)
# answer.sort()
# check = 0
# goj = []
# while True:
#     if cnt == len(lst1):
#         break
#     if lst1 == answer:
#         break
#     if lst1[cnt] != cnt+1:
#         tmp = lst1[cnt]
#         if lst1[lst1[cnt]-1] == cnt+1:
#             goj.append(lst1[cnt]-1)
#             lst1[lst1[cnt]-1],lst1[cnt] = lst1[cnt],lst1[lst1[cnt]-1]
#             cnt += 1 
#         else:
#             myc = 0
#             for i in goj:
#                 if cnt < i :
#                     lst1[lst1[cnt]-1],lst1[cnt] = lst1[cnt],lst1[lst1[cnt]-1]
#                     goj.append(lst1[cnt]-1)
#                     #cnt += 1
#                     myc = 1
#                     break
#             if myc == 0:
#                 del lst1[cnt]
#                 lst1.insert(tmp-1,tmp)
#                 goj.append(tmp-1)
#     else:
#         cnt += 1
#     check += 1

# print(check)

# K,N = map(int,input().split())
# #K = 0의 개수
# #N = 숫자 까지 ㅇㅇ
# check = 0
# for i in range(N):
#     a = bin(i)
#     b = a[2:]           #0
#     a = bin(i+1)
#     c = a[2:]           #1

#     for i in range(len(b)): #작은길이기준
#         if b[-(i+1)] != c[-(i+1)]:
#             check += 1
#     for i in range(len(c)-len(b)):
#         if b[i] == "1":
#             check+=1
# print(check)



# import copy
# K,N = map(int,input().split())
# #K = 0의 개수
# #N = 숫자 까지 ㅇㅇ
# bin_list = []
# for i in range(K):
#     bin_list.append(0)
# big = []
# for i in range(N+1):
#     a = bin(i)
#     cnt = 0
#     for i in a[2:]:
#         len(a) 
#         if bin_list[-(len(a)-2) + cnt] != int(i):
#             bin_list[-(len(a)-2) + cnt] = 1
#         cnt += 1

#     big.append(copy.deepcopy(bin_list))
#     for i in range(K):
#         bin_list[i] = 0

# res = 0 
# sumres = 0 
# for i in range(N):
#     res = 0 
#     j = 0
#     for j in range(K):
#         if big[i][j] != big[i+1][j] :
#             res += 1
#     sumres += res

# print(sumres)


###########################
# M, T, S, N = [eval(x) for x in input().split()]

# token = 1
# meCha = S
# lst = []

# for x in range(M*T):
#     num = [eval(x) for x in input().split()]
#     lst.append(num)

# new_lst = [lst[i:i+T] for i in range(0, len(lst), T)]

# for x in range(N-1):
#     next_meCha = new_lst[meCha - 1][token - 1][1]
#     next_token = new_lst[meCha - 1][token - 1][0]

#     meCha, token = next_meCha, next_token

# print(meCha)
# s1 = [eval(i) for i in input().split()]
# total = sum(s1)
# m_list = []
# for i in range(total):
#     m_list.append(int(input()))
# m_dict = dict()
# for i in range(total):
#     if m_list[i] not in m_dict:
#         m_dict[m_list[i]] = 1
#     else:
#         m_dict[m_list[i]] += 1
# res_list = []
# for k,v in m_dict.items():
#     if v > 1:
#         res_list.append(k)
# res_list.sort()
# print(len(res_list))
# for i in res_list:
#     print(i)



# N = 6
# a = [[14,38,11,89,-1],[27,34,-1],[27,12,34,-1],[27,-1],[92,2,3,1,-1],[17,2,-1]]

# n_list = list()
# for i in a:
#     n_list.append(i[0])
# a.sort(key= lambda x:x[0])
# m_list = [[]]
# length = 0
# for i in range(len(a)):
#     if i == len(a)-1:
#         break
#     if a[i][0]!= a[i+1][0]:
#         m_list[length].append(a[i])
#         m_list.append([])
#         length+=1
#     else:
#         m_list[length].append(a[i])
# m_list[length].append(a[len(a)-1])
# print(m_list)
# depth = 0
# #깊이를 정함 
# for i in m_list:
#     depth += 1
#     if len(i)<2:
#         continue
#     else:
#         new_node  = [[]]
#         new_node[0].append(i[depth])
# for i in m_list:
#     i.sort(key=lambda x:x[1])
# print(m_list)
