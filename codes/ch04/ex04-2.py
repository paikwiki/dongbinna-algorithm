# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex04-2.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cbaek <cbaek@student.42seoul.kr>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/11 17:03:21 by cbaek             #+#    #+#              #
#    Updated: 2020/10/11 17:08:34 by cbaek            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# 예제 4-2 - 시각 P.113.

# H를 입력받기
h = int(input())

count = 0
for i in range(h + 1):
	for j in range(60):
		for k in range(60):
			# 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
			if '3' in str(i) + str(j) + str(k):
				count += 1
print(count)
