# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    q04-price-which-cannot-make.py                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cbaek <cbaek@student.42seoul.kr>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/02 20:54:47 by cbaek             #+#    #+#              #
#    Updated: 2020/11/02 21:55:10 by cbaek            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Q04 만들 수 없는 금액 p.314.

inputCount = int(input())
inputData = list(map(int, input().split()))

inputData.sort()
result = 1

for item in inputData:
	if result >= item:
		result += item
	else:
		break
print(result)

# 결과
# $ python codes/ch11/q04-price-which-cannot-make.py
# 5
# 3 2 1 1 9
# 8
