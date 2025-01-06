# practice

11111
11111
11111
11111
11111

#for i in range(5):

#    for j in range(5):
#        print('*****', end ="")
#        print()


#st1 = [1,2,3,4,5,6,7,8]
#st2 = st1[2:5]
#print(st2)
#st1[2:5]
#print(st1)

#st1[:] = []

#def gugudan(dan):
#    for i in range(1,10):
#        print(dan,"*", i ,"=", dan*i)

#gugudan(5)

#def circle_area(radius):
#    return 3.14 * radius * radius


#area = circle_area(5)
#print(area)

#def triangle_area(width, height):
#    return width * height / 2

#area = triangle_area(3, 4)
#print(area)

#def rec_area(x, y):
#    return x * y

#area = rec_area(3,4)
#print(area)

#def say_myself(name, man, age = 27):
#    pass

#result = 0
#for i in range(1, 1001):
#    result = result + i
#print(result)

#a = 20
#print (a)
#b= 10
#print (b)
#sum = a + b
#print = (sum) 

# 리스트 관련 함수


#st = [1,3,5,7,9]
#st.remove(1) # 리스트 안에 있는 값 삭제

#num = len(st)

#print(st)

#st = [1,2,3]
#st.append(4) # 리스트 안의 마지막 요소에 값을 집어넣음
#print(st)

#st.extend([5,6]) # [1, 2, 3, 4,+[ 5, 6]
#print(st)

#st = [1,2,4]
#st.insert(2,3) # 인덱스 값 2의 위치에 3을 저장

#print(st)

#st [1,9]
#st = []
#st.append(1)
#st.append(2)

#st.insert(0,1)
#st.insert(1,2)

#print(st)


#st = [1,2,3,4,5]
#print(st.pop(1)) #인덱스 값 0의 위치에 저장된 데이터 삭제

#print(st)
#st.remove(5)
#print(st)

#st. remove(3)
#print(st)

# 검색함수들
#st = [1,2,3,1,2]
#st.count(1)
#st.index(2) # 처음 2 등장하는 index 위치

#print (st[st.index(2)])

#string = "YoonSungWoo"
# oo의 개수는

#print(string.count('oo'))

#org = "kim"

#lcp = org.lower() # 모든 문자를 소문자로
#ucp = org.upper() # 모든 문자를 대문자로

#print(lcp)
#print(ucp)

org = " MIDDLE "

# 타 언어에서는 trim()
#cp1 = org.strip() # 앞뒤 공백 제거
#cp2 = org.lstrip() # 왼쪽 공백 제거
#cp3 = org.rstrip() # 오른쪽 공백 제거

#print(cp1)
#print(cp2)
#print(cp3)
#print(org)

#org = "heoo"
#rps = org.replace("he","ho") # 문자열 교체 함수
#print(rps)

#rps = org.replace("heo","")
#print(rps)

#org="Heee"

#rps = org.replace("e","o",1) # 첫번째 e만 바꾼다
#print(rps)

#rps = org.replace("e","o",2) # 두개를 o로 바꾼다
#print(rps)


#org = "ab_cd_ef"

#ret = org.split('_') # 글자 자르는데 return 값이 list
#print(ret)

#for string in ret:
#    print (string)

#tel = "020-1234-5678"
#org = "020_1234_5678"
#ret = org.split('_')
#print(ret)

#for string in ret:
#    print (string)

# 탐색 관련

#string = "What is important is that you should choose what is best for you"

#string.find("is") #index 값이 리턴됨
#string.rfind("is")#마지막 is가 있는 index값이 리턴됨
#string.count("is")#개수

#이스케이프(탈출)문자

string = "escape ₩n characters"
print(string)

string = "escape ₩/tcharacters"
print(string)

#두가지 정리
print("abcd",end="\n")
print("abcd")

# 두번째
#string = "escape '안녕하세요' characters"
#print(string)

#string = "escape '안녕하세요' characters"
#print(string)

#함수가 아닌 del(삭제) 명령


#st = [1,2,3,4,5]
#del st[:]
#del st[0]
#print(st)

#del st[1:3]
#print(st)

#del st
#print(st)
#num = 3
#del num
#print(num)


