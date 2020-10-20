# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    q02-ant-warrior.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cbaek <cbaek@student.42seoul.kr>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/20 19:03:58 by cbaek             #+#    #+#              #
#    Updated: 2020/10/20 20:08:39 by cbaek            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# 실전문제 - 개미 전사 P.220.

# 정수 N을 입력받기
n = int(input())
# 모든 식량 정보 입력 받기
array = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
	d[i] = max(d[i - 1], d[i - 2] + array[i])

# 계산된 결과 출력
print(d[n - 1])

# 결과
# $ python codes/ch08/q02-ant-warrior.py
# 4
# 9 1 3 6
# 15
#
# $ python codes/ch08/q02-ant-warrior.py
# 6
# 9 1 3 6 2 3
# 18
