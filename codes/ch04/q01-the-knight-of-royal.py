# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    q01-the-knight-of-royal.py                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cbaek <cbaek@student.42seoul.kr>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/11 17:19:38 by cbaek             #+#    #+#              #
#    Updated: 2020/10/11 18:02:56 by cbaek            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# 실전문제 - 왕실의 나이트 P.115.

# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1
# ord(): https://docs.python.org/3/library/functions.html?highlight=ord#ord

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [
			(-2, -1), (-1, -2), (1, -2), (2, -1),
			(2, 1), (1, 2), (-1, 2), (-2, 1)
		]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
	# 이동하고자 하는 위치 확인
	next_row = row + step[0]
	next_column = column + step[1]
	# 해당 위치로 이동이 가능하다면 카운트 증가
	if next_row >= 1 and next_row <= 8 and \
			next_column >= 1 and next_column <= 8:
		result += 1

print(result)
