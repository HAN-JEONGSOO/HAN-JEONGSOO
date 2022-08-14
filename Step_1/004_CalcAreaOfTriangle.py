# Python Program to find the area of triangle
# 삼각형 넓이를 구하는 파이썬 프로그램

a = 5
b = 6
c = 7

# Uncomment below to take inputs from the user
# a = float(input('Enter first side: '))
# b = float(input('Enter second side: '))
# c = float(input('Enter third side: '))

# semi-perimeter 계산하기
s = (a + b + c) / 2

# 넓이 계산
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)
