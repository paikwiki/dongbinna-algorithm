# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    q05-choose-balls.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cbaek <cbaek@student.42seoul.kr>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/03 16:54:27 by cbaek             #+#    #+#              #
#    Updated: 2020/11/03 17:25:37 by cbaek            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Q05 볼링공 고르기 p.315.

_ = list(map(int, input().split()))
balls = list(map(int, input().split()))
result = 0

balls.sort()
for idx in range(0, len(balls) - 1):
	for idx_sub in range(idx, len(balls)):
		if balls[idx] != balls[idx_sub]:
			result += 1

print(result)

# 결과
# $ python codes/ch11/q05-choose-balls.py
# 8 5
# 1 5 4 3 2 4 5 2
# 25
