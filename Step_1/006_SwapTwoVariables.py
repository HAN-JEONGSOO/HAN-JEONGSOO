# Python program to swap two variables
# 두 변수를 바꾸는 파이썬 프로그램

x = 5
y = 10

# To take inputs from the user
#x = input('Enter value of x: ')
#y = input('Enter value of y: ')

# create a temporary variable and swap the values
# 임시변수를 만들어 요소를 바꾼다
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))
