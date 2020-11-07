# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    q07-lucky-straight.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cbaek <cbaek@student.42seoul.kr>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/07 17:31:04 by cbaek             #+#    #+#              #
#    Updated: 2020/11/07 17:42:23 by cbaek            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Q07 럭키 스트레이트 p.321.

inputData = input()
currentIndex = 0

leftValue = 0
rightValue = 0

for chr in inputData:
	if currentIndex < len(inputData) / 2: # 왼쪽
		leftValue += int(chr)
	else: # 오른쪽
		rightValue += int(chr)
	currentIndex += 1

if leftValue == rightValue: # 비교
	print("LUCKY")
else:
	print("READY")
