# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex06-4.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cbaek <cbaek@student.42seoul.kr>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/18 23:50:10 by cbaek             #+#    #+#              #
#    Updated: 2020/10/19 00:23:39 by cbaek            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# 예제 6-4 - 퀵 정렬 P.166.

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
	if start >= end: # 원소가 1개인 경우 종료
		return
	pivot = start # 피벗은 첫 번째 원소
	left = start + 1
	right = end
	while left <= right:
		# 피벗보다 큰 데이터를 찾을 때까지 반복
		while left <= end and array[left] <= array[pivot]:
			left += 1
		# 피벗보다 작은 데이터를 찾을 때까지 반복
		while right > start and array[right] >= array[pivot]:
			right -= 1
		if left > right: # 엇갈렸다면 작은 right -= 1 데이터와 피벗을 교체
			array[right], array[pivot] = array[pivot], array[right]
		else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
			array[left], array[right] = array[right], array[left]
	# 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
	quick_sort(array, start, right - 1)
	quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)

# 결과
# $ python codes/ch06/ex06-4.py
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
