# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    q01-from-top-to-bottom.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cbaek <cbaek@student.42seoul.kr>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/19 09:56:00 by cbaek             #+#    #+#              #
#    Updated: 2020/10/19 09:59:09 by cbaek            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# 실전문제 - 위에서 아래로 P.178.

# N 입력받기
n = int(input())

# N 개의 정수를 입력받아 리스트에 저장
array = []
for i in range(n):
	array.append(int(input()))

# 파이썬 기본 정렬 라이브러리를 이용하여 정렬 수행
array = sorted(array, reverse=True)

# 정렬이 수행된 결과를 출력
for i in array:
	print(i, end=' ')

# 결과
# $ python codes/ch06/q01-from-top-to-bottom.py
# 3
# 15
# 27
# 12
# 27 15 12
