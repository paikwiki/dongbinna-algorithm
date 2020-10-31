# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    q02-multiply-or-sum.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cbaek <cbaek@student.42seoul.kr>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/31 15:35:16 by cbaek             #+#    #+#              #
#    Updated: 2020/10/31 15:43:21 by cbaek            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Q02 곱하기 혹은 더하기 p.312.

data = input()

result = int(data[0])
for i in range(1, len(data)):
	# 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 더하기 수행
	num = int(data[i])
	if num <= 1 or result <= 1:
		result += num
	else:
		result *= num

print(result)
