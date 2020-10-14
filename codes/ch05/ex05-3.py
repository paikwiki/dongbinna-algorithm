# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex05-3.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cbaek <cbaek@student.42seoul.kr>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/14 17:00:48 by cbaek             #+#    #+#              #
#    Updated: 2020/10/14 17:02:50 by cbaek            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# 예제 5-3 - 재귀 함수 P.130.

def recursive_function():
	print('재귀 함수를 호출합니다.')
	recursive_function()

recursive_function()

# 출력
# $ python codes/ch05/ex05-3.py
# 재귀 함수를 호출합니다.
# 재귀 함수를 호출합니다.
# 재귀 함수를 호출합니다.
# 재귀 함수를 호출합니다.
# 재귀 함수를 호출합니다.
# 재귀 함수를 호출합니다.
# 재귀 함수를 호출합니다.
# .
# .
# 재귀 함수를 호출합니다.
# Traceback (most recent call last):
#   File "codes/ch05/ex05-3.py", line 19, in <module>
#     recursive_function()
#   File "codes/ch05/ex05-3.py", line 17, in recursive_function
#     recursive_function()
#   File "codes/ch05/ex05-3.py", line 17, in recursive_function
#     recursive_function()
#   File "codes/ch05/ex05-3.py", line 17, in recursive_function
#     recursive_function()
#   [Previous line repeated 992 more times]
#   File "codes/ch05/ex05-3.py", line 16, in recursive_function
#     print('재귀 함수를 호출합니다.')
# RecursionError: maximum recursion depth exceeded while calling a Python object
