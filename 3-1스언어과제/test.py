n = eval(input("2진수로 변화하고 싶은 10진수 입력: "))
strg = []
def decimalToBinary(value):
    global strg
    strg.append(value%2)
    if value == 1:
        return value
    else:
        value = value//2
        return decimalToBinary(value)

decimalToBinary(n)
strg.reverse()
res =""
for i in strg:
    res += str(i)
print(res)
