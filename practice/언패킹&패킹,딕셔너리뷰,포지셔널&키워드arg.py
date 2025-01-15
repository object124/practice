#키워드 인자 포지셔널 인자
#Positional argument=위치로 값을 주고 받음

#def  div(x,y):
#    return x-y
#div(4,1)
#Keyword argument=직접 변수 이용(위치 상관없이)
#div (x=4 , y= 1)
#keyword argument가 positional argument 앞에 오면 안됨

#def mul(x,y,/): #포지셔널 인자만 받겠다
#    return x*y
#mul(4,5)

#def only_keyword(*,x,y):#키워드 인자만 받겠다
#    return x+y
#only_keyword(x=1,y=2)
#only_keyword(1,2)

#2개 혼용
#def mix_fun(a,b,/,h,i,*,x,y): # ab는 포지셔널 인자만 받고 hi는 2개 다 써도 되고 xy는 키워드 인자만
#    print(a-b)
#    print(h-i)
#    print(x*y)

#mix_fun(1,2,3,i=4,x=5,y=6)

#=======================================================================

#dic 루핑
#d = dict(a=1,b=2,c=3)
#for k in d:
#    print(d[k],end=", ")

#for k in d.keys():
#    print(k, end = ", ")

#for v in d.values():#언패킹
#    print(k, end = ", ")

#for k,v in d.items():
#    print(k,v, end = ", ")

#=======================================================================

#딕셔너리 뷰 객체
#d = dict(a=1,b=2,c=3)
#뷰 객체는 단순히 키 또는 값을 얻어오는데 사용될 뿐만 아니라 현재 딕셔너리의 상태를 그대로 반영한다는 특징이 있다.
#('뷰'라는 이름처럼 딕셔너리의 현재 상태를 바라본다.)
#vo = d.items()  # view 객체 생성

#for kv in vo:
#    print(kv)

#d['a'] = d['a'] + 3 # 값 수정
#d['c'] += 2  # 값 수정

#for kv in vo:
#    print(kv)


#딕셔너리도 컴프리 헨션이 가능함
#d1 = dict(a=1,b=2,c=3)
#d2 = {k:v*2 for k,v in d1. items() }# d1 값을 2배 늘린 딕셔너리 생성
#print(d2)

#d3 = {k:v**2 for k,v in d1. items()}
#print(d3)

#맵과 필터

#def pow(n):
#    return n**2
#str1 = [1,2,3]
#st2 = [pow(str1[0]),pow(str1[1]),pow(str1[2])]
#st2

#=======================================================================

#맵 함수 데이터와 함수를 매핑하는 함수

#st2 = list(map(pow,str1))# pow 콜백 함수 =>연산이 끝나면 이터레이터 객체로 리턴됨

#ir = map(pow,str1) # 맵은 이터레이터 객체를 반환
#for i in ir:
#    print(i)

#print(st2)

#st1 = [1,2,3]
#st2 = [3,2,1]

#def sum(n1,n2):
#    return n1+n2

#st3= list(map(sum,st1,st2))#함수에 파라미터가 2개 이상일 경우
#st3

#람다와 같이 사용

#def rev(s):# "1234" "4321"
#    return s [::-1]
#s1 = ['one','two','three']
#ref = list(map(rev,s1))
#print(ref)

#람다 적용

#ref = list(map(lambda s:s[::-1],s1))
#print(ref)


#filter  함수 ->걸러내기
#def is_odd(n):

#    return n % 2 #홀수이면 True

#st = [1,2,3,4,5]
#ost = list(filter(is_odd,st))#True or False를 반환하는 함수가 들어와야 함 
#print(ost)

#=======================================================================

#필터 함수로 'gender' F 추출
#users = [{'mail': 'gregorythomas@gmail.com', 'name': 'Brett Holland', 'gender': 'M'},
#         {'mail': 'hintoncynthia@hotmail.com', 'name': 'Madison Martinez', 'gender': 'F'}]

#def is_female(user):
#    return user['gender'] == 'F'

#print(list(filter(lambda user:user['gender'] == 'F',users)))

#결과 데이터 반환을 위해 filter와 컴프리 헨션으로 효율적인 코딩 가능

#=======================================================================

#튜플 패킹과 언패킹
#tri_one=(12,15)
#print(tri_one)

#tri_two = 12,15
#print(tri_two)

#x,y=12,15# 복수 할당
#print(x,y)

#tri_three=(12,25)
#bt,ht=tri_three#튜플 언패킹
#print(bt,ht)

#nums = (1,2,3,4,5)
#n1, n2, *others = nums#둘 이상의 값을 리스트로 패킹 #변수 선언할 때 *의 의미
#변수 앞에 
#print(n1,n2,others)# 리스트로 묶는다

#num = (1,2,3,4,5)
#first, *others, last = num
#print(first,others,last)

#*others, n1, n2 = num
#print(others, n1, n2)


#=======================================================================


#함수에 * 적용
#함수에도  *를 파라미터처럼 쓸 수 있다
#1. *단독으로 파라미터로 쓸 때 ->def only_keyword(*,x,y):#키워드 인자만 받겠다
#    return x+y
#2. *변수명이 붙을 경우 = 묶는다(패킹) = 튜플로 묶는다
#3. 
#def show_nums(n1,n2,*others):#4,5는 튜플로 묶인다
#    print(n1,n2,others)

# * 파라미터의 응용
#show_nums(1,2,3,4,5)

#def sum(*num):
#    s = 0
#    for i in num:
#        s+=i
#    return s

#print(sum(1,2,3))
#print(sum(1,2,3,4,5,6,7,8,9))

def show_man(name,age,height):
    print(name,age,height)
p = ('Yoon', 22, 180)
show_man(*p) # 언패킹
#'함수를 호출할 때 *가 사용되면' 이는 튜플 언패킹으로 이어진다
#* 사용 위치에 따라 패킹 또는 언패킹
#언패킹 케이스는 튜플로 함수 호출할 때
#p에 담긴 값을 풀어서 각각의 매개 변수에 전달


