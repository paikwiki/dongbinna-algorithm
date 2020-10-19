# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    q01-searching-for-parts3.py                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cbaek <cbaek@student.42seoul.kr>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/19 13:04:15 by cbaek             #+#    #+#              #
#    Updated: 2020/10/19 13:07:33 by cbaek            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# 실전문제 - 부품 찾기. 답안3(set() 함수). P.197.

# N(가게의 부품 개수)을 입력받기
n = int(input())
# 가게에 있는 전체 부품 번호를 입력받아서 집합(set) 자료형에 기록
array = set(map(int, input().split()))

# M(손님이 확인 요청한 부품 개수)을 입력받기
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
	# 해당 부품이 존재하는지 확인
	if i in array:
		print('yes', end=' ')
	else:
		print('no', end=' ')

# 결과
# $ python codes/ch07/q01-searching-for-parts3.py
# 5
# 8 3 7 9 2
# 3
# 5 7 9
# no yes yes
