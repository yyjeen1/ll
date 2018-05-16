engkor_dict={}
eng=input("영어 단어: ")
print("사전이 비어 있습니다.")
print("단어를 추가합니다.")
kor=input("한글 단어: ")
engkor_dict[e]=k
while True:
    e = input("영어 단어:")
    if(e == ""):
        break
    else:
        if e in engkor_dict:
            print("한글 단어:",endkor_dict[e])
            continue
        else:
            print(e, "단어가 등록되어 있지 않습니다.")
            print("단어를 추가합니다.")
            k=input("한글 단어: ")
            engkor_dict[e]=k
            continue
        break
print(engkor_dict)
