# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex08-3.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cbaek <cbaek@student.42seoul.kr>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/20 18:17:12 by cbaek             #+#    #+#              #
#    Updated: 2020/10/20 18:46:50 by cbaek            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# 예제 8-3 - 호출되는 함수 확인 P.210.

d = [0] * 100

def pibo(x):
	print('f(' + str(x) + ')', end=' ')
	if x == 1 or x == 2:
		return 1
	if d[x] != 0:
		return d[x]
	d[x] = pibo(x - 1) + pibo(x - 2)
	return d[x]
pibo(6)

# 결과
# $ python codes/ch08/ex08-3.py
# f(6) f(5) f(4) f(3) f(2) f(1) f(2) f(3) f(4)