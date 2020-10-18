# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex06-1.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cbaek <cbaek@student.42seoul.kr>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/18 23:23:44 by cbaek             #+#    #+#              #
#    Updated: 2020/10/18 23:28:49 by cbaek            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# 예제 6-1 - 선택 정렬 P.159.

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
	min_index = i # 가장 작은 원소의 인덱스
	for j in range(i + 1, len(array)):
		if array[min_index] > array[j]:
			min_index = j
	array[i], array[min_index] = array[min_index], array[i] # 스와프

print(array)

# 결과
# $ python codes/ch06/ex06-1.py
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
