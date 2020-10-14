# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex05-5.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cbaek <cbaek@student.42seoul.kr>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/14 17:11:28 by cbaek             #+#    #+#              #
#    Updated: 2020/10/14 17:16:10 by cbaek            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# 예제 5-5 - 2가지 방식으로 구현한 팩토리얼 P.129.

# 반복적으로 구현한 n!
def factorial_iteration(n):
	result = 1
	# 1부터 n까지의 수를 차례대로 곱하기
	for i in range(1, n + 1):
		result *= i
	return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
	if n <= 1: # n이 1 이하인 경우 1을 반환
		return 1
	# n! = n * (n - 1)!을 그대로 작성하기
	return n * factorial_recursive(n - 1)

# 각각의 방식으로 구현한 n! 출력(n = 5)
print('반복적으로 구현: ', factorial_iteration(5))
print('재귀적으로 구현: ', factorial_recursive(5))

# 출력
# $ python codes/ch05/ex05-5.py
# 반복적으로 구현:  120
# 재귀적으로 구현:  120
