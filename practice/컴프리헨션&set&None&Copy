#s1 = set([1,2,3,4,5,6])
#s2 = set([4,5,6,7,8,9])
#s3 = s1&s2 # 교집합
#print(s3)
#s3 = s1|s2 # 합집합
#s3 = s1-s2 # 차집합

#s1.update([4,5,6])
#print(s1)
#s1.remove(6)
#print(s1)

#set 응용 로또
#import random
#lotto = set()
#while len(lotto) < 6:
#    num = random.randint(1,45)
#    lotto.add(num)
#print(lotto)

#None의 이해
#my_value = 1

#print(my_value)

#my_value = None
#print(my_value)
#print(type(my_value))

#deep copy와 shallow copy
a = 1000
b = 1000

print(a==b)
print(id(a),id(b))
print(a is b)

a = 3
b = 3
print(a==b)
print(id(a),id(b))
print(a is b)

import copy
john = ['john',('man','usa'),[175,23]]

tom = list(john) #얕은 복사 껍데기만 새로 생성
chulsu = copy.copy(john)
younghee = copy.deepcopy(john) #안에 있는 값까지 새로 생성



john[2][1] += 1

print(john)
print(tom)
print(chulsu)
print(younghee)

#리스트의 생성과 그 리스트의 채울 데이터를 가공 추출하는 일련의 과정들을 하나로 묶기 위해 존재하는 것이 
#리스트 컴프리헨션이다.
r1 = [1,2,3,4,5]
r2 = []

r2= [x*2 for x in r1 if x % 2 == 0]#리스트 컴프리 헨션
print(r2)

