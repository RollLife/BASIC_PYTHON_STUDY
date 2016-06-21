list = ['가위', '바위','보']
list2 = [37,23,10,333, 29,49]

print(list)
print(list2)

print(list[1])
#1을 출력하면 2번째가 나옴

list[0] = '바위'

print(list)
print(list[-1])
# 리스트에서 -1은 뒤에서 1번째라는 뜻

print(list[-3])
# 리스트에서 -3은 뒤에서 3번재라는 뜻

#리스트를 추가하려면 append 함수를 써야한다.

list2.append(16)
print(list2)

#또한 이런 방법이 있다.

list3 = list2 + [16]
print(list3)

list4 = list2 + list3
print(list4)

del(list4[12]) #12번째 값을 지운다.
print (list4)

n=16
if n in list4:
	print('{}가 리스트에 있다.'.format(n))

#있는지 없는지 확인하는 조건문
 
list4.remove(16)
#같은 값이 많이 있다면 맨 첫번재 해당값을 지운다. del과 다르게 번째가 아닌 해당 값을 지우는 것이다.
print(list4)
