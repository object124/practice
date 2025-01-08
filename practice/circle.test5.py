print("hello world")
#import 선언 없이 언제든지 호출 가능한 함수

import math
from turtle import circle

print(math.pi) #math 모듈의 pi 상수 호출
print(math.sin(5))

from circle import *
print(circle.pi)