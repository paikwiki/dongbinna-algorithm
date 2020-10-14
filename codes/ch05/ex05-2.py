# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex05-2.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cbaek <cbaek@student.42seoul.kr>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/14 16:56:01 by cbaek             #+#    #+#              #
#    Updated: 2020/10/14 17:02:54 by cbaek            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# 예제 5-2 - 큐 P.129.

from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 다음 출력을 위해 역순으로 바꾸기
print(queue)

# 출력
# $ python codes/ch05/ex05-2.py
# deque([3, 7, 1, 4])
# deque([4, 1, 7, 3])
