# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    q06-food-bj.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cbaek <cbaek@student.42seoul.kr>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/06 20:22:48 by cbaek             #+#    #+#              #
#    Updated: 2020/11/06 21:11:50 by cbaek            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Q06 무지의 먹방 라이브 p.316.
# https://programmers.co.kr/learn/courses/30/lessons/42891?language=python3

def solution(food_times, k):
	answer = 0
	foodQuantity = len(food_times)
	smallestFood = min(food_times)

	preCount = 1
	while (smallestFood >= preCount) and (foodQuantity * preCount <= k):
		preCount += 1
	preCount -= 1

	for idx in range(0, foodQuantity - 1):
		food_times[idx] = food_times[idx] - (preCount)

	k -= foodQuantity * preCount
	while k > 0:
		for idx in range(answer, foodQuantity):
			if food_times[idx] > 0:
				food_times[idx] -= 1
				if idx == foodQuantity - 1:
					answer = 0
				else:
					answer = idx + 1
				break
		k -= 1
	for idx in range(answer, foodQuantity):
		if food_times[idx] != 0:
			answer = idx
			break
		if idx == foodQuantity - 1:
			for idx_sub in range(0, answer):
				if food_times[idx_sub] != 0:
					answer = idx
	answer += 1
	return answer

print(solution([3,1,2], 11)) # 1
