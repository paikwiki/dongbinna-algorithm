# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex05-1.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cbaek <cbaek@student.42seoul.kr>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/14 16:42:20 by cbaek             #+#    #+#              #
#    Updated: 2020/10/14 17:02:58 by cbaek            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# 예제 5-1 - 스택 P.126.

stack = []

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력

# 출력
# $ python codes/ch05/ex05-1.py
# [5, 2, 3, 1]
# [1, 3, 2, 5]
