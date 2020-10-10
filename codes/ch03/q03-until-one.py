# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    q03-until-one.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cbaek <cbaek@student.42seoul.kr>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/10 17:39:01 by cbaek             #+#    #+#              #
#    Updated: 2020/10/10 18:06:32 by cbaek            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# 실전문제 - 1이 될 때까지 P.99.

n, k = map(int, input().split())
result = 0

# N이 K 이상이라면 K로 계속 나누기
while n >= k:
	# N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
	while n % k != 0:
		n -= 1
		result += 1
	# K로 나누기
	n //= k
	result += 1
# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
	n -= 1
	result += 1
print(result)
