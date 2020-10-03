# 실전문제 - 큰 수의 법칙 P.92. 답안2

# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수 정렬
first = data[n - 1] # 가장 큰 수
second = data[n -2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)	# 0으로 나누어떨어지지 않을 경우,
						# 마지막에 오는 두번째로 큰 수는 반드시 잘려나감.
						# 그러므로 count를 "m % (k + 1)"만큼 증가시킴
result = 0
result += (count) * first
result += (m - count) * second

print(result) # 결과 출력
