# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    q02-number-card-game2.py                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cbaek <cbaek@student.42seoul.kr>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/07 14:31:38 by cbaek             #+#    #+#              #
#    Updated: 2020/10/07 14:31:40 by cbaek            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# 실전문제 - 숫자 카드 게임 P.98. 답안2

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
	data = list(map(int, input().split()))
	# 현재 줄에서 `가장 작은 수` 찾기
	min_value = 10001
	for a in data:
		min_value = min(min_value, a)
	# '가장 작은 수'들 중에서 가장 큰 수 찾기
	result = max(result, min_value)

print(result) # 최종 답안 출력
