# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    q08-string-sorting.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cbaek <cbaek@student.42seoul.kr>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/20 18:30:21 by cbaek             #+#    #+#              #
#    Updated: 2020/11/20 19:27:48 by cbaek            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Q08 문자열 재정렬 p.322.

inputData = input()

sumInteger = -1
characters = []

for chr in inputData:
	if chr.isnumeric():
		sumInteger += 1 + int(chr) if sumInteger < 0 else int(chr)
	else:
		characters.append(chr)
characters.sort()

print('{characters}{sumInteger}'.format(characters=''.join(characters), \
		sumInteger='' if sumInteger < 0 else sumInteger))
