dex=input("문자열:")
def reverse(dex):
    rev=''
    for i in range(len(dex)-1,-1,-1):
        rev = rev + dex[i]
    return rev

print("개별 문자열 출력:",dex)
print("역순 문자열 출력:",reverse(dex))
