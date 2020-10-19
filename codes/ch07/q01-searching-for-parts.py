# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    q01-searching-for-parts.py                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cbaek <cbaek@student.42seoul.kr>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/19 12:37:44 by cbaek             #+#    #+#              #
#    Updated: 2020/10/19 12:51:16 by cbaek            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# 실전문제 - 부품 찾기 P.197.

# 이진 탐색 소스코드 구현(반복문)
def binary_search(array, target, start, end):
	while start <= end:
		mid = (start + end) // 2
		# 찾은 경우 중간점 인덱스 반환
		if array[mid] == target:
			return mid
		# 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
		elif array[mid] > target:
			end = mid - 1
		# 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
		else:
			start = mid + 1
	return None

# N(가게의 부품 개수) 입력
n = int(input())
# 가게에 있는 전체 부품 번호를 공백으로 구분하여 입력
array = list(map(int, input().split()))
array.sort() # 이진 탐색을 수행하기 위해 사전에 정렬 수행
# M(손님이 요청한 부품 개수) 입력
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
	# 해당 부품이 존재하는지 확인
	result = binary_search(array, i, 0, n - 1)
	if result != None:
		print('yes', end=' ')
	else:
		print('no', end=' ')

# 결과
# $ python codes/ch07/q01-searching-for-parts.py
# 5
# 8 3 7 9 2
# 3
# 5 7 9
# no yes yes
