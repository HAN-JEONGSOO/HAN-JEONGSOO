# 2차방정식 해 구하기 ax**2 + bx + c = 0

# math module Import하기
import cmath

a = 1
b = 5
c = 6

# 루트 안에 들어갈 판별식 d
d = (b**2) - (4*a*c)

# 두 가지 +- 모두 정의
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))
