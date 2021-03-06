# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex06-2.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cbaek <cbaek@student.42seoul.kr>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/18 23:28:28 by cbaek             #+#    #+#              #
#    Updated: 2020/10/18 23:29:57 by cbaek            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# 예제 6-2 - 파이썬 스와프(Swap) P.159.

# 0 인덱스와 1 인덱스의 원소 교체하기
array = [3, 5]
array[0], array[1] = array[1], array[0]

print(array)

# 결과
# $ python codes/ch06/ex06-2.py
# [5, 3]
